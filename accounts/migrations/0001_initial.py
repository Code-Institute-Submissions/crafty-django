from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('username', models.CharField(max_length=150)),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=15)),
                ('password2', models.CharField(max_length=15)),
                ('experience', models.CharField(max_length=300)),
                ('style', models.CharField(max_length=200)),
                ('wood_source', models.BooleanField(default=True)),
            ],
        ),
    ]