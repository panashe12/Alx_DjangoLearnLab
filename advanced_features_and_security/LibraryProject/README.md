
Permissions & Groups Setup:

1. Add custom permissions to Book model:
   - can_view
   - can_create
   - can_edit
   - can_delete

2. Create groups in Django Admin:
   - Viewers: can_view
   - Editors: can_view, can_create, can_edit
   - Admins: all permissions

3. Protect views using @permission_required:
   - book_list -> bookshelf.can_view
   - create_book -> bookshelf.can_create
   - edit_book -> bookshelf.can_edit
   - delete_book -> bookshelf.can_delete

# Security settings
# DEBUG must be False in production to prevent sensitive info leaks.
# CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE enforce HTTPS only cookies.
# CSP prevents XSS by allowing only self-hosted scripts/styles.
