from django.shortcuts import render, redirect
from .models import Article


def main_page(request):
    return render(request, 'main/index_main.html')


def add_news_page(request):
    if request.method == 'POST':
        form_values = request.POST.getlist('news')
        Article.objects.create(title=form_values[0],
                               announce=form_values[1],
                               full_text=form_values[2],
                               date=form_values[3]
                               )
    return render(request, 'main/index_add_news.html')


def news_page(request):
    data = Article.objects.all()
    return render(request, 'main/index_news.html', {'data': data})


def search_page(request):
    result = []
    if request.method == 'POST':
        key_word = request.POST['search']
        titles = [title for dict_ in Article.objects.values('title') for title in dict_.values()]
        for i in titles:
            if key_word in i.lower() and key_word:
                result.append(Article.objects.get(title=i))
    return render(request, 'main/index_search.html', {'data': result})


def read_page(request):
    if request.method == 'GET':
        data = Article.objects.get(id=request.GET['read'])
    return render(request, 'main/index_news_read.html', {'data': data})
