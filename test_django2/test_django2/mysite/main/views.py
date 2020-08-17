from django.shortcuts import render
from .models import Post


def index(request):
    postAll = Post.objects.all() # 전체 개시물 들어감 
    return render(request, 'main/index.html', {'postAll':postAll}) # 사용자의 질의와 함께 렌더링 
