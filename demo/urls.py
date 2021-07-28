from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),
    path('first', views.first),

]