{"filter":false,"title":"0003_profile_user.py","tooltip":"/accounts/migrations/0003_profile_user.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":18,"column":5},"action":"insert","lines":["from django.conf import settings","from django.db import migrations, models","import django.db.models.deletion","","","class Migration(migrations.Migration):","","    dependencies = [","        migrations.swappable_dependency(settings.AUTH_USER_MODEL),","        ('accounts', '0002_auto_20200318_1332'),","    ]","","    operations = [","        migrations.AddField(","            model_name='profile',","            name='user',","            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),","        ),","    ]"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":5},"end":{"row":18,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1585146881462,"hash":"926e9a1d8c911d1a22d3c894772ef2a4a557020e"}