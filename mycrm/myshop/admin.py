from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django import forms


admin.site.register(UnitIzm)
admin.site.register(Companies)
admin.site.register(Partners)
admin.site.register(Orders)
admin.site.register(Goods)
admin.site.register(Banks)
admin.site.register(BankAccount)
