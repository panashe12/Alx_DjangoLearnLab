from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView (KEEP THIS)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users

    """
    Handles all CRUD operations for Book model.
    Permissions:
    - IsAuthenticated: only logged-in users can access
    - Optional: admin-only for update/delete
    Authentication:
    - TokenAuthentication: clients must provide token in header
    """

# NEW: ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



