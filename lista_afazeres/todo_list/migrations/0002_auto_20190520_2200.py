# Generated by Django 2.2.1 on 2019-05-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemfazer',
            options={'verbose_name': 'Item a fazer', 'verbose_name_plural': 'Itens a fazer'},
        ),
        migrations.AlterField(
            model_name='itemfazer',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]