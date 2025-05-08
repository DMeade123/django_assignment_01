from django.contrib import admin
from .models import Authors, Books, Members, Loans

# Register your models here.

admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Members)
admin.site.register(Loans)


