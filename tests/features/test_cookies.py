# -*- coding: utf-8 -*-

import pytest


@pytest.mark.feature
@pytest.mark.local_server
def test_cookie_roundtrip_with_local_server(page, server):
    page.get(server.get_url("/set-cookie"))
    cookies = {c.name: c.value for c in page.get_cookies(all_info=True)}
    assert cookies.get("server_cookie") == "server_value"
    assert cookies.get("session_id") == "abc123"

    page.set_cookies(
        {
            "name": "api_cookie",
            "value": "api_value",
            "domain": "127.0.0.1",
            "path": "/",
        }
    )
    page.get(server.get_url("/get-cookie"))
    body_text = page.ele("tag:body").text
    assert "api_cookie=api_value" in body_text
