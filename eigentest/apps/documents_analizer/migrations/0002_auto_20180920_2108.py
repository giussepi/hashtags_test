# Generated by Django 2.1.1 on 2018-09-20 21:08

from django.db import migrations, models
import documents_analizer.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents_analizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_file',
            field=models.FileField(upload_to=documents_analizer.models.Document.update_filename),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='word',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]