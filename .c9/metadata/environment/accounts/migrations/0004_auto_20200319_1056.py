{"filter":false,"title":"0004_auto_20200319_1056.py","tooltip":"/accounts/migrations/0004_auto_20200319_1056.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":72,"column":5},"action":"insert","lines":["from django.conf import settings","from django.db import migrations, models","import django.db.models.deletion","","","class Migration(migrations.Migration):","","    dependencies = [","        ('accounts', '0003_profile_user'),","    ]","","    operations = [","        migrations.AddField(","            model_name='profile',","            name='country',","            field=models.CharField(blank=True, default='', max_length=100),","        ),","        migrations.AlterField(","            model_name='profile',","            name='address_one',","            field=models.CharField(blank=True, default='', max_length=100),","        ),","        migrations.AlterField(","            model_name='profile',","            name='address_two',","            field=models.CharField(blank=True, default='', max_length=100),","        ),","        migrations.AlterField(","            model_name='profile',","            name='city',","            field=models.CharField(blank=True, default='', max_length=50),","        ),","        migrations.AlterField(","            model_name='profile',","            name='email',","            field=models.EmailField(blank=True, default='', max_length=254),","        ),","        migrations.AlterField(","            model_name='profile',","            name='experience',","            field=models.CharField(blank=True, default='', max_length=300),","        ),","        migrations.AlterField(","            model_name='profile',","            name='first_name',","            field=models.CharField(blank=True, default='', max_length=12),","        ),","        migrations.AlterField(","            model_name='profile',","            name='last_name',","            field=models.CharField(blank=True, default='', max_length=12),","        ),","        migrations.AlterField(","            model_name='profile',","            name='password1',","            field=models.CharField(default='', max_length=15),","        ),","        migrations.AlterField(","            model_name='profile',","            name='password2',","            field=models.CharField(default='', max_length=15),","        ),","        migrations.AlterField(","            model_name='profile',","            name='style',","            field=models.CharField(blank=True, default='', max_length=200),","        ),","        migrations.AlterField(","            model_name='profile',","            name='user',","            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),","        ),","    ]"],"id":1}]]},"ace":{"folds":[],"scrolltop":465.625,"scrollleft":0,"selection":{"start":{"row":72,"column":5},"end":{"row":72,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1585146925970,"hash":"b8292b6ca2708f4186dbc420b248b8ac4650e246"}