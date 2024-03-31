from django.contrib import admin
from django.contrib.admin import register
from .models import *

# Register your models here.
@register(UserProfile) 
class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'picture', 'setor')
    list_display = ['name', 'id']



@register(Card) 
class CardAdmin(admin.ModelAdmin):
    fields = ('title', 'card_index', 'checklist')
    list_display = ['id',]

@register(List) 
class ListAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ['id',] 

@register(Board)
class BoardAdmin(admin.ModelAdmin):
    fields = ('title', 'lists', 'owner', 'viewers')
    list_display = ('title', 'id')

@register(Setor)
class SetorAdmin(admin.ModelAdmin):
    fields = ('title', 'picture')
    list_display = ('title', 'id')

@register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    fields = ('title', 'steps')
    list_display = ('title', 'id')

@register(Step)
class StepAdmin(admin.ModelAdmin):
    fields = ('title', 'done')
    list_display = ('title', 'id', 'done')


@register(Rule)
class RuleAdmin(admin.ModelAdmin):
    fields = ('trigger', 'actions')
    list_display = ('trigger', 'actions', 'active')
 
@register(Label)
class LabelAdmi(admin.ModelAdmin):
    fields = ('title', 'color')
    list_display = ('title', 'color')