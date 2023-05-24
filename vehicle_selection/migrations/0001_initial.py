# Generated by Django 4.1.7 on 2023-05-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Displaycar',
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
            ],
        ),
        migrations.CreateModel(
            name='Newcarstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelyear', models.CharField(blank=True, max_length=50, null=True)),
                ('modelcategory', models.CharField(blank=True, max_length=50, null=True)),
                ('grade', models.CharField(blank=True, max_length=50, null=True)),
                ('modelcode', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('modeltype', models.CharField(blank=True, max_length=50)),
                ('colour', models.CharField(blank=True, max_length=50, null=True)),
                ('compatiblemanufacturers', models.CharField(blank=True, max_length=240, null=True)),
                ('prcodes', models.CharField(blank=True, max_length=50, null=True)),
                ('commissionno', models.CharField(blank=True, max_length=50, null=True)),
                ('VINnumber', models.CharField(blank=True, max_length=50, null=True)),
                ('commissionyear', models.CharField(blank=True, max_length=50, null=True)),
                ('importer', models.CharField(blank=True, max_length=50, null=True)),
                ('inventorystatus', models.CharField(blank=True, max_length=15, null=True)),
                ('distributorinventory', models.CharField(blank=True, max_length=15, null=True)),
                ('stockinventory', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Preordercarstockmst',
            fields=[
                ('field_sequenceno', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('createdusercode', models.CharField(blank=True, max_length=50, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('updatedusercode', models.CharField(blank=True, max_length=50, null=True)),
                ('updateddate', models.DateTimeField(blank=True, null=True)),
                ('deleteflg', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('modelcode', models.CharField(blank=True, max_length=50, null=True)),
                ('modelyear', models.CharField(blank=True, max_length=50, null=True)),
                ('brandcode', models.CharField(blank=True, max_length=50, null=True)),
                ('applydatefrom', models.CharField(max_length=50)),
                ('applydateto', models.CharField(max_length=50)),
                ('vehiclepriceintax', models.CharField(blank=True, max_length=50, null=True)),
                ('orderbyflg', models.CharField(blank=True, max_length=50, null=True)),
                ('field_remarks', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Selectedcar',
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
                ('deleteflg', models.CharField(blank=True, max_length=1, null=True)),
                ('vehiclepriceintax', models.IntegerField(blank=True, null=True)),
                ('vehicleprice', models.IntegerField(blank=True, null=True)),
                ('vehiclepurchasetax', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usedcarstocks',
            fields=[
                ('sortno', models.CharField(blank=True, max_length=7, primary_key=True, serialize=False)),
                ('modelcode', models.CharField(blank=True, max_length=8)),
                ('typecode', models.CharField(blank=True, max_length=3, null=True)),
                ('colorcode', models.CharField(blank=True, max_length=4, null=True)),
                ('fueltype', models.CharField(blank=True, max_length=2, null=True)),
                ('bodycolor', models.CharField(blank=True, max_length=32, null=True)),
                ('modelyear', models.CharField(blank=True, max_length=4, null=True)),
                ('createddate', models.DateTimeField(blank=True, null=True)),
                ('mileage', models.CharField(blank=True, max_length=32, null=True)),
                ('expiredateofinsp', models.DateTimeField(blank=True, null=True)),
                ('freonprice', models.IntegerField(blank=True, null=True)),
                ('informationcareprice', models.IntegerField(blank=True, null=True)),
                ('salesprice', models.CharField(blank=True, max_length=100000, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('dealerinventory', models.CharField(blank=True, max_length=5, null=True)),
                ('YOR', models.DateTimeField(blank=True, null=True)),
                ('carname', models.CharField(blank=True, max_length=64, null=True)),
                ('kindofcarname', models.CharField(blank=True, max_length=64, null=True)),
                ('bodyno', models.CharField(blank=True, max_length=18, null=True)),
                ('updateddate', models.DateTimeField(blank=True, null=True)),
                ('gradename', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
