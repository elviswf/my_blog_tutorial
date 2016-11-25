# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from article import views as article_views
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', article_views.home, name='home'),
    url(r'^(?P<id>\d+)/$', article_views.detail, name='detail'),
    url(r'^archives/$', article_views.archives, name='archives'),
    url(r'^aboutme/$', article_views.about_me, name='about_me'),
    url(r'^tag/(?P<tag>\w+)/$', article_views.search_tag, name='search_tag'),
    url(r'^search/$', article_views.blog_search, name='search'),
    url(r'^feed/$', article_views.RSSFeed(), name="RSS"),
]

"""
修改下 index() 视图， 让它显示系统中最新发布的 5 个调查问题，以逗号分割并按发布日期排序：:

from django.http import HttpResponse

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)
"""
