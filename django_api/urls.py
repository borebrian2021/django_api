
from django.contrib import admin
from django.urls import path
from test_app.views import SimpleGenerics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple-generics',SimpleGenerics.as_view())
    ]
