import json
import pytest
from lib.link_test import *


def test_checkProtocol():
    assert checkProtocol("github.com") == False
    assert checkProtocol("http:/github.com") == False
    assert checkProtocol("https://github.com") == True
    assert checkProtocol("https:/github.com") == False


def test_linkCheck():
    assert linkCheck("https://www.github.com")


def test_linkCheck_fail():
    with pytest.raises(Exception):
        assert linkCheck("ThisDoesNotExist")
        assert linkCheck("http://ThisDoesNotExist.com")
        assert linkCheck("https://ThisDoesNotExist.com")
        assert linkCheck("http://www.ThisDoesNotExist.com")
        assert linkCheck("https://www.ThisDoesNotExist.com")
        assert linkCheck("https:/www.github.com")


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
