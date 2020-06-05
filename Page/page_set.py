from Base.base_tool import Base_Tool
from Page.element_page import Concentrated_Ele


class Page_Set(Base_Tool):
    """搜索页操作"""
    def Page_Set_click(self,timeout=10,poll_frequency=0.5):
        """设置首页点击搜索放大镜"""
        self.base_click(Concentrated_Ele.setup_click,timeout,poll_frequency)







































