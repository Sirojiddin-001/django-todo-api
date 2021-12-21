from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'content': data,
            'pageable': {
                'total': self.page.paginator.count,
                'num_pages': self.page.paginator.num_pages,
                'current': self.page.number,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            }
        })
