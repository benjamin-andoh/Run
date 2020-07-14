from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# for the class based views
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer


# Generic View
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request, id):
        return self.create(request, id)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


# APIView
class ArticleAPIView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function based API view
@api_view(['GET', 'POST'])
def article_list(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article, many=True)
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
