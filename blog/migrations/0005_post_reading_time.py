# Generated by Django 4.2.5 on 2023-10-12 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_active_alter_comment_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reading_time',
            field=models.PositiveIntegerField(default=0, verbose_name='زمان مطالعه '),
            preserve_default=False,
        ),
    ]
