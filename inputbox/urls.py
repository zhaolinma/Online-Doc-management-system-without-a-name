from django.conf.urls import url
from . import views
app_name='article'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^login/$', views.login_user ,name = 'login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.User_Form_View.as_view(),name='register'),
    url(r'^(?P<article_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^article/add/$', views.Article_Create_View.as_view(),name='article-add'),
    url(r'^article/(?P<article_id>[0-9]+)/edit/$', views.Article_Edit_View.as_view(),name='article-edit'),
    url(r'^article/(?P<article_id>[0-9]+)/delete/$', views.Article_Delete_View.as_view(), name='article-delete'),
    url(r'^article/(?P<article_id>[0-9]+)/add_part/$',views.Part_Create_View.as_view(),name='part-add'),
    url(r'^article/(?P<article_id>[0-9]+)/(?P<part_id>[0-9]+)/part_edit/$',views.Part_Edit_View.as_view(),name='part-edit'),
    url(r'^article/(?P<article_id>[0-9]+)/(?P<part_id>[0-9]+)/part_delete/$',views.Part_Delete_View.as_view(),name='part-delete'),
]
