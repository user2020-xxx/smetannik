from django.contrib import admin
from .models import ReferencesModel, GroupReferencesModel
# Register your models here.


admin.site.register(ReferencesModel)
admin.site.register(GroupReferencesModel)