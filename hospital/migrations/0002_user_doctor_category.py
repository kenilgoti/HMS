# Generated by Django 4.1.5 on 2023-02-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='doctor_category',
            field=models.CharField(db_column='D_Category', default='Mbbs', max_length=255),
        ),
    ]
