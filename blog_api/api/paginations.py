from rest_framework.pagination import PageNumberPagination


class SmallPagePagination(PageNumberPagination):
    max_page_size = 100
    page_size = 10
    page_query_param = 'page'


class LargePagePagination(PageNumberPagination):
    max_page_size = 1000
    page_size = 100
    page_query_param = 'page'
