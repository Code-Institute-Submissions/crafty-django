# Generated by Django 2.0.2 on 2020-03-20 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='images')),
                ('wood', models.CharField(default='', max_length=50)),
                ('style', models.CharField(default='', max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
