from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination


class PropertyPagination(PageNumberPagination):
    page_size = 3
    # page_query_apram='p'
    # page_size_query_param = 'size'
    # max_page_size=10
    # last_page_strings = 'end'

class PropertyLOPagination(LimitOffsetPagination):
    default_limit = 1