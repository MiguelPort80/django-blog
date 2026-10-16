from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm


# Renderiza o index.html
def blog_index(request): 
    # Pega todos os posts e organiza por data, no caso usamos o '-' para o django pegar do maior valor até o menor
    posts = Post.objects.all().order_by("-created_on")
    # Criamos um dictionary e colocamos nossos posts para ser renderizado no template
    context = {
            "posts" : posts,
    }
    # enviamos e renderizamos isso no index.html
    return render(request, "blog/index.html", context)


def blog_category(request, category): 
    posts = Post.objects.filter(
            categories__name__contains=category
    ).order_by("-created_on")


    context = { 
               "category" : category,
               "posts": posts,
    }

    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    #Cria uma instancia de formulario
    form = CommentForm()
    #Verifica se a requisição é do tipo post
    if request.method == "POST":
        #Atualiza o form com os dados do post
        form = CommentForm(request.POST)
        #Verifica se o usuário preencheu o formulário corretamente
        if form.is_valid():
            #Cria uma nova instancia de comentário
            comment = Comment(
                    #Limpa os campos para evitar vulnerabilidades
                    author=form.cleaned_data["author"],
                    body=form.cleaned_data["body"],
                    post=post,
                )
            #Salva o comentário
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
            "post": post,
            "comments": comments,
            "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)
