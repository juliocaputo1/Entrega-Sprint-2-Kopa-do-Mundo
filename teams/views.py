from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.request import Request
from teams.models import Team
from django.forms.models import model_to_dict

class TeamCreateList(APIView):
    def post(self, request: Request):
        team_req = request.data
        team_model = Team.objects.create(**team_req)

        team_dict = model_to_dict(team_model)

        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request: Request):
        teams = Team.objects.all()

        team_list = []

        for team in teams:
            t = model_to_dict(team)
            team_list.append(t)
        
        return Response(team_list)

class TeamUpdateDeleteFilter(APIView):
    def get(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"msg": "team not found"}, status.HTTP_404_NOT_FOUND)
        
        team_list = model_to_dict(team)

        return Response(team_list, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"msg": "team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        team_list = model_to_dict(team)

        return Response(team_list, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int):
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"msg": "team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)