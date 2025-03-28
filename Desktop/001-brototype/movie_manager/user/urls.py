from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    

    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)