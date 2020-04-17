from django.contrib import admin
from django.urls import include, path
from questoes import views as questoes_views

from rest_framework import routers
from users import views as user_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path(
        'questoes/',
        view=questoes_views.QuestaoViewSet.as_view(
            {'get': 'list'}),
        name='questoes'
    ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
