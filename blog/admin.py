from django.contrib import admin
from .models import Post

''' É necessário registrar em admin.py a classe definida no model para que ela seja iniciada na página do Administrador'''

# admin.site.register(Post)

''' No entanto, podemos customizar como o model Post será mostrado no na página do Administrador '''

@admin.register(Post) # Igual 'admin.site.register(Post)'
class PostAdmin(admin.ModelAdmin):
    ''' list_display é um atributo para mostrar na página apenas os atributos definidos nesta ordem'''
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    '''Adiciona a barra lateral de filtragem com os campos selecionados'''
    list_filter = ('status', 'created', 'publish', 'author')

    '''Adiciona o search_field pesquisando pelos campos selecionados'''
    search_fields = ('title', 'body')
    
    '''Automaticamente popular os campo de slug'''
    prepopulated_fields = {'slug': ('title',)}

    '''Neste trecho estamos salvando na tabela Post o id de Autor'''
    raw_id_fields = ('author',)

    '''Habilita uma Hierarquia pela data da publicação abaixo do campo de pesquisa'''
    date_hierarchy = 'publish'

    '''Ordena os registros pelas colunas Status Status e Publish'''
    ordering = ('status', 'publish')