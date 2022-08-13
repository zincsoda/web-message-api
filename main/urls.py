from django.contrib import admin
from django.urls import include, path
from main import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/test', views.test),
    path('', views.test),
    path('power_on', views.power_on),
    path('power_off', views.power_off),
    path('message/<str:message_string>/', views.message, name='message'),
    # url(r'^(?P<uuid>[^/]+)/$', views.render_message),
    # path('^api/messages', views.MessageList.as_view(), name='message-list'),
    # path('^api/messages/(?P<pk>[0-9]+)', views.MessageDetail.as_view(), name='message-detail'),    
]