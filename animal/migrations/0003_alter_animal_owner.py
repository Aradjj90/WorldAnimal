# Generated by Django 4.2.1 on 2023-07-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_remove_animal_user_animal_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='owner',
            field=models.CharField(blank=True, default='root', max_length=255, verbose_name='Owner'),
        ),
    ]
