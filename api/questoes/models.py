from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

upload_storage = FileSystemStorage(location=settings.UPLOAD_IMAGE_DIR)


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class Questao(models.Model):
    projeto_id = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(storage=upload_storage)
    descricao = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

class Alternativa(models.Model):
    questao_id = models.ForeignKey(Questao, related_name='alternativas', on_delete=models.CASCADE)
    descricao = models.TextField(max_length=100)