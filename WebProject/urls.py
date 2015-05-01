from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    url(r'^signup/$', TemplateView.as_view(template_name='signup.html'), name='signup'),
    url(r'^post/$', TemplateView.as_view(template_name='post.html'), name='post'),
    url(r'^user_profile/$', TemplateView.as_view(template_name='user_profile.html'), name="user_profile"),
    url(r'^users_list/$', TemplateView.as_view(template_name='users_list.html'), name="users_list"),
    url(r'^movie_profile/$', TemplateView.as_view(template_name='movie_profile.html')),
    url(r'^search/$', TemplateView.as_view(template_name='search.html'), name='search'),

)
