# Generated by Django 4.1.7 on 2023-05-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_selection', '0002_displaycar_distributorinventory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newcarstock',
            old_name='inventorystatus',
            new_name='dealercode',
        ),
        migrations.RemoveField(
            model_name='newcarstock',
            name='compatiblemanufacturers',
        ),
        migrations.AddField(
            model_name='newcarstock',
            name='colourname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]