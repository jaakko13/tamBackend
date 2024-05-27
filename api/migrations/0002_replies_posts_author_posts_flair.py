# Generated by Django 5.0.6 on 2024-05-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('top_parent', models.IntegerField()),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='posts',
            name='flair',
            field=models.CharField(default='Discussion', max_length=20),
        ),
    ]