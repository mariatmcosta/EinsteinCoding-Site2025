from django.shortcuts import render, get_object_or_404
from .models import News


def home(request):
    featured_news = News.objects.filter(is_featured=True).order_by('-created_at')
    latest_news = News.objects.filter(is_featured=False).order_by('-created_at')[:4]

    return render(request, 'home.html', {
        'featured_news': featured_news,
        'latest_news': latest_news,
    })


def news_detail(request, id):
    news = get_object_or_404(News, id=id)

    return render(request, 'news_detail.html', {
        'news': news
    })

def codigo_social(request):
    return render(request, 'codigo_social.html')

def gestao(request):
    return render(request, "gestao.html")