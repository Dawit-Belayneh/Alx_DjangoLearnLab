from django.contrib import admin
from .models import Book

# Custom admin class
class BookAdmin(admin.ModelAdmin):
    # Show these fields as columns in the admin list page
    list_display = ("title", "author", "publication_year")

    # Add filtering options on the right side
    list_filter = ("publication_year", "author")

    # Enable search bar for these fields
    search_fields = ("title", "author")

# Register with customization
admin.site.register(Book, BookAdmin)
