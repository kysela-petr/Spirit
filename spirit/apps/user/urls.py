# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse_lazy

from . import views


urlpatterns = [
    url(r'^login/$', views.custom_login, {'template_name': 'spirit/user/login.html'}, name='user-login'),
    url(r'^logout/$', views.custom_logout, {'next_page': '/', }, name='user-logout'),

    url(r'^register/$', views.register, name='user-register'),
    url(r'^resend-activation/$', views.resend_activation_email, name='resend-activation'),

    url(r'^activation/(?P<pk>\d+)/(?P<token>[0-9A-Za-z_\-\.]+)/$', views.registration_activation,
        name='registration-activation'),
    url(r'^email-change/(?P<token>[0-9A-Za-z_\-\.]+)/$', views.email_change_confirm, name='email-change-confirm'),

    url(r'^password-reset/$', views.custom_reset_password,
        {'template_name': 'spirit/user/password_reset_form.html',
         'email_template_name': 'spirit/user/password_reset_email.html',
         'subject_template_name': 'spirit/user/password_reset_subject.txt',
         'post_reset_redirect': reverse_lazy('spirit:password-reset-done')},
        name='password-reset'),

    url(r'^password-reset/done/$', password_reset_done, {'template_name': 'spirit/user/password_reset_done.html', },
        name='password-reset-done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[\w\-]+)/$', password_reset_confirm,
        {'template_name': 'spirit/user/password_reset_confirm.html',
         'post_reset_redirect': reverse_lazy('spirit:password-reset-complete')},
        name='password-reset-confirm'),

    url(r'^reset/done/$', password_reset_complete, {'template_name': 'spirit/user/password_reset_complete.html', },
        name='password-reset-complete'),

    url(r'^$', views.profile_update, name='profile-update'),
    url(r'^password-change/$', views.profile_password_change, name='profile-password-change'),
    url(r'^email-change/$', views.profile_email_change, name='profile-email-change'),

    url(r'^(?P<pk>\d+)/$', views.profile_comments, kwargs={'slug': "", }, name='profile-detail'),
    url(r'^(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.profile_comments, name='profile-detail'),

    url(r'^topics/(?P<pk>\d+)/$', views.profile_topics, kwargs={'slug': "", }, name='profile-topics'),
    url(r'^topics/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.profile_topics, name='profile-topics'),

    url(r'^likes/(?P<pk>\d+)/$', views.profile_likes, kwargs={'slug': "", }, name='profile-likes'),
    url(r'^likes/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.profile_likes, name='profile-likes'),

    url(r'^menu/$', views.menu, name='user-menu'),
]
