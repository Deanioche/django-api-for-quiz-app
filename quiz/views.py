from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

# 그냥 hello world 출력하는 페이지 /quiz/hello/
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

# 주어진 개수만큼 랜덤한 퀴즈를 반환하는 API
# /quiz?id:
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    # many=True 옵션을 넣으면 다수의 데이터에 대해서도 직렬화가 진행된다.
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)