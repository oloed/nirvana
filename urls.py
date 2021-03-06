from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^$', 'nirvana.pkg.views.welcome'),
    (r'^admin/', include(admin.site.urls)),
    (r'^token/', 'nirvana.pkg.views.api_token'),
    (r'^categories/$', 'nirvana.pkg.views.categories'),
    (r'^category/new/$', 'nirvana.pkg.views.category_new'),
    (r'^category/(?P<slug>[-\w]+)/$', 'nirvana.pkg.views.category'),
    (r'^package/new/$', 'nirvana.pkg.views.package_new'),
    (r'^package/(?P<slug>[-\w]+)/latest/new/$', 'nirvana.pkg.views.variant_new', {'version_slug': None}),
    (r'^package/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/new/$', 'nirvana.pkg.views.variant_new'), # TODO: fix the version regex

    (r'^package/(?P<slug>[-\w]+)/latest/(?P<variant_slug>[-\w]+)/edit/$', 'nirvana.pkg.views.variant_edit', {'version_slug': None}),
    (r'^package/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/(?P<variant_slug>[-\w.]+)/edit/$', 'nirvana.pkg.views.variant_edit'), # TODO: fix the version regex

    (r'^package/(?P<slug>[-\w]+)/new/$', 'nirvana.pkg.views.version_new'),
    (r'^package/(?P<slug>[-\w]+)/edit/$', 'nirvana.pkg.views.package_edit'),
    (r'^package/(?P<slug>[-\w]+)/managers/$', 'nirvana.pkg.views.package_edit_managers'),

    (r'^package/(?P<slug>[-\w]+)/latest/edit/$', 'nirvana.pkg.views.version_edit', {'version_slug': None}),
    (r'^package/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/edit/$', 'nirvana.pkg.views.version_edit'), # TODO: fix the version regex

    (r'^packages/(?P<slug>[-\w]+)/$', 'nirvana.pkg.views.package'),

    (r'^packages/(?P<slug>[-\w]+)/latest/$', 'nirvana.pkg.views.version', {'version_slug': None}),
    (r'^packages/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/$', 'nirvana.pkg.views.version'), # TODO: fix the version regex

    (r'^packages/(?P<slug>[-\w]+)/latest/(?P<variant_slug>[-\w]+)/$', 'nirvana.pkg.views.variant', {'version_slug': None}),
    (r'^packages/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/(?P<variant_slug>[-\w.]+)/$', 'nirvana.pkg.views.variant'), # TODO: fix the version regex

    (r'^packages/(?P<slug>[-\w]+)/latest/(?P<variant_slug>[-\w]+)/(?P<usefile>[-\w.]+)\.use$', 'nirvana.pkg.views.usefile', {'version_slug': None}),
    (r'^packages/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/(?P<variant_slug>[-\w.]+)/(?P<usefile>[-\w.]+)\.use$', 'nirvana.pkg.views.usefile'), # TODO: fix the version regex
    (r'^packages/(?P<slug>[-\w]+)/latest/(?P<variant_slug>[-\w]+)/(?P<checksums>[-\w.]+)\.checksums$', 'nirvana.pkg.views.checksums', {'version_slug': None}),
    (r'^packages/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/(?P<variant_slug>[-\w.]+)/(?P<checksums>[-\w.]+)\.checksums$', 'nirvana.pkg.views.checksums'), # TODO: fix the version regex
    (r'^packages/(?P<slug>[-\w]+)/latest/(?P<variant_slug>[-\w]+)/(?P<checksums_signature>[-\w.]+)\.checksums\.sig$', 'nirvana.pkg.views.checksums_signature', {'version_slug': None}),
    (r'^packages/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/(?P<variant_slug>[-\w.]+)/(?P<checksums_signature>[-\w.]+)\.checksums\.sig$', 'nirvana.pkg.views.checksums_signature'), # TODO: fix the version regex



    (r'^accounts/', include('registration.urls')),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/fred/dev/ooc/nirvana/media'}), # TODO: only for development

    # api
    (r'^api/authorized/$', 'nirvana.pkg.views.api_authorized'),
    (r'^api/submit/$', 'nirvana.pkg.views.api_submit'),
    (r'^api/categories/$', 'nirvana.pkg.views.api_categories'),
    (r'^api/search/$', 'nirvana.pkg.views.api_search'),
    (r'^api/category/(?P<slug>[-\w]+)/$', 'nirvana.pkg.views.api_category'),
    (r'^api/packages/(?P<slug>[-\w]+)/$', 'nirvana.pkg.views.api_package'),
    (r'^api/packages/(?P<slug>[-\w]+)/latest/$', 'nirvana.pkg.views.api_version', {'version_slug': None}),
    (r'^api/packages/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/$', 'nirvana.pkg.views.api_version'),
    (r'^api/packages/(?P<slug>[-\w]+)/latest/(?P<variant_slug>[-\w.]+)/$', 'nirvana.pkg.views.api_variant', {'version_slug': None}),
    (r'^api/packages/(?P<slug>[-\w]+)/(?P<version_slug>[-\w.]+)/(?P<variant_slug>[-\w.]+)/$', 'nirvana.pkg.views.api_variant'),
)
