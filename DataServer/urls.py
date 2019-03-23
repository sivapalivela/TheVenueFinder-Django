from django.urls import path,include
from DataServer import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('apiget/', views.getDataList.as_view()),
    path('apipost/<str:id>',views.getData_expt_get.as_view()),
    # path('mongo_auth/', include('mongo_auth.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)