# Generated by Django 4.1.4 on 2024-03-30 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('card_index', models.IntegerField(blank=True, null=True, verbose_name='card-index')),
                ('creation_data', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=2048, null=True)),
                ('cape', models.CharField(max_length=256, null=True)),
                ('start_data', models.DateTimeField(null=True)),
                ('finish_data', models.DateTimeField(null=True)),
                ('reminder', models.BooleanField(default=False)),
                ('reminder_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('url', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.CharField(max_length=10000)),
                ('actions', models.CharField(max_length=10000)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('picture', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('picture', models.CharField(blank=True, max_length=256, null=True)),
                ('setor', models.ManyToManyField(to='api.setor')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('creation_data', models.DateTimeField(auto_now_add=True)),
                ('cards', models.ManyToManyField(blank=True, to='api.card')),
                ('followers', models.ManyToManyField(blank=True, to='api.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('steps', models.ManyToManyField(blank=True, to='api.step')),
            ],
        ),
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('what', models.CharField(max_length=256)),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='checklist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.checklist'),
        ),
        migrations.AddField(
            model_name='card',
            name='clones',
            field=models.ManyToManyField(blank=True, to='api.card'),
        ),
        migrations.AddField(
            model_name='card',
            name='files',
            field=models.ManyToManyField(blank=True, to='api.file'),
        ),
        migrations.AddField(
            model_name='card',
            name='labels',
            field=models.ManyToManyField(blank=True, to='api.label'),
        ),
        migrations.AddField(
            model_name='card',
            name='viewers',
            field=models.ManyToManyField(blank=True, to='api.userprofile'),
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('creation_data', models.DateTimeField(auto_now_add=True)),
                ('background', models.CharField(blank=True, max_length=256, null=True)),
                ('lists', models.ManyToManyField(blank=True, to='api.list')),
                ('owner', models.ManyToManyField(blank=True, related_name='board_owner', to='api.userprofile')),
                ('rules', models.ManyToManyField(blank=True, to='api.rule')),
                ('viewers', models.ManyToManyField(blank=True, related_name='viewer', to='api.userprofile')),
            ],
        ),
    ]