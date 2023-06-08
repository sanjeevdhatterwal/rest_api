from django.contrib import admin
from api import models
from genericapi import models as genericmodel
# Register your models here.
admin.site.register([
    models.Tag,
    models.Article,
    genericmodel.Tag,
    genericmodel.Article
])