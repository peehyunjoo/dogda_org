# Generated by Django 2.2 on 2019-07-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20190703_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='flowers',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]