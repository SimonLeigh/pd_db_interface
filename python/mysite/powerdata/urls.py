from django.conf.urls import patterns, url

from powerdata import views

urlpatterns = patterns('',
    # example /powerdata/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # example /powerdata/$unix_epoch (2dp)
    url(r'^(?P<pk>\d+(\.\d{1,2})+)/$', views.DetailView.as_view(), name='detail'),
)
