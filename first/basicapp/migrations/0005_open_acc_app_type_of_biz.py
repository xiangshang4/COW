# Generated by Django 2.1 on 2019-07-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0004_auto_20190725_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='open_acc_app',
            name='type_of_biz',
            field=models.CharField(choices=[('Private Limited/Public Company', ' Private Limited/Public Company'), ('Representative Office (IE)', ' Representative Office (IE)'), ('Sole Proprietorship', ' Sole Proprietorship'), ('Partnership / Joint Venture', ' Partnership / Joint Venture'), ('Branch', ' Branch'), ('Others', 'Association / Club / Society / Trusts/ Estate / Others')], default='', max_length=256),
            preserve_default=False,
        ),
    ]
