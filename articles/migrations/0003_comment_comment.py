# Generated by Django 3.0.6 on 2020-06-08 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200608_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='articles.Comment'),
        ),
    ]
