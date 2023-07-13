from rest_framework import generics
from .models import Book, BookPagination
from .serializers import BookSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        exclude = self.request.query_params.get('exclude')

        kwargs['context'] = self.get_serializer_context()
        kwargs['fields'] = fields.split(',') if fields else None
        kwargs['exclude'] = exclude.split(',') if exclude else None

        return self.serializer_class(*args, **kwargs)
