# Generated by Django 3.0.3 on 2020-04-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200314_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('local', 'local'), ('ldap', 'ldap')], default='local', max_length=20, verbose_name='user type'),
        ),
    ]
