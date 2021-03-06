# Generated by Django 3.0.2 on 2022-02-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='image_link',
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.FileField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='active',
            field=models.CharField(choices=[('0', 'Active'), ('1', 'Sold')], default='0', max_length=30, verbose_name='STATUS'),
        ),
    ]
