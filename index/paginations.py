from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """
    This class allow user define custom pagination in
    query params by 'size' key.
    http://www.sample.com/products/?size=`custom number of pagination`.
    """
    page_size_query_param = 'size'
