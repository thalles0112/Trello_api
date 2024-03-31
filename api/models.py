from django.db import models
from django.contrib.auth.models import User


SHORT_TEXT = 32
MEDIUM_TEXT = 256
LONG_TEXT = 2048
LONGER_TEXT = 10000

# Create your models here.


class Setor(models.Model):
    title = models.CharField(max_length=SHORT_TEXT)
    picture = models.CharField(max_length=MEDIUM_TEXT, blank=True)
    
    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=MEDIUM_TEXT)
    picture = models.CharField(max_length=MEDIUM_TEXT, null=True, blank=True)
    setor = models.ManyToManyField(Setor)
    def __str__(self): 
        return self.name

class Label(models.Model):
    color = models.CharField(max_length=SHORT_TEXT)
    title = models.CharField(max_length=SHORT_TEXT, null=True)
    def __str__(self): 
        return f'{self.title} - `{self.color}'

class Change(models.Model):
    who = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    what = models.CharField(max_length=MEDIUM_TEXT)

class Step(models.Model):
    title = models.CharField(max_length=MEDIUM_TEXT)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class CheckList(models.Model):
    title = models.CharField(max_length=SHORT_TEXT)
    steps = models.ManyToManyField(Step, blank=True)
    def __str__(self):
        return self.title

class File(models.Model):
    title = models.CharField(max_length=MEDIUM_TEXT, null=True)
    url = models.CharField(max_length=MEDIUM_TEXT)
    def __str__(self):
        return f'{self.url} - {self.title}'

class Rule(models.Model):
    trigger = models.CharField(max_length=LONGER_TEXT)
    actions = models.CharField(max_length=LONGER_TEXT)
    active = models.BooleanField(default=False)


class Card(models.Model):
    title = models.CharField(max_length=512)
    card_index = models.IntegerField(verbose_name='card-index', blank=True, null=True)
    creation_data = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=LONG_TEXT, null=True)
    cape = models.CharField(max_length=MEDIUM_TEXT, null=True)
    files = models.ManyToManyField(File, blank=True)
    labels = models.ManyToManyField(Label, blank=True)
    checklist = models.ForeignKey(CheckList, null=True, on_delete=models.SET_NULL, blank=True )
    viewers = models.ManyToManyField(UserProfile, blank=True)
    start_data = models.DateTimeField(null=True)
    finish_data = models.DateTimeField(null=True)
    reminder = models.BooleanField(default=False)
    reminder_date = models.DateTimeField(null=True)
    clones = models.ManyToManyField('self', blank=True)
    
    
    def viewers_details(self):
        viewer_list = []
        for viewer in self.viewers.all():
            viewer_list.append({'name':viewer.name, 'id':viewer.id})
        return viewer_list

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=LONG_TEXT)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    def return_user(self):
        return self.user.name 
    def __str__(self):
        return f'{self.text} - {self.user.name}'

class List(models.Model):
    title = models.CharField(max_length=MEDIUM_TEXT, null=True)
    creation_data = models.DateTimeField(auto_now_add=True)
    cards = models.ManyToManyField(Card, blank=True)
    followers = models.ManyToManyField(UserProfile, blank=True)
    def __str__(self):
        return self.title

    

class Board(models.Model):
    title = models.CharField(max_length=MEDIUM_TEXT, null=False)
    creation_data = models.DateTimeField(auto_now_add=True)
    lists = models.ManyToManyField(List, blank=True)
    viewers = models.ManyToManyField(UserProfile, blank=True, related_name='viewer')
    owner = models.ManyToManyField(UserProfile, related_name='board_owner', blank=True)
    background = models.CharField(max_length=MEDIUM_TEXT, null=True, blank=True)
    rules = models.ManyToManyField(Rule, blank=True)

    def __str__(self):
        return self.title


