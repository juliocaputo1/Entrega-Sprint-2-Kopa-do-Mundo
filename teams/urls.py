from django.urls import path
from .views import TeamCreateList
from .views import TeamUpdateDeleteFilter


urlpatterns = [
    path('teams/', TeamCreateList.as_view()),
    path('teams/<team_id>/', TeamUpdateDeleteFilter.as_view())
]