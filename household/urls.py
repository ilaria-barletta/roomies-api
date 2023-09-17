from django.urls import path
from household import views

urlpatterns = [
    path("households/", views.HouseholdList.as_view()),
]
