from django.conf.urls import patterns, url

from powerdata import views

urlpatterns = patterns('',
    # example /powerdata/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # example /powerdata/$unix_epoch (2dp)
    url(r'^(?P<pk>\d+(\.\d{1,2})+)/$', views.DetailView.as_view(), name='detail'),
    # latest records
    url(r'^latest/(?P<n_records>\d+)$', views.latest, name='latest'),
    url(r'^latest/$', views.latest, name='latest'),
    # charts
    url(r'^latest_chart/$', views.latest_chart, name='latest_chart'),
    url(r'^latest_chart/(?P<hours>\d+)$', views.latest_chart, name='latest_chart_with_hrs'),
    url(r'^livechart/$', views.livechart, name='livechart'),
    url(r'^livechart/(?P<last_minutes>\d+)$', views.livechart, name='livechart_with_mins'),
)
