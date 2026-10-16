from django.db import models

# Create your models here.



class Category(models.Model):
    # charfield é auto explicativo, estou importando da classe models do django o ORM
    name = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model): 
    title = models.CharField(max_length=255)
    body = models.TextField()
    #o parâmetro auto_now_add faz que cada vez que um post seja criado ele atribui uma data e hora
    created_on = models.DateTimeField(auto_now_add=True)
    #o parâmentro auto_now faz com que cada vez que um post seja alterado ele atribui uma data e hora
    last_modified = models.DateTimeField(auto_now=True)
    #configura um campo para um relacionamento Many To Many (vários posts tem várias categorias e vice versa)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #Cria uma chave estrangeira para atribuir vários comentários a um post, e o on_delete faz com que caso o comentário seja deletado as respostas são deletadas junto
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

