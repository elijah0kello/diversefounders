# Generated by Django 3.2.8 on 2021-10-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_editpage_user1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editpage',
            name='profileimg',
            field=models.ImageField(blank=True, null=True, upload_to='pics/'),
        ),
    ]