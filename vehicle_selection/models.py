from django.db import models

# Create your models here.

class Usedcarstocks(models.Model):
    sortno = models.CharField(primary_key = True, max_length=50, blank=True, null=False)
    modelcode = models.CharField(max_length=50, blank=True)   #pk 
    typecode = models.CharField(max_length=50, blank=True, null=True) #pk 
    colorcode = models.CharField(max_length=50, blank=True, null=True) #pk
    fueltype = models.CharField(max_length=50, blank=True, null=True)
    bodycolor = models.CharField(max_length=50, blank=True, null=True)
    modelyear = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    mileage = models.CharField(max_length=50, blank=True, null=True)
    expiredateofinsp = models.DateTimeField(blank=True, null=True)
    freonprice = models.IntegerField(blank=True, null=True)
    informationcareprice = models.IntegerField(blank=True, null=True)
    salesprice = models.CharField(max_length=100000, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    dealercode = models.CharField(max_length=50, blank=True, null=True)
    YOR = models.DateTimeField(blank=True, null=True)
    carname = models.CharField(max_length=64, blank=True, null=True)
    kindofcarname = models.CharField(max_length=64, blank=True, null=True)
    bodyno = models.CharField(max_length=50, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    gradename = models.CharField(max_length=50, blank=True, null=True)
    distributorinventory = models.CharField(max_length=50, blank=True, null=True)
    stockinventory = models.CharField(max_length=50, blank=True, null=True)
    otherdealerinventory = models.CharField(max_length=50, blank=True, null=True)
# NEWCAR

class Newcarstock(models.Model):
    modelyear = models.CharField(max_length=50, blank=True, null=True)
    modelcategory = models.CharField(max_length=50, blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True, null=True)
    modelcode = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    modeltype = models.CharField(max_length=50, blank=True, null=False)
    colour = models.CharField(max_length=50, blank=True, null=True)
    colourname = models.CharField(max_length=50, blank=True, null=True)
    #compatiblemanufacturers = models.CharField(max_length=240, blank=True, null=True)
    prcodes = models.CharField(max_length=50, blank=True, null=True)
    commissionno = models.CharField(max_length=50, blank=True, null=True)
    VINnumber = models.CharField(max_length=50, blank=True, null=True)
    commissionyear = models.CharField(max_length=50, blank=True, null=True)
    importer = models.CharField(max_length=50, blank=True, null=True)
    #inventorystatus = models.CharField(max_length=15, blank=True, null=True)
    dealercode = models.CharField(max_length=50, blank=True, null=True)
    distributorinventory = models.CharField(max_length=50, blank=True, null=True)
    stockinventory = models.CharField(max_length=50, blank=True, null=True)

 # PREORDER CAR STOCK    

class Preordercarstockmst(models.Model):
    field_sequenceno = models.CharField(primary_key=True, max_length=50, null=False)
    createdusercode = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    updatedusercode = models.CharField(max_length=50, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    deleteflg = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    modelcode = models.CharField(max_length=50, blank=True, null=True)
    modelyear = models.CharField(max_length=50, blank=True, null=True)
    brandcode = models.CharField(max_length=50, blank=True, null=True)
    applydatefrom = models.CharField(max_length=50)
    applydateto = models.CharField(max_length=50)
    vehiclepriceintax = models.CharField(max_length=50, blank=True, null=True)
    orderbyflg = models.CharField(max_length=50, blank=True, null=True)
    field_remarks = models.CharField(max_length=64, blank=True, null=True)

#DISPLAYCAR

class Displaycar(models.Model):
    modelyear = models.CharField(max_length=100, blank=True, null=True)
    modelcategory = models.CharField(max_length=100, blank=True, null=True)
    gradename = models.CharField(max_length=100, blank=True, null=True)
    modelcode = models.CharField(max_length=100, blank=True, null=True)
    typecode = models.CharField(max_length=100, blank=True, null=True)
    prcodes = models.CharField(max_length=300, blank=True, null=True)
    colorcode = models.CharField(max_length=100, blank=True, null=True)
    colorname = models.CharField(max_length=100, blank=True, null=True)
    interiorcode = models.CharField(max_length=100, blank=True, null=True)
    interiorname = models.CharField(max_length=100, blank=True, null=True)
    specialmodelno = models.CharField(max_length=100, blank=True, null=True)
    applydatefrom = models.DateTimeField(blank=True, null=True)
    applydateto = models.DateTimeField(blank=True, null=True)
    createdusercode = models.CharField(max_length=100, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    updatedusercode = models.CharField(max_length=100, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    deleteflg = models.CharField(max_length=100, blank=True, null=True)
    vehiclepriceintax = models.IntegerField(blank=True, null=True)
    vehicleprice = models.IntegerField(blank=True, null=True)
    vehiclepurchasetax = models.IntegerField(blank=True, null=True)
    distributorinventory = models.CharField(max_length=100, blank=True, null=True)
    storeinventory = models.CharField(max_length=100, blank=True, null=True)

#SELECTEDCAR


class Selectedcar(models.Model):
    modelyear = models.CharField(max_length=50, blank=True, null=True)
    modelcategory = models.CharField(max_length=50, blank=True, null=True)
    gradename = models.CharField(max_length=50, blank=True, null=True)
    modelcode = models.CharField(max_length=50, blank=True, null=True)
    typecode = models.CharField(max_length=50, blank=True, null=True)
    prcodes = models.CharField(max_length=300, blank=True, null=True)
    colorcode = models.CharField(max_length=50, blank=True, null=True)
    colorname = models.CharField(max_length=50, blank=True, null=True)
    interiorcode = models.CharField(max_length=50, blank=True, null=True)
    interiorname = models.CharField(max_length=50, blank=True, null=True)
    specialmodelno = models.CharField(max_length=50, blank=True, null=True)
    applydatefrom = models.DateTimeField(blank=True, null=True)
    applydateto = models.DateTimeField(blank=True, null=True)
    createdusercode = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    updatedusercode = models.CharField(max_length=50, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    deleteflg = models.CharField(max_length=50, blank=True, null=True)
    vehiclepriceintax = models.IntegerField(blank=True, null=True)
    vehicleprice = models.IntegerField(blank=True, null=True)
    vehiclepurchasetax = models.IntegerField(blank=True, null=True)
    distributorinventory = models.CharField(max_length=50, blank=True, null=True)
    storeinventory = models.CharField(max_length=50, blank=True, null=True)
  
#APARNA

class aparna(models.Model):
    modelyear = models.CharField(max_length=50, blank=True, null=True)
    modelcategory = models.CharField(max_length=50, blank=True, null=True)
    gradename = models.CharField(max_length=50, blank=True, null=True)
    modelcode = models.CharField(max_length=50, blank=True, null=True)
    typecode = models.CharField(max_length=50, blank=True, null=True)
    prcodes = models.CharField(max_length=300, blank=True, null=True)
    colorcode = models.CharField(max_length=50, blank=True, null=True)
    colorname = models.CharField(max_length=50, blank=True, null=True)
    interiorcode = models.CharField(max_length=50, blank=True, null=True)
    interiorname = models.CharField(max_length=50, blank=True, null=True)
    specialmodelno = models.CharField(max_length=50, blank=True, null=True)
    applydatefrom = models.DateTimeField(blank=True, null=True)
    applydateto = models.DateTimeField(blank=True, null=True)
    createdusercode = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    updatedusercode = models.CharField(max_length=50, blank=True, null=True)
    updateddate = models.DateTimeField(blank=True, null=True)
    deleteflg = models.CharField(max_length=50, blank=True, null=True)
    vehiclepriceintax = models.IntegerField(blank=True, null=True)
    vehicleprice = models.IntegerField(blank=True, null=True)
    vehiclepurchasetax = models.IntegerField(blank=True, null=True)
    distributorinventory = models.CharField(max_length=50, blank=True, null=True)
    storeinventory = models.CharField(max_length=50, blank=True, null=True)