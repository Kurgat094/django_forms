from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('admin/', admin.site.urls),
     
]
from django.urls import path
from . import views

urlpatterns = [
    path('input', views.save_user_data, name='save_user_data'),
    path('success',views.read_user_data,name="read_user_data"),

]


if settings.DEBUG:
    
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)