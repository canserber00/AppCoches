from django.contrib import admin

# Register your models here.

from .scraper import Coche

admin.site.register(Coche)

