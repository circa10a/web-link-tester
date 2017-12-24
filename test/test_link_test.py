import json,pytest
from lib.link_test import checkProtocol
from lib.link_test import createJson
from lib.link_test import linkCheck
def test_checkProtocol():
    assert checkProtocol("github.com") == False
    assert checkProtocol("http:/github.com") == False
    assert checkProtocol("https://github.com") == True
    assert checkProtocol("https:/github.com") == False

def test_createJson():
    assert json.dumps(createJson(200,"https://github.com"))

@pytest.mark.xfail(raises=TypeError)
def test_createJson_fail():
    assert json.dumps(createJson(200))

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
