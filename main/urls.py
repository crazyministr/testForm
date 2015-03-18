from django.conf.urls import patterns, url


urlpatterns = patterns(
    'main.views',
    url(r'^$', 'main', name='main-page'),
)
