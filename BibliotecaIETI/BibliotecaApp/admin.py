from django.contrib import admin
from .models import User, ItemType, CatalogItem, Copy, Reservation, Loan, Request, Log

admin.site.register(User)
admin.site.register(ItemType)
admin.site.register(CatalogItem)
admin.site.register(Copy)
admin.site.register(Reservation)
admin.site.register(Loan)
admin.site.register(Request)
admin.site.register(Log)
