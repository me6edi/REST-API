# from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import CursorPagination

# class MypageNumber(LimitOffsetPagination):
#     # page_size = 5
#     # page_query_param = 'p'
#     # page_size_query_param = 'records'
#     # max_page_size = 7
#     # # last_page_strings = 'end'


#     # limit offset
#     default_limit = 5
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'
#     max_limit = 6



class MypageNumber(CursorPagination):
    page_size = 5
    ordering = 'name'
    cursor_query_param = 'cu'