# Create Operation — Django Shell

This step creates a new `Book` record in the database.

## Command Executed

```python
>>> from bookshelf.models import Book

>>> book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )

>>> book
