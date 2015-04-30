from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^signup/$', TemplateView.as_view(template_name='signup.html'), name='signup'),
    url(r'^user_profile/$', TemplateView.as_view(template_name='user_profile.html')),
    url(r'^movie_profile/$', TemplateView.as_view(template_name='movie_profile.html')),
    url(r'^search/$', TemplateView.as_view(template_name='search.html')),

)
