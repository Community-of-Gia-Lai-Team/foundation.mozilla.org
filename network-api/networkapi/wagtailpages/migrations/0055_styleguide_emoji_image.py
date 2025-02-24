# Generated by Django 3.2.13 on 2022-09-08 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailpages', '0054_merge_20220906_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='styleguide',
            name='emoji_image',
            field=models.ForeignKey(blank=True, help_text='Emoji style image for use in the styleguide.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
    ]
