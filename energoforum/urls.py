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
from oscar.app import application
from energotechnology.views import energotechnologyAll, energotechnology
from oscar.views import handler403, handler404, handler500
from content.views import skipopros,testimonials, newslist, news, faq
from staticpages.views import index, info, contact
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^energotechnology/$', energotechnologyAll),
    url(r'^energotechnology/(.+)/$', energotechnology),
    url(r'^skipopros/$', skipopros),
    url(r'^news/$', newslist),
    url(r'^contact/$', contact),
    url(r'^faq/$', faq),
    url(r'^news/(\d+)/$', news),
    url(r'^testimonials/', testimonials),
    url(r'^info/$', info),
    url (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^catalog/', include(application.urls)),
    # url(r'^', application.urls),  если  будем испоьзовать приложения
    url(r'^', index),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
