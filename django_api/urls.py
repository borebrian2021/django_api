
from django.contrib import admin
from django.urls import path
from test_app.views import SimpleGenerics,SimpleGenericsUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    #GET
    path('simple-generics',SimpleGenerics.as_view()),
    #UPDATE OR PATCH
    path('simple-generics/<int:id>',SimpleGenericsUpdate.as_view())
    ]
