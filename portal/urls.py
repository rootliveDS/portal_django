from django.urls import path
from .views import StartPage, PostPage, UserPage, create
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', StartPage, name='start'),
    path('post', PostPage.as_view(), name='post'),
    path('123/', UserPage.as_view(), name='user.list'),
    path('test/', create, name='create'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# <str:username>