from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django import forms


admin.site.register(UnitIzm)
admin.site.register(Companies)


