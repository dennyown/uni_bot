# Generated by Django 3.1.4 on 2020-12-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralUniModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_message', models.CharField(db_index=True, max_length=150)),
            ],
        ),
    ]