# Generated by Django 4.0.2 on 2022-02-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_topic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='related_posts',
            field=models.ManyToManyField(related_name='topics', to='posts.Post'),
        ),
    ]
