import pytest

    # use xfail to mark exception assertion directly
    # @pytest.mark.xfail(raises=ZeroDivisionError)
    # def test_3(self):
    #     1/1
'''
    USE MAKERS
'''
@pytest.fixture()
def fixtureNotSpecified():
    print("directly call this fixture without using this fixuture explicitly ")
# pytestmark=pytest.mark.usefixtures("fixtureNotSpecified")
@pytest.mark.usefixtures("fixtureNotSpecified")
@pytest.mark.markersTest
def testRseFixtureNotSpecified():
    assert False


'''
    USE PARAMETRIZATION
'''
@pytest.mark.parametrization
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 7), ("6*9", 42)])
def test_eval(test_input, expected):
    print(test_input,expected)
    assert eval(test_input) == expected

'''
    tmp_path_retention_count = 3,use this opts to determine how many temp directoriess will be kept

'''
# @pytest.mark.test
def test_tmp_path(tmp_path):
    assert 0

'''
    monkey_patch: change obj
'''
@pytest.mark.test
def test_patch(monkeypatch):
    import os
    monkeypatch.setattr(os,'getcwd',lambda:'./')
    print(os.getcwd())
    assert 0

'''
    doctest
>>> x = 3
>>> x
3
'''
