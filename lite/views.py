from rest_framework import status
from rest_framework.response import Response

from lite.models import Author
from lite.models import Reader
from lite.serializers import AuthorSerializer
from lite.serializers import ReaderSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView 


class AuthorView(APIView):

    def get(self, request, pk=False):
        paginator = PageNumberPagination()
        if pk:
            try:
                author = Author.objects.get(pk=pk)
            except Author.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = AuthorSerializer(author)
        else:
            author = Author.objects.all()
            result_page = paginator.paginate_queryset(author, request)
            serializer = AuthorSerializer(result_page,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

    def put(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "update successful"
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        operation = author.delete()
        data = {}
        if operation:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete failed"
        return Response(data=data)


    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data['success'] = "successful"
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ReaderView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    pagination_class = PageNumberPagination 