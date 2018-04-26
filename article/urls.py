from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.homepage, name='index'),
    url(r'^register/login$', views.user_login, name='user_login'),
    url(r'^index/$', views.user_logout, name='user_logout'),
    url(r'^register/post$', views.post_email,name='post_email'),
    url(r'^register/register$', views.register, name='user_register'),
    url(r'^emailfind/login', views.emailLogin,name='email_login'),
    url(r'^emailfind/post', views.post_email_login,name='login_post_email'),
    url(r'^newarticle/', views.publishArticle, name='new_article'),
    url(r'^show_article/(?P<article_id>[0-9]+)/$', views.article, name='show_article'),
    url(r'^article_list/(?P<category_id>[0-9]+)/$', views.category, name='article_list'),
    url(r'^show_article/collect$', views.collected, name='collected'),
    url(r'^myposts', views.getmyarticle, name='myarticle'),
    url(r'^mycollects', views.getmycollect, name='mycollect'),
    url(r'^myinfo', views.myinfo, name='myinfomation'),
    url(r'^download/(?P<article_id>[0-9]+)/$', views.downloadfile, name='download'),
    url(r'^show_article/subcom', views.submit_comment, name='submitcomment'),
    url(r'^show_article/subreply', views.submit_reply, name='submitreply'),
    url(r'search', views.search, name='search'),
    url(r'^resetpwd', views.resetpwd, name='reset_pwd'),
]