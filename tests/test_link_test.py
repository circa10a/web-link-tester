import json
import pytest
from lib.link_test import *


def test_valid_protocol():
    assert valid_protocol("github.com") == False
    assert valid_protocol("http:/github.com") == False
    assert valid_protocol("https://github.com") == True
    assert valid_protocol("https:/github.com") == False


def test_link_check():
    assert link_check("https://www.github.com")


def test_linkCheck_fail():
    with pytest.raises(Exception):
        assert link_check("ThisDoesNotExist")
        assert link_check("http://ThisDoesNotExist.com")
        assert link_check("https://ThisDoesNotExist.com")
        assert link_check("http://www.ThisDoesNotExist.com")
        assert link_check("https://www.ThisDoesNotExist.com")
        assert link_check("https:/www.github.com")


def test_validate_json():
    url = "https://github.com"
    test_pass_dict = {
        "url": url
    }
    test_pass_json = json.dumps(test_pass_dict)
    get_url_from_json = validate_json(json.loads(test_pass_json))
    assert get_url_from_json == url


def test_validate_json_fail():
    with pytest.raises(Exception):
        url = "https://github.com"
        test_fail_dict = {
            "urlbad": url
        }
        test_fail_json = json.dumps(test_fail_dict)
        get_url_from_json = validate_json(json.loads(test_fail_json))
