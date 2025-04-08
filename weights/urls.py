from django.urls import path
from weights import views


urlpatterns = [
    path('weights/', views.WeightEntryList.as_view()),
    path('weights/<int:pk>/', views.WeightEntryDetail.as_view()),
]