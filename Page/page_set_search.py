from Base.base_tool import Base_Tool
from Page.element_page import Concentrated_Ele


class Page_set_search(Base_Tool):
    """搜索放大镜操作"""
    def page_set_search_input(self,text,timeout=10,poll_frequency=0.5):
        # 输入框输入操作
        self.base_input(Concentrated_Ele.setup_search_input,text,timeout,poll_frequency)


    def page_set_search_text(self,timeout=10,poll_frequency=0.5):
        # 获取元素文本
        return self.base_text(Concentrated_Ele.setup_search_text,timeout,poll_frequency)
















































