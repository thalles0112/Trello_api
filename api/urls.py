
from django.urls import re_path
from django.conf.urls import include
from api import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register('simple-boards', views.BoardViewSet)
router.register('owner-boards', views.OwnerBoardViewSet)
router.register('guest-boards', views.GuestBoardViewSet)
router.register('cards', views.CardViewSet)
router.register('basic-lists', views.ListViewSet)
router.register('users', views.UserViewSet)
router.register('profiles', views.ProfileViewSet)
router.register('comentarios', views.ComentarioViewSet)
router.register('steps', views.StepViewSet)
router.register('simple-checklists', views.CheckListViewset)
router.register('rules', views.RuleViewSet)
router.register('labels', views.LabelViewset) 
router.register('setors', views.SetorViewset)

 
urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path('lists', views.CompleteListViewSet.as_view()),
    re_path('checklist', views.CustomCheckListView.as_view()),
    re_path('rules-by-board', views.RulesByBoardViewset.as_view()),
    re_path('full-board', views.BoardListCardViewset.as_view()),
    re_path('auth/', views.CustomObtainAuthToken.as_view()),
]   