UPDATE OPERATION

Update the book’s publication year to 1950.

>>> book = Book.objects.get(title="1984")
>>> book.publication_year = 1950
>>> book.save()

>>> book

Output
# <Book: 1984 by George Orwell>
# Updated successfully (publication_year = 1950)