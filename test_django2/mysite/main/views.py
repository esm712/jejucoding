from django.shortcuts import render
from .models import Post


def index(request):
    postAll = Post.objects.all() # 전체 게시물 들어감
    return render(request, 'main/index.html', {'postAll':postAll}) # 사용자의 질의와 함께 렌더링

def mentor(request):

    return render(request, 'main/mentor.html')

def mentee(request):

    return render(request, 'main/mentee.html')

def board(request):

    return render(request, 'main/board.html')

def about(request):

    return render(request, 'main/about.html')

def result(request):

    return render(request, 'main/result.html')

def recommend(request):

    return render(request, 'main/recommend.html')

def comment(request):

    return render(request, 'main/comment.html')
