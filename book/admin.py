from django.contrib import admin
from .models import H_book, Booking

# Register your models here.
class H_a_book(admin.ModelAdmin):
    list_display = ['id','title', 'hot_price','price', 'ranks']
    list_editable = [ 'title', 'hot_price','price', 'ranks']
    list_filter = ['ranks']

admin.site.register(H_book, H_a_book)
admin.site.register(Booking)
