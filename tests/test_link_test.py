import json,pytest
from lib.link_test import *

def test_checkProtocol():
    assert checkProtocol("github.com") == False
    assert checkProtocol("http:/github.com") == False
    assert checkProtocol("https://github.com") == True
    assert checkProtocol("https:/github.com") == False

def test_linkCheck():
    assert linkCheck("https://www.github.com")

@pytest.mark.xfail()
def test_linkCheck_fail():
    assert linkCheck("ThisDoesNotExist")
    assert linkCheck("http://ThisDoesNotExist.com")
    assert linkCheck("https://ThisDoesNotExist.com")
    assert linkCheck("http://www.ThisDoesNotExist.com")
    assert linkCheck("https://www.ThisDoesNotExist.com")
    assert linkCheck("https:/www.github.com")
