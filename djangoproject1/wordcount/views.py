from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word = len(words)
    dic = {}
    for a in words:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
        
    return render(request, 'result.html',{'full':text, 'words':word, 'dictionary': dic.items()})