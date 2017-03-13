"""energoforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.skipoprosas_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from content.views import skipopros,testimonials
from staticpages.views import index,energotechnology, info,news,newslist
from django.conf.urls.static import static
from django.conf import settings
from energoforum import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^energotechnology/$', energotechnology),
    url(r'^skipopros/$', skipopros),
    url(r'^news/$', newslist),
    url(r'^news/(\.*)/$', news),
    url(r'^testimonials/', testimonials),
    url(r'^info/', info),
    url (r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^', index),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
