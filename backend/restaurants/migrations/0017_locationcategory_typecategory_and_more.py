# Generated by Django 4.1.3 on 2022-11-20 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0016_alter_restaurant_location_type_alter_restaurant_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.locationcategory'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.typecategory'),
        ),
    ]