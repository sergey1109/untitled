# Generated by Django 3.1.1 on 2020-09-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='H_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1500)),
                ('price', models.FloatField()),
                ('hot_price', models.BooleanField(default=False)),
                ('new_price', models.FloatField(blank=True, null=True)),
                ('ranks', models.CharField(choices=[('1*', 'One star hotel '), ('2*', 'Two stars hotel '), ('3*', 'Three stars hotel '), ('4*', 'Four stars hotel '), ('5*', 'Five stars hotel ')], max_length=255)),
            ],
        ),
    ]
