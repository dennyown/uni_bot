# Generated by Django 3.1.4 on 2020-12-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_userunimodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userunimodel',
            name='telegram_data',
            field=models.CharField(db_index=True, default='', max_length=300),
        ),
    ]
