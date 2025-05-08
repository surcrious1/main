from django.shortcuts import render
from django.http import JsonResponse
from news.models import News

def latest_news(request):
    news_list = News.objects.order_by('-crawled_at')[:20]
    data = [{
        'title': n.title,
        'link': n.link,
        'media': n.media,
        'content': n.content,
    } for n in news_list]
    return JsonResponse(data, safe=False)