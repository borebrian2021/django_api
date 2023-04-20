from django.contrib import admin
from .models import TestModel
from .models import ModelX
from .models import ModelY

admin.site.register((TestModel,ModelX,ModelY))

