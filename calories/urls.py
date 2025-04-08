from django.urls import path
from calories import views

urlpatterns = [
    path('calories/', views.CalorieEntryList.as_view()),
    path('calories/<int:pk>/', views.CalorieEntryDetail.as_view()),

]