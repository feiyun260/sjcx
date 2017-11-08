# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    ccuscode = models.CharField(db_column='cCusCode', primary_key=True, max_length=20)  # 会员编号
    ccusname = models.CharField(db_column='cCusName', max_length=98, blank=True, null=True)  # 会员姓名
    ccusabbname = models.CharField(db_column='cCusAbbName', max_length=60)  # 会员编号姓名合并

    def __str__(self):
        return self.ccusname

    class Meta:
        managed = False
        db_table = 'Customer'


class YyServiceitem(models.Model):
    cvouchcode = models.CharField(db_column='cVouchCode', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cmaker = models.CharField(db_column='cMaker', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dmakedateex = models.DateTimeField(db_column='dMakeDateEx', blank=True, null=True)  # Field name made lowercase.
    dmakedate = models.DateTimeField(db_column='dMakeDate', blank=True, null=True)  # Field name made lowercase.
    cmender = models.CharField(db_column='cMender', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dmodifydateex = models.DateTimeField(db_column='dModifyDateEx', blank=True, null=True)  # Field name made lowercase.
    dmodifydate = models.DateTimeField(db_column='dModifyDate', blank=True, null=True)  # Field name made lowercase.
    cauditor = models.CharField(db_column='cAuditor', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dauditdateex = models.DateTimeField(db_column='dAuditDateEx', blank=True, null=True)  # Field name made lowercase.
    dauditdate = models.DateTimeField(db_column='dAuditDate', blank=True, null=True)  # Field name made lowercase.
    cmemo = models.CharField(db_column='cMemo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ddate = models.DateTimeField(db_column='dDate', blank=True, null=True)  # Field name made lowercase.
    cdefine1 = models.CharField(db_column='cDefine1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdefine2 = models.CharField(db_column='cDefine2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdefine3 = models.CharField(db_column='cDefine3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cdefine4 = models.DateTimeField(db_column='cDefine4', blank=True, null=True)  # Field name made lowercase.
    cdefine5 = models.IntegerField(db_column='cDefine5', blank=True, null=True)  # Field name made lowercase.
    cdefine6 = models.DateTimeField(db_column='cDefine6', blank=True, null=True)  # Field name made lowercase.
    cdefine7 = models.DecimalField(db_column='cDefine7', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    cdefine8 = models.CharField(db_column='cDefine8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cdefine9 = models.CharField(db_column='cDefine9', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cdefine10 = models.CharField(db_column='cDefine10', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cdefine11 = models.CharField(db_column='cDefine11', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine12 = models.CharField(db_column='cDefine12', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine13 = models.CharField(db_column='cDefine13', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine14 = models.CharField(db_column='cDefine14', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine15 = models.IntegerField(db_column='cDefine15', blank=True, null=True)  # Field name made lowercase.
    cdefine16 = models.DecimalField(db_column='cDefine16', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iswfcontrolled = models.IntegerField(blank=True, null=True)
    iverifystate = models.IntegerField(blank=True, null=True)
    ireturncount = models.IntegerField(blank=True, null=True)
    uapruntime_rowno = models.IntegerField(db_column='UAPRuntime_RowNO', blank=True, null=True)  # Field name made lowercase.
    uap_vouchertransform_rowkey = models.CharField(db_column='UAP_VoucherTransform_Rowkey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdepcode = models.CharField(db_column='cDepCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ccuscode = models.ForeignKey(Customer,db_column='cCusCode')  # Field name made lowercase.
    cpersoncode = models.CharField(db_column='cPersonCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cexch_name = models.CharField(max_length=8, blank=True, null=True)
    iexchrate = models.DecimalField(db_column='iExchRate', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ccontactname = models.CharField(db_column='cContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ccusoaddress = models.CharField(db_column='cCusOAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cphone = models.CharField(db_column='cPhone', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iamount = models.DecimalField(db_column='iAmount', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YY_ServiceItem'


class YyServiceitems(models.Model):
    cinvcode = models.CharField(db_column='cInvCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fquantity = models.DecimalField(db_column='fQuantity', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    fprice = models.DecimalField(db_column='fPrice', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    famount = models.DecimalField(db_column='fAmount', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    cdetailmemo = models.CharField(db_column='cDetailMemo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cverificationcode = models.CharField(db_column='cVerificationCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cshopcode = models.CharField(db_column='cShopCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fcommoney = models.DecimalField(max_digits=28, decimal_places=10, blank=True, null=True)
    cdefine22 = models.CharField(db_column='cDefine22', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cdefine23 = models.CharField(db_column='cDefine23', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cdefine24 = models.CharField(db_column='cDefine24', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cdefine25 = models.CharField(db_column='cDefine25', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cdefine26 = models.DecimalField(db_column='cDefine26', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    cdefine27 = models.DecimalField(db_column='cDefine27', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    cdefine28 = models.CharField(db_column='cDefine28', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine29 = models.CharField(db_column='cDefine29', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine30 = models.CharField(db_column='cDefine30', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine31 = models.CharField(db_column='cDefine31', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine32 = models.CharField(db_column='cDefine32', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine33 = models.CharField(db_column='cDefine33', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cdefine34 = models.IntegerField(db_column='cDefine34', blank=True, null=True)  # Field name made lowercase.
    cdefine35 = models.IntegerField(db_column='cDefine35', blank=True, null=True)  # Field name made lowercase.
    cdefine36 = models.DateTimeField(db_column='cDefine36', blank=True, null=True)  # Field name made lowercase.
    cdefine37 = models.DateTimeField(db_column='cDefine37', blank=True, null=True)  # Field name made lowercase.
    bsale = models.CharField(db_column='bSale', max_length=32, blank=True, null=True)  # Field name made lowercase.
    submitperson = models.CharField(db_column='SubmitPerson', max_length=40, blank=True, null=True)  # Field name made lowercase.
    submitdate = models.DateTimeField(db_column='SubmitDate', blank=True, null=True)  # Field name made lowercase.
    dusetime = models.DateTimeField(db_column='DUSETIME', blank=True, null=True)  # Field name made lowercase.
    autoid = models.IntegerField(db_column='AUTOID', primary_key=True)  # Field name made lowercase.
    id = models.ForeignKey(YyServiceitem,db_column='ID')  # Field name made lowercase.
    uapruntime_rowno = models.IntegerField(db_column='UAPRuntime_RowNO', blank=True, null=True)  # Field name made lowercase.
    uap_vouchertransform_rowkey = models.CharField(db_column='UAP_VoucherTransform_Rowkey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refmainid = models.CharField(db_column='RefMainID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refrowid = models.CharField(db_column='RefRowID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    itaxrate = models.DecimalField(db_column='iTaxRate', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    itax = models.DecimalField(db_column='iTax', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    iorimoney = models.DecimalField(db_column='iOriMoney', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    breturndate = models.DateTimeField(db_column='bReturndate', blank=True, null=True)  # Field name made lowercase.
    breturnflag = models.CharField(db_column='bReturnFlag', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cpznum = models.CharField(db_column='cPZNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cpzid = models.CharField(db_column='cPzID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commoneypznum = models.CharField(db_column='commoneyPzNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    commoneypzid = models.CharField(db_column='commoneyPzId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    salespznum = models.CharField(db_column='salesPzNum', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salespzid = models.CharField(db_column='salesPzId', max_length=30, blank=True, null=True)  # Field name made lowercase.
    iunitprice = models.DecimalField(db_column='iUnitPrice', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    itaxunitprice = models.DecimalField(db_column='iTaxUnitPrice', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    imoney = models.DecimalField(db_column='iMoney', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    isum = models.DecimalField(db_column='iSum', max_digits=28, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'YY_ServiceItems'


class Entry(models.Model):
    name = models.CharField(max_length=30)
    cbs = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=30)
    entry = models.ForeignKey(Entry)

    def __str__(self):
        return self.name