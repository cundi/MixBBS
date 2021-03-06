# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AddField(
            model_name='account',
            name='time_zone',
            field=models.FloatField(default=8.0, verbose_name='\u65f6\u533a\u9009\u62e9', choices=[(-12.0, '-12'), (-11.0, '-11'), (-10.0, '-10'), (-9.5, '-09.5'), (-9.0, '-09'), (-8.5, '-08.5'), (-8.0, '-08 PST'), (-7.0, '-07 MST'), (-6.0, '-06 CST'), (-5.0, '-05 EST'), (-4.0, '-04 AST'), (-3.5, '-03.5'), (-3.0, '-03 ADT'), (-2.0, '-02'), (-1.0, '-01'), (0.0, '00 GMT'), (1.0, '+01 CET'), (2.0, '+02'), (3.0, '+03'), (3.5, '+03.5'), (4.0, '+04'), (4.5, '+04.5'), (5.0, '+05'), (5.5, '+05.5'), (6.0, '+06'), (6.5, '+06.5'), (7.0, '+07'), (8.0, '+08'), (9.0, '+09'), (9.5, '+09.5'), (10.0, '+10'), (10.5, '+10.5'), (11.0, '+11'), (11.5, '+11.5'), (12.0, '+12'), (13.0, '+13'), (14.0, '+14')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_activity',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterModelTable(
            name='account',
            table=None,
        ),
    ]
