from django.conf.urls import url

from . import views

urlpatterns = [
    # /getvid/
    url(r'^$', views.index, name='index'),
    # /getvid/udemy/
    url(r'^udemy/$', views.udemy, name='udemy'),
    # /getvid/lynda/
    url(r'^lynda/$', views.lynda, name='lynda'),
]