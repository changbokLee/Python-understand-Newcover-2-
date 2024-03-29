# Generated by Django 2.2.3 on 2019-07-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, verbose_name='아이디')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='가입일시')),
            ],
            options={
                'db_table': 'dls_myuser',
            },
        ),
    ]
