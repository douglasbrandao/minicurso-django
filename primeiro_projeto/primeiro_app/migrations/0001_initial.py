# Generated by Django 2.2.1 on 2019-05-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('idade', models.IntegerField()),
                ('curso', models.CharField(choices=[('ECO', 'Engenharia de Computação'), ('ECA', 'Eng. de Controle e Automação'), ('SPI', 'Sistemas para internet'), ('TUR', 'Turismo')], default='ECO', max_length=3)),
            ],
        ),
    ]
