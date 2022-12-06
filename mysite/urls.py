from django.contrib import admin
from django.urls import path,include
from brown.views import *
from django.conf import settings
from django.templatetags.static import static
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brown/',include('brown.urls')),
    path('blog/',include('blog.urls')),
    path('post/',include('post.urls')),
    path('product/',include('product.urls')),
    path('ajx/',include('ajx.urls')),
    path('sign/',include('sign.urls')),
    path('inheritApp/',include('inheritApp.urls')),
    path('middle/',include('middle.urls')),
    path('authh/',include('authh.urls')),
    path('', include('django.contrib.auth.urls'))
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)