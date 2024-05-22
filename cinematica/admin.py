from django.contrib import admin

from .models import Movie, Janr, Reviews, Author

admin.site.register(Movie)
admin.site.register(Janr)
admin.site.register(Reviews)
admin.site.register(Author)
