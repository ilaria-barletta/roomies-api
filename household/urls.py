from django.urls import path
from household import views

urlpatterns = [
    path("households/", views.HouseholdList.as_view()),
    path("households/<int:pk>/", views.HouseholdDetail.as_view()),
    path("households/<int:pk>/members", views.HouseholdMembersList.as_view()),
    path(
        "households/<int:household_pk>/members/<int:pk>",
        views.HouseholdMembersDetail.as_view(),
    ),
]
