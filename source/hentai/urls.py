from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from hentai import views

urlpatterns = [
    path('', views.SeriesSerializerView.as_view()),
    path('series/<int:pk>/', views.IdSeriesDetailSerializerView.as_view()),
    path('series/<str:name>/', views.NameSeriesDetailSerializerView.as_view()),
    path('series/<str:name>/<int:pk>/', views.VideoSeriesSerializerView.as_view()),
    path('video/<int:pk>/', views.VideoDetailSerializerView.as_view()), # Optional functionality
    path('tag/<str:tags>/', views.AnyTagsSerializerView.as_view()),
    path('tag/any/<str:tags>/', views.AnyTagsSerializerView.as_view()),
    path('tag/all/<str:tags>/', views.AllTagsSerializerView.as_view()),
]

# All the routing for the videos