# Generated by Django 4.1.7 on 2023-05-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_selection', '0004_rename_dealerinventory_usedcarstocks_dealercode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='aparna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelyear', models.CharField(blank=True, max_length=50, null=True)),
                ('modelcategory', models.CharField(blank=True, max_length=50, null=True)),
                ('gradename', models.CharField(blank=True, max_length=50, null=True)),
                ('modelcode', models.CharField(blank=True, max_length=50, null=True)),
                ('typecode', models.CharField(blank=True, max_length=50, null=True)),
                ('prcodes', models.CharField(blank=True, max_length=300, null=True)),
                ('colorcode', models.CharField(blank=True, max_length=50, null=True)),
                ('colorname', models.CharField(blank=True, max_length=50, null=True)),
                ('interiorcode', models.CharField(blank=True, max_length=50, null=True)),
                ('interiorname', models.CharField(blank=True, max_length=50, null=True)),
                ('specialmodelno', models.CharField(blank=True, max_length=50, null=True)),
                ('applydatefrom', models.DateTimeField(blank=True, null=True)),
                ('applydateto', models.DateTimeField(blank=True, null=True)),
                ('createdusercode', models.CharField(blank=True, max_length=50, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('updatedusercode', models.CharField(blank=True, max_length=50, null=True)),
                ('updateddate', models.DateTimeField(blank=True, null=True)),
                ('deleteflg', models.CharField(blank=True, max_length=50, null=True)),
                ('vehiclepriceintax', models.IntegerField(blank=True, null=True)),
                ('vehicleprice', models.IntegerField(blank=True, null=True)),
                ('vehiclepurchasetax', models.IntegerField(blank=True, null=True)),
                ('distributorinventory', models.CharField(blank=True, max_length=15, null=True)),
                ('storeinventory', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]