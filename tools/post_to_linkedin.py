#!/usr/bin/env python3
"""Post a text update to LinkedIn on behalf of the .env token owner.

Usage:
    python3 tools/post_to_linkedin.py "<post text>"

Reads LINKEDIN_TOKEN from .env in the current working directory.
Stdlib only — no pip install required.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

USERINFO_URL = "https://api.linkedin.com/v2/userinfo"
POSTS_URL = "https://api.linkedin.com/v2/ugcPosts"


def load_token() -> str:
    env_path = Path(".env")
    if not env_path.is_file():
        sys.exit("ERROR: .env not found in current directory. Run from the project root.")
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        if key.strip() == "LINKEDIN_TOKEN":
            return value.strip().strip('"').strip("'")
    sys.exit("ERROR: LINKEDIN_TOKEN not set in .env")


def http_request(url: str, *, method: str, headers: dict, body: bytes | None = None) -> tuple[int, dict, bytes]:
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read()


def resolve_author_urn(token: str) -> str:
    status, _headers, body = http_request(
        USERINFO_URL,
        method="GET",
        headers={"Authorization": f"Bearer {token}"},
    )
    if status != 200:
        sys.exit(f"ERROR: /v2/userinfo returned {status}: {body.decode('utf-8', 'replace')}")
    data = json.loads(body)
    sub = data.get("sub")
    if not sub:
        sys.exit(f"ERROR: /v2/userinfo response missing 'sub': {data}")
    return f"urn:li:person:{sub}"


def publish(token: str, author_urn: str, text: str) -> tuple[str, str]:
    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        },
    }
    status, headers, body = http_request(
        POSTS_URL,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "X-Restli-Protocol-Version": "2.0.0",
            "Content-Type": "application/json",
        },
        body=json.dumps(payload).encode("utf-8"),
    )
    if status < 200 or status >= 300:
        msg = body.decode("utf-8", "replace")
        hint = ""
        if status == 403:
            hint = (
                "\nHINT: 403 usually means the token is missing the w_member_social scope. "
                "Tokens from 'Sign In with LinkedIn' (OIDC) only have openid/profile/email. "
                "To post, your LinkedIn app needs the 'Share on LinkedIn' product enabled, "
                "and you must generate a new token with w_member_social explicitly requested."
            )
        sys.exit(f"ERROR: POST /v2/ugcPosts returned {status}: {msg}{hint}")
    urn = headers.get("x-restli-id") or headers.get("X-RestLi-Id") or ""
    if not urn:
        sys.exit(f"ERROR: post succeeded ({status}) but no x-restli-id header in response: {headers}")
    url = f"https://www.linkedin.com/feed/update/{urn}/"
    return urn, url


def main() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        sys.exit('Usage: python3 tools/post_to_linkedin.py "<post text>"')
    text = sys.argv[1]
    token = load_token()
    author_urn = resolve_author_urn(token)
    urn, url = publish(token, author_urn, text)
    print(f"Posted: {urn}")
    print(f"URL:    {url}")


if __name__ == "__main__":
    main()
