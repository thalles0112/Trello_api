from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.authtoken.models import Token



class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text',
                  'user',
                  'date',
                  'card',
                  'return_user'
                ]

class BoardSerializer(ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class ListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'
        

class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = [  'id',
                    'title',
                    'card_index',
                    'creation_data',
                    'description',
                    'cape',
                    'files',
                    'labels',
                    'checklist',
                    'viewers',
                    'start_data',
                    'finish_data',
                    'reminder',
                    'reminder_date',
                    'clones', 
                    'viewers_details',]


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile # MODELO DO models.py
        fields = '__all__' # vai pegar todos os campos desse modelo

class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile')
        extra_kwargs = {'password':{'write_only':True, 'required': False}}
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data) 
        UserProfile.objects.create(user=user)
        Token.objects.create(user=user)
        return user

class StepSerializer(ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class CheckListSerializer(ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'


class RuleSerializer(ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

class LabelSerializer(ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'


class SetorSerializer(ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'