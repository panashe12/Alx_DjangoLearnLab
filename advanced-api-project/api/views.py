from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer


"""
This file contains generic views for handling CRUD operations
on the Book model using Django REST Framework.

We use DRF's generic views to reduce boilerplate code while
maintaining flexibility for customization.
"""


class BookListView(generics.ListAPIView):
    """
    GET /books/

    Returns a list of all books.
    Accessible to all users (read-only).
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<pk>/

    Returns a single book by ID.
    Accessible to all users (read-only).
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/

    Creates a new Book instance.
    Restricted to authenticated users only.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize object creation.
        Here we simply save the instance.
        This method allows additional logic like logging or modifying data.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<pk>/update/

    Updates an existing Book instance.
    Restricted to authenticated users only.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<pk>/delete/

    Deletes a Book instance.
    Restricted to authenticated users only.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
