from django.contrib import admin
from .models import TestModel
from .models import ModelX

admin.site.register((TestModel,ModelX))

