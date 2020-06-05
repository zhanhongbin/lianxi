import allure
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


    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("设置点击搜索")
    @pytest.fixture(scope="class",autouse=True,)
    def click_search(self):
        Base_object.base_object_set().Page_Set_click()
        allure.attach("设置点击搜索")



    @allure.step("设置搜索内容判断是否存在")
    @pytest.mark.parametrize("text,loc",data_tool("data_search.yaml"))
    def test_search(self,text,loc):
        Base_object.base_object_search().page_set_search_input(text)
        allure.attach("设置搜索内容判断是否存在")
        assert loc in Base_object.base_object_search().page_set_search_text()
















































