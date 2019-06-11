from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_list.sort()

    return render(request, 'wordcount/count.html', {'list' : word_list})