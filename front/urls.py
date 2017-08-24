from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view()),
	url(r'company/(?P<slug>[0-9A-Za-z-_.//]+)/$', views.CompanyDetailView.as_view(), name='company-detail')
]
