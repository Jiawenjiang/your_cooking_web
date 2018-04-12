"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url

import django.contrib.auth.views


import grumblr.views

urlpatterns = [
    url(r'^$', grumblr.views.home),
    url(r'^global_stream$', grumblr.views.home, name='home'),
    url(r'^register$', grumblr.views.register, name='register'),
    
    url(r'^post', grumblr.views.post, name='post'),
    url(r'^profile/(?P<username>\w+)$', grumblr.views.profile, name='profile'),
    url(r'^photo/(?P<username>\w+)$', grumblr.views.get_profile_photo, name='photo'),
    url(r'^follow/(?P<username>\w+)$', grumblr.views.follow, name='follow'),
    
    url(r'^password_reset_form/(?P<username>\w+)$', grumblr.views.password_reset_form, name='reset_form'),
    url(r'^edit_profile$', grumblr.views.edit_profile, name='edit_profile'),
    url(r'^reset$', grumblr.views.reset_pass, name='reset_pass'),
    url(r'^reset_password$', grumblr.views.reset_password, name='reset_password'),
    url(r'^change_password$', grumblr.views.change_password, name='change_password'),
    url(r'^login$', django.contrib.auth.views.login, {'template_name':'grumblr/login.html'}, name='login'),
    url(r'^logout$', django.contrib.auth.views.logout_then_login, name='logout'),
  
    url(r'^follower_stream$', grumblr.views.follower_stream, name='follower_stream'),
    url(r'^unfollow/(?P<username>\w+)$', grumblr.views.unfollow, name='unfollow'),
    

    url(r'^delete/(?P<id>\d+)$', grumblr.views.delete, name='delete'),

    url(r'^password_reset_confirmation/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', grumblr.views.password_reset_confirmation, name='password_confirm'),
    

    url(r'^get-changes/(?P<time>.+)$', grumblr.views.get_changes),
    url(r'^get-changes/?$', grumblr.views.get_changes),

    url(r'^add-comment/(?P<post_id>\d+)$', grumblr.views.add_comment),
    url(r'^get-comments-changes/(?P<time>.+)/(?P<post_id>\d+)$', grumblr.views.get_comments_changes),
    url(r'^get-changes-follower/(?P<time>.+)$', grumblr.views.get_changes_follower),
    url(r'^get-changes-follower/?$', grumblr.views.get_changes_follower),
    url(r'^get-comments-changes-for-post/(?P<time>.*)/(?P<post_id>\d+)$', grumblr.views.get_comments_changes_for_post),
    url(r'^get-changes-profile/(?P<username>.+)/(?P<time>.+)$', grumblr.views.get_changes_profile),
    url(r'^get-changes-profile/(?P<username>.+)/?$', grumblr.views.get_changes_profile),
]
