import pytest

from Base.base_object import Base_object
from Base.data import Data
from Base.driver import Driver


def data_tool(name):
    data = []
    for i in Data(name).values():
        data.append((i.get("input"),i.get("exc")))
    return data




class Test_search:

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.fixture(scope="class",autouse=True,)
    def click_search(self):
        Base_object.base_object_set().Page_Set_click()

    @pytest.mark.parametrize("text,loc",data_tool("data_search.yaml"))
    def test_search(self,text,loc):
        Base_object.base_object_search().page_set_search_input(text)
        assert loc in Base_object.base_object_search().page_set_search_text()
















































