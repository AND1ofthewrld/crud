import jwt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel, Article
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'roles/index.html')
def check_collection(request):
    if request.method == 'POST':
        username_input = request.POST.get('username', '')
        password_input = request.POST.get('password', '')
      
        if MyModel.objects.filter(username__iexact=username_input, passsword__iexact=password_input).exists():
            # Пользователь найден, создаем JWT токен
            my_model_instance = MyModel.objects.get(username__iexact=username_input)
            payload = {
                'user_id': my_model_instance.id,
                'username': my_model_instance.username,
                'role': my_model_instance.role
            }
            session_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            my_model_instance.session_token = session_token
            my_model_instance.save()

            response = redirect('article_page')
            response.set_cookie('session_token', session_token)
            response.set_cookie('role', my_model_instance.role)
            response.set_cookie('author', my_model_instance.username)
            return response
            
        else:
            return HttpResponse('Permission denied')
    return render(request, 'roles/auth.html')
def article_page(request):
    try:
        
        role = request.COOKIES.get('role', '')
       
    except MyModel.DoesNotExist:
        print(f"Пользователь не найден.")
    
    articles = Article.objects.all()
    print(articles)
    if role == "admin":
        can_edit = 1
    elif role == "user":
        can_edit = 2
    else:
        can_edit = 3

    return render(request, 'roles/articles.html', {'articles': articles, 'can_edit': can_edit})


def article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        
        Article.objects.create(title=title, content=content)
        
        return redirect('article_page')

    return render(request, 'roles/article_create.html')


def article_delete(request):

    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('article_page')

    articles = Article.objects.all()
    return render(request, 'roles/article_delete.html', {'articles': articles})



from .forms import ArticleForm

def article_edit(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_page')
    else:
        # Если запрос GET, отобразить форму для редактирования статьи
        form = ArticleForm(instance=article)

    return render(request, 'roles/article_edit.html', {'form': form, 'article': article})