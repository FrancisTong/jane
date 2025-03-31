# -*- coding: utf-8 -*-

from django.conf import settings
from django.urls import include, path, re_path
from django.contrib.gis import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jane.waveforms.urls')),
    path('', include('jane.documents.urls')),
    path('', include('jane.jane.urls')),
    path('fdsnws/', include('jane.fdsnws.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += staticfiles_urlpatterns()
