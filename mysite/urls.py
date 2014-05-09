from django.conf.urls.defaults import patterns, include, url
from mysite.views import home,, current_datetime, hours_ahead
		
urlpatterns = patterns('',
	url(r'^home$', home),
	url(r'^home/login/$' , login),
	url(r'^home/login/newArticle/$', new_article),
        url(r'^home/login/articleList/$', article_list),
	url(r'^home/login/articleList/modifArticle/$', modif_art),
	url(r'^home/register/$', register),
	url(r'^home/reset/$', reset),
)
