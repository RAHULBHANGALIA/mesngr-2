from django.conf.urls import patterns,include, url
from django.contrib import admin
from rest_framework import routers, viewsets
from prjctapp.models import User,Message
from prjctapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

class UserViewSet(viewsets.ModelViewSet):
    model=User
	
router=routers.DefaultRouter()
router.register(r'path',UserViewSet)

class MessageViewSet(viewsets.ModelViewSet):
    model=Message
	
#router=routers.DefaultRouter()
router.register(r'path1',MessageViewSet)

urlpatterns =[
   url(r'^api/', include(router.urls)),
   url(r'^signin/',views.index),
   url(r'^files/',views.files, name='files'),
   url(r'^profile/',views.signup),
   url(r'^logout/',views.logout),
   url(r'^profile1/',views.userprofile),
   url(r'^message/',views.message),
   url(r'^save/',views.savemessage),
   url(r'^admin/', include(admin.site.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

urlpatterns += staticfiles_urlpatterns()
