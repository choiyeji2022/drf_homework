from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from boards.models import Board
from boards.serializers import BoardSerializer, BoardListSerializer, BoardCreateSerializer

class BoardView(APIView):
    def get(self, resquest):
        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = BoardCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetailView(APIView):
    def get(self, resquest, board_id):
        board = get_object_or_404(Board,id=board_id)
        serializer = BoardSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, board_id):
        board = get_object_or_404(Board, id=board_id)
        if request.user == board.user:
            serializer = BoardCreateSerializer(board, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    
    def delete(self, request, board_id):
        board = get_object_or_404(Board, id=board_id)
        if request.user == board.user:
            board.delete()
            return Response("삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)    

