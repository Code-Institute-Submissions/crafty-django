{"filter":false,"title":"0006_auto_20200319_1343.py","tooltip":"/accounts/migrations/0006_auto_20200319_1343.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":34,"column":5},"action":"insert","lines":["from django.db import migrations","","","class Migration(migrations.Migration):","","    dependencies = [","        ('accounts', '0005_auto_20200319_1101'),","    ]","","    operations = [","        migrations.RemoveField(","            model_name='profile',","            name='email',","        ),","        migrations.RemoveField(","            model_name='profile',","            name='first_name',","        ),","        migrations.RemoveField(","            model_name='profile',","            name='last_name',","        ),","        migrations.RemoveField(","            model_name='profile',","            name='password1',","        ),","        migrations.RemoveField(","            model_name='profile',","            name='password2',","        ),","        migrations.RemoveField(","            model_name='profile',","            name='username',","        ),","    ]"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":34,"column":5},"end":{"row":34,"column":5},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":6,"state":"start","mode":"ace/mode/python"}},"timestamp":1585147032446,"hash":"f5230f2a9cfea597810f9b5972c21a3c5d3390ba"}