
from django.shortcuts import render
from .models import News, Author

def index(request):
    latest_news = News.objects.all().order_by("-publication_date")[:10]
    return render(request, 'index.html', {'latest_news': latest_news})

def news_list(request):
    all_news = News.objects.all().order_by('-publication_date')
    return render(request, 'news_list.html', {'all_news': all_news})

def news_detail(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news_detail.html', {'news': news})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})

def author_news(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'author_news.html', {'author': author})

def author_news_list(request, id):
    author = Author.objects.get(id=id)
    news_list = author.news_set.all()
    return render(request, 'author_news_list.html', {'author': author, 'news_list': news_list})