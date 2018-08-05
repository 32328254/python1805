from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',view=views.index,name="index"),
    url(r'^(?P<question_id>[0-9]+/$)',view=views.detail,name="detail"),
    url(r'^(?P<question_id>[0-9]+/vote/$)', view=views.vote, name="vote"),
    url(r'^(?P<question_id>[0-9]+/result/$)', view=views.result, name="result"),
    url(r'^(?P<question_id>[0-9]+/details/$)', view=views.detail, name="result")
]
