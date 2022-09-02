from django.contrib import admin
from .models import Book, Author, Address, Country


# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_filter = ('name', 'code')
    list_display = ('name', 'code')


class AddressAdmin(admin.ModelAdmin):
    list_filter = ('street', 'postal_code', 'city')
    list_display = ('street', 'postal_code', 'city')


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating')
    list_display = ('title', 'author', 'rating', 'is_bestselling')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
