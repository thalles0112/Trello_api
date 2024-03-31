from django.shortcuts import render
from django.contrib.auth.models import Permission
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import status

# Create your views here.

def get_queryset(self):
    # funcao exemplo de pegar permisao do usuario    
    #print('user ->', self.request.user)
    #content = self.request.user.get_all_permissions() 
    #has_permission = 'api.view_workspace' in content # => return True or False

    #serializer = self.serializer_class

    #userId = self.request.query_params.get('user_profile')
    #           model obj                        ?params
    #queryset = WorkSpace.objects.filter(viewers=userId)
    pass
        
  
class ComentarioViewSet(ModelViewSet):
    serializer_class = ComentarioSerializer
    
    queryset = Comment.objects.all()
    def get_queryset(self):
        cardId = self.request.query_params.get('card')
        queryset = Comment.objects.filter(card=cardId).order_by('-id')
        return queryset


class BoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()



class OwnerBoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer
    #authentication_classes = [TokenAuthentication,]
    #permission_classes = [IsAuthenticated,]
    queryset = Board.objects.all()
    def get_queryset(self):
        userprofile = self.request.query_params.get('profile_id')
        queryset = Board.objects.all().filter(owner=userprofile)
        return queryset

class GuestBoardViewSet(ModelViewSet):
    serializer_class = BoardSerializer
    #authentication_classes = [TokenAuthentication,]
    #permission_classes = [IsAuthenticated,]
    queryset = Board.objects.all()
    def get_queryset(self):
        userprofile = self.request.query_params.get('profile_id')
        queryset = Board.objects.all().filter(viewers=userprofile)
        return queryset
        

class CompleteListViewSet(APIView):
    serializer_class = CardSerializer
    queryset = List.objects.all()
    
    def get(self, request, format=None):
        list_id = str((self.request.query_params.get('list_id')))
         
        cards = []
        followers = []
        if list_id == 'None' or list_id == '':
            queryset = []
        else:
            queryset = List.objects.all().filter(id__in=list_id.split(',')) 
        newquery = []
        for q in queryset:
            for card in q.cards.all().order_by('card_index'):
                cards.append({'id': card.id, 'title': card.title, 'card_index': card.card_index})
            
            for follower in q.followers.all():
                followers.append({'id':follower.id, 'name': follower.name})

            newquery.append({'id':q.id, 'title':q.title, 'creation_data': q.creation_data, 'cards':cards[:], 'followers': followers[:]})
            cards.clear()
            followers.clear()
        return Response(newquery)

class StepViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    serializer_class = StepSerializer
    queryset = Step.objects.all()

class CheckListViewset(ModelViewSet):
    authentication_classes = [TokenAuthentication,]
    serializer_class = CheckListSerializer
    queryset = CheckList.objects.all() 


class CustomCheckListView(APIView):
    authentication_classes = [TokenAuthentication, ] 
    def get(self, request, format=None):
        queryset = {}
        checklist = {}
        steps = []
        try:
            checklist = CheckList.objects.get(id=int(request.query_params.get('checklist-id')))
        except:
            checklist = {}
        else:
            for step in checklist.steps.all():
                steps.append({'id':step.id, 'title':step.title, 'done':step.done })
            
            queryset = {'id':checklist.id, 'title': checklist.title, 'steps':steps}
        
        


        return Response(queryset) 


class ListViewSet(ModelViewSet):
    serializer_class = ListSerializer
    queryset = List.objects.all()


class LabelViewset(ModelViewSet):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()

   
class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    
    
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class ProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        userSerializer = UserSerializer(user, many=False)

        return Response({'token': token.key, 'user': userSerializer.data})


class RuleViewSet(ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer



class SetorViewset(ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer



class RulesByBoardViewset(APIView):
    def get(self, request, format=None):
        rules_list  =[]
        try:
            boardId = int(request.query_params.get('boardId'))
            board = Board.objects.get(id=boardId)
            for rule in board.rules.all():
                rules_list.append({'trigger':rule.trigger, 'actions': rule.actions, 'active': rule.active, 'id': rule.id})
            

        except Exception as e:
            print(e)
            return Response([])
        
        else:
            
            return Response(rules_list)


class BoardListCardViewset(APIView):
    def get(self, request, format=None):
        user = 1#self.request.query_params.get('profile_id')
        boards = []
        
        tmp_listList = []
        tmp_cardList = []

        guestBoards = Board.objects.filter(viewers=user)
        ownerBoards = Board.objects.filter(owner=user)
        for Gobj, Oobj in zip(guestBoards, ownerBoards):
            boards.append(BoardSerializer(Gobj).data)
            boards.append(BoardSerializer(Oobj).data)

        for board in boards:
            for list in board['lists']:
                listObj = List.objects.get(id=list)
                serializedList = ListSerializer(listObj).data

                
                for card in serializedList['cards']:
                    cardObj = Card.objects.get(id=card)
                    serializedCard = CardSerializer(cardObj).data
                    tmp_cardList.append(serializedCard)
                    serializedList['cards'].append(serializedCard)
                
                tmp_listList.append(serializedList)
                    
            board['lists'] = tmp_listList[:]

            tmp_listList.clear()
            



        
        return Response(boards)