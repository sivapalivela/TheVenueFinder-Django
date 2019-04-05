from django.urls import path,include
from DataServer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/getjson/', views.GetJsonData.as_view()),
    path('api/post/<str:id>',views.GetDatabyId.as_view()),
    path('api/get/requestedjson',views.GetFilterList.as_view()),
    path('api/ratingsjson',views.GetDatabyRating.as_view()),
    path('api/votesjson',views.GetDatabyVotes.as_view()),
    path('api/avgcostjson',views.GetDatabyAvgCost.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)