# -*- coding: utf-8 -*-

import pytest

from ruyipage import FirefoxPage, launch


@pytest.mark.feature
def test_private_mode_with_options(opts_factory, temp_user_dir):
    page = FirefoxPage(opts_factory(private=True, user_dir=temp_user_dir))
    try:
        page.get("about:blank")
        assert page.url == "about:blank"
    finally:
        page.quit()


@pytest.mark.feature
def test_private_mode_with_launch(temp_user_dir):
    page = launch(headless=False, private=True, user_dir=temp_user_dir)
    try:
        page.get("about:blank")
        assert page.url == "about:blank"
    finally:
        page.quit()
