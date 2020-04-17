from .models import Questao, Alternativa
from rest_framework import serializers


class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = ['descricao', 'questao_id']


class QuestaoSerializer(serializers.ModelSerializer):
    alternativas = AlternativaSerializer(read_only=True, many=True)

    class Meta:
        model = Questao
        fields = ['titulo', 'imagem', 'descricao', 'alternativas']
