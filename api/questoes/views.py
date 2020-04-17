from rest_framework import viewsets

from .models import Questao
from .serializers import QuestaoSerializer


class QuestaoViewSet(viewsets.ModelViewSet):
    serializer_class = QuestaoSerializer

    def get_queryset(self):
      queryset = Questao.objects.all().order_by('projeto_id', 'id')
      if len(self.kwargs) and 'id' in self.kwargs:
          id = self.kwargs['id']
          queryset = queryset.filter(id=id)
      return queryset
