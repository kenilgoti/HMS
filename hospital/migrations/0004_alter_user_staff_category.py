# Generated by Django 4.1.5 on 2023-02-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_user_staff_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='staff_category',
            field=models.CharField(db_column='S_Category', default='Compounder', max_length=255),
        ),
    ]
