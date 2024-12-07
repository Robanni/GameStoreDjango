from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Game
from .serializers import GameSerializer,GameCardSerializer


class GameBaseDataView(APIView):

    def get_object_by_id(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        game = self.get_object_by_id(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
    

class GameCartListView(APIView):

    def get(self, request, format=None):
        limit = request.query_params.get('limit', None)  

        if limit:
            try:
                limit = int(limit)

                if(limit<=0):
                    return Response({"error": "Limit must be greater tha 0"}, status=status.HTTP_400_BAD_REQUEST)
                
                games = Game.objects.all().order_by('-created_at')[:limit]

            except ValueError:
                return Response({"error": "Limit must be an integer."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            games = Game.objects.all().order_by('-created_at')


        serializer = GameCardSerializer(games, many=True)
        return Response(serializer.data)