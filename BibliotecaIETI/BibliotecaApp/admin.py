from django.contrib import admin
from .models import User, TipusElement, ElementCatalog, Exemplar, Reserva, Prestec, Peticio, Registre

admin.site.register(User)
admin.site.register(TipusElement)
admin.site.register(ElementCatalog)
admin.site.register(Exemplar)
admin.site.register(Reserva)
admin.site.register(Prestec)
admin.site.register(Peticio)
admin.site.register(Registre)
