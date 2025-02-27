from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('profiles/weights/', views.WeightList.as_view()),
    path('profiles/calories/', views.CalorieEntryList.as_view()),

]