# Generated by Django 5.1 on 2024-08-20 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_enquiry_id_alter_enquiry_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
