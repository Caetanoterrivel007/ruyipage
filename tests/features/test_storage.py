# -*- coding: utf-8 -*-

import pytest


@pytest.mark.feature
def test_local_storage_roundtrip(page, fixture_page_url):
    page.get(fixture_page_url("storage_fixture.html"))

    page.local_storage.clear()
    page.local_storage.set("token", "abc123")
    page.local_storage["theme"] = "dark"

    assert page.local_storage.get("token") == "abc123"
    assert page.local_storage["theme"] == "dark"
    assert "token" in page.local_storage
    assert len(page.local_storage) == 2
    assert page.local_storage.items()["token"] == "abc123"


@pytest.mark.feature
def test_session_storage_roundtrip(page, fixture_page_url):
    page.get(fixture_page_url("storage_fixture.html"))

    page.session_storage.clear()
    page.session_storage.set("step", "2")
    page.session_storage.set("state", "active")

    assert page.session_storage.get("step") == "2"
    assert page.session_storage.get("state") == "active"
    assert sorted(page.session_storage.keys()) == ["state", "step"]
