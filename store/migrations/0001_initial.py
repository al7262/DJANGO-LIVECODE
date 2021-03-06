# Generated by Django 3.0 on 2019-12-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('Photo URL', models.CharField(default=None, max_length=1000)),
                ('detail', models.TextField()),
            ],
        ),
    ]
