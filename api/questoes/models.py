from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    created = models.DateTimeField()

class Questao(models.Model):
    projeto_id = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="**/**upload/images/")
    descricao = models.TextField(max_length=500)
    created = models.DateTimeField()
    last_updated = models.DateTimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

class Alternativa(models.Model):
    questao_id = models.ForeignKey(Questao, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=100)