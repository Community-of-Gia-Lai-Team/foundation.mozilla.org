# Generated by Django 3.2.13 on 2022-10-13 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('mozfest', '0008_adds_profile_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mozfestprimarypage',
            name='search_image',
            field=models.ForeignKey(blank=True, help_text='Image must be high quality, include our logo mark and have the dimensions 1200 x 628 px. For more design guidelines see here: https://foundation.mozilla.org/en/docs/brand/brand-identity/social-media/#og-images', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image'),
        ),
    ]
