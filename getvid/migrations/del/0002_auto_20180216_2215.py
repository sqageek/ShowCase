# Generated by Django 2.0.2 on 2018-02-16 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('getvid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='providerID',
            field=models.ForeignKey(default='12345678-1234-5678-1234-567812345678', on_delete=django.db.models.deletion.SET_DEFAULT, to='getvid.Provider'),
        ),
    ]