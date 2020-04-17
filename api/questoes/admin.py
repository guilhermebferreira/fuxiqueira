from django.contrib import admin
from .models import Projeto, Questao, Alternativa

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    fields = ('titulo',)
    pass

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    fields = ('projeto_id', 'titulo', 'imagem', 'descricao',)
    pass

@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    fields = ('questao_id', 'descricao',)
    pass
