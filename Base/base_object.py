from Page.page_set import Page_Set
from Page.page_set_search import Page_set_search


class  Base_object:
    @classmethod
    def base_object_set(cls):
        return Page_Set()
    @classmethod
    def base_object_search(cls):
        return Page_set_search()



























