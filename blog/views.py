from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
# Create your views here.

def post_list(request):

    '''Adicionando paginação'''
    object_list = Post.published.all()
    paginator = Paginator(object_list,3) # Define 3 posts por página
    page = request.GET.get('page') # retorna qual é a page atual

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        '''Se a página não for inteiro retorna página 1'''
        posts = paginator.page(1)   
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                'blog/post/list.html',
                {'posts': posts})

def post_detail(request, year, month, day, post):
    ''' 
    A função requisita do banco o objeto cadastrado a partir dos campos year, month, day, post 
    '''
    post = get_object_or_404(Post, slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)

    return render(request,
                'blog/post/detail.html',
                {'post': post})