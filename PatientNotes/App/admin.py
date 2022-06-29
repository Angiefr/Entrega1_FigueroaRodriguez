from django.contrib import admin

from .models import Medicamento, Tratamiento, Doctor
# Register your models here.

admin.site.register(Medicamento)
admin.site.register(Tratamiento)
admin.site.register(Doctor)