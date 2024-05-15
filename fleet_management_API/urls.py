from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('fleet_management_app.urls'), name='fleet_management_app.urls')
]


