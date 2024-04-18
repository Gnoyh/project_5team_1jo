# Generated by Django 5.0.4 on 2024-04-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecomBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('recomment', models.CharField(default='없음', max_length=2000)),
                ('recomno', models.CharField(default='0000', max_length=20)),
                ('drcode', models.IntegerField(default=0)),
                ('keyword', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
