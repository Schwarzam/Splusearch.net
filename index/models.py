from django.db import models
from django.contrib.auth.models import User

## func that creates the table
def create_model(name):
    class CustomModel(models.Model):
        # define your fileds here
        id = models.CharField(db_column='ID', primary_key=True, max_length=-1)  # Field name made lowercase.
        ra = models.CharField(db_column='RA', max_length=-1)  # Field name made lowercase.
        dec = models.CharField(db_column='Dec', max_length=-1)  # Field name made lowercase.
        x = models.CharField(db_column='X', max_length=-1)  # Field name made lowercase.
        y = models.CharField(db_column='Y', max_length=-1)  # Field name made lowercase.
        isoarea = models.CharField(db_column='ISOarea', max_length=-1)  # Field name made lowercase.
        s2ndet = models.CharField(db_column='s2nDet', max_length=-1)  # Field name made lowercase.
        photoflag = models.CharField(db_column='PhotoFlag', max_length=-1)  # Field name made lowercase.
        fwhm = models.CharField(db_column='FWHM', max_length=-1)  # Field name made lowercase.
        fwhm_n = models.CharField(db_column='FWHM_n', max_length=-1)  # Field name made lowercase.
        mumax = models.CharField(db_column='MUMAX', max_length=-1)  # Field name made lowercase.
        a = models.CharField(db_column='A', max_length=-1)  # Field name made lowercase.
        b = models.CharField(db_column='B', max_length=-1)  # Field name made lowercase.
        theta = models.CharField(db_column='THETA', max_length=-1)  # Field name made lowercase.
        flraddet = models.CharField(db_column='FlRadDet', max_length=-1)  # Field name made lowercase.
        krraddet = models.CharField(db_column='KrRadDet', max_length=-1)  # Field name made lowercase.
        ndet_auto = models.CharField(db_column='nDet_auto', max_length=-1)  # Field name made lowercase.
        ndet_petro = models.CharField(db_column='nDet_petro', max_length=-1)  # Field name made lowercase.
        ndet_aper = models.CharField(db_column='nDet_aper', max_length=-1)  # Field name made lowercase.
        ujava_auto = models.CharField(db_column='uJAVA_auto', max_length=-1)  # Field name made lowercase.
        eujava_auto = models.CharField(db_column='euJAVA_auto', max_length=-1)  # Field name made lowercase.
        s2n_ujava_auto = models.CharField(db_column='s2n_uJAVA_auto', max_length=-1)  # Field name made lowercase.
        ujava_petro = models.CharField(db_column='uJAVA_petro', max_length=-1)  # Field name made lowercase.
        eujava_petro = models.CharField(db_column='euJAVA_petro', max_length=-1)  # Field name made lowercase.
        s2n_ujava_petro = models.CharField(db_column='s2n_uJAVA_petro', max_length=-1)  # Field name made lowercase.
        ujava_aper = models.CharField(db_column='uJAVA_aper', max_length=-1)  # Field name made lowercase.
        eujava_aper = models.CharField(db_column='euJAVA_aper', max_length=-1)  # Field name made lowercase.
        s2n_ujava_aper = models.CharField(db_column='s2n_uJAVA_aper', max_length=-1)  # Field name made lowercase.
        f378_auto = models.CharField(db_column='F378_auto', max_length=-1)  # Field name made lowercase.
        ef378_auto = models.CharField(db_column='eF378_auto', max_length=-1)  # Field name made lowercase.
        s2n_f378_auto = models.CharField(db_column='s2n_F378_auto', max_length=-1)  # Field name made lowercase.
        f378_petro = models.CharField(db_column='F378_petro', max_length=-1)  # Field name made lowercase.
        ef378_petro = models.CharField(db_column='eF378_petro', max_length=-1)  # Field name made lowercase.
        s2n_f378_petro = models.CharField(db_column='s2n_F378_petro', max_length=-1)  # Field name made lowercase.
        f378_aper = models.CharField(db_column='F378_aper', max_length=-1)  # Field name made lowercase.
        ef378_aper = models.CharField(db_column='eF378_aper', max_length=-1)  # Field name made lowercase.
        s2n_f378_aper = models.CharField(db_column='s2n_F378_aper', max_length=-1)  # Field name made lowercase.
        f395_auto = models.CharField(db_column='F395_auto', max_length=-1)  # Field name made lowercase.
        ef395_auto = models.CharField(db_column='eF395_auto', max_length=-1)  # Field name made lowercase.
        s2n_f395_auto = models.CharField(db_column='s2n_F395_auto', max_length=-1)  # Field name made lowercase.
        f395_petro = models.CharField(db_column='F395_petro', max_length=-1)  # Field name made lowercase.
        ef395_petro = models.CharField(db_column='eF395_petro', max_length=-1)  # Field name made lowercase.
        s2n_f395_petro = models.CharField(db_column='s2n_F395_petro', max_length=-1)  # Field name made lowercase.
        f395_aper = models.CharField(db_column='F395_aper', max_length=-1)  # Field name made lowercase.
        ef395_aper = models.CharField(db_column='eF395_aper', max_length=-1)  # Field name made lowercase.
        s2n_f395_aper = models.CharField(db_column='s2n_F395_aper', max_length=-1)  # Field name made lowercase.
        f410_auto = models.CharField(db_column='F410_auto', max_length=-1)  # Field name made lowercase.
        ef410_auto = models.CharField(db_column='eF410_auto', max_length=-1)  # Field name made lowercase.
        s2n_f410_auto = models.CharField(db_column='s2n_F410_auto', max_length=-1)  # Field name made lowercase.
        f410_petro = models.CharField(db_column='F410_petro', max_length=-1)  # Field name made lowercase.
        ef410_petro = models.CharField(db_column='eF410_petro', max_length=-1)  # Field name made lowercase.
        s2n_f410_petro = models.CharField(db_column='s2n_F410_petro', max_length=-1)  # Field name made lowercase.
        f410_aper = models.CharField(db_column='F410_aper', max_length=-1)  # Field name made lowercase.
        ef410_aper = models.CharField(db_column='eF410_aper', max_length=-1)  # Field name made lowercase.
        s2n_f410_aper = models.CharField(db_column='s2n_F410_aper', max_length=-1)  # Field name made lowercase.
        f430_auto = models.CharField(db_column='F430_auto', max_length=-1)  # Field name made lowercase.
        ef430_auto = models.CharField(db_column='eF430_auto', max_length=-1)  # Field name made lowercase.
        s2n_f430_auto = models.CharField(db_column='s2n_F430_auto', max_length=-1)  # Field name made lowercase.
        f430_petro = models.CharField(db_column='F430_petro', max_length=-1)  # Field name made lowercase.
        ef430_petro = models.CharField(db_column='eF430_petro', max_length=-1)  # Field name made lowercase.
        s2n_f430_petro = models.CharField(db_column='s2n_F430_petro', max_length=-1)  # Field name made lowercase.
        f430_aper = models.CharField(db_column='F430_aper', max_length=-1)  # Field name made lowercase.
        ef430_aper = models.CharField(db_column='eF430_aper', max_length=-1)  # Field name made lowercase.
        s2n_f430_aper = models.CharField(db_column='s2n_F430_aper', max_length=-1)  # Field name made lowercase.
        g_auto = models.CharField(max_length=-1)
        eg_auto = models.CharField(max_length=-1)
        s2n_g_auto = models.CharField(max_length=-1)
        g_petro = models.CharField(max_length=-1)
        eg_petro = models.CharField(max_length=-1)
        s2n_g_petro = models.CharField(max_length=-1)
        g_aper = models.CharField(max_length=-1)
        eg_aper = models.CharField(max_length=-1)
        s2n_g_aper = models.CharField(max_length=-1)
        f515_auto = models.CharField(db_column='F515_auto', max_length=-1)  # Field name made lowercase.
        ef515_auto = models.CharField(db_column='eF515_auto', max_length=-1)  # Field name made lowercase.
        s2n_f515_auto = models.CharField(db_column='s2n_F515_auto', max_length=-1)  # Field name made lowercase.
        f515_petro = models.CharField(db_column='F515_petro', max_length=-1)  # Field name made lowercase.
        ef515_petro = models.CharField(db_column='eF515_petro', max_length=-1)  # Field name made lowercase.
        s2n_f515_petro = models.CharField(db_column='s2n_F515_petro', max_length=-1)  # Field name made lowercase.
        f515_aper = models.CharField(db_column='F515_aper', max_length=-1)  # Field name made lowercase.
        ef515_aper = models.CharField(db_column='eF515_aper', max_length=-1)  # Field name made lowercase.
        s2n_f515_aper = models.CharField(db_column='s2n_F515_aper', max_length=-1)  # Field name made lowercase.
        r_auto = models.CharField(max_length=-1)
        er_auto = models.CharField(max_length=-1)
        s2n_r_auto = models.CharField(max_length=-1)
        r_petro = models.CharField(max_length=-1)
        er_petro = models.CharField(max_length=-1)
        s2n_r_petro = models.CharField(max_length=-1)
        r_aper = models.CharField(max_length=-1)
        er_aper = models.CharField(max_length=-1)
        s2n_r_aper = models.CharField(max_length=-1)
        f660_auto = models.CharField(db_column='F660_auto', max_length=-1)  # Field name made lowercase.
        ef660_auto = models.CharField(db_column='eF660_auto', max_length=-1)  # Field name made lowercase.
        s2n_f660_auto = models.CharField(db_column='s2n_F660_auto', max_length=-1)  # Field name made lowercase.
        f660_petro = models.CharField(db_column='F660_petro', max_length=-1)  # Field name made lowercase.
        ef660_petro = models.CharField(db_column='eF660_petro', max_length=-1)  # Field name made lowercase.
        s2n_f660_petro = models.CharField(db_column='s2n_F660_petro', max_length=-1)  # Field name made lowercase.
        f660_aper = models.CharField(db_column='F660_aper', max_length=-1)  # Field name made lowercase.
        ef660_aper = models.CharField(db_column='eF660_aper', max_length=-1)  # Field name made lowercase.
        s2n_f660_aper = models.CharField(db_column='s2n_F660_aper', max_length=-1)  # Field name made lowercase.
        i_auto = models.CharField(max_length=-1)
        ei_auto = models.CharField(max_length=-1)
        s2n_i_auto = models.CharField(max_length=-1)
        i_petro = models.CharField(max_length=-1)
        ei_petro = models.CharField(max_length=-1)
        s2n_i_petro = models.CharField(max_length=-1)
        i_aper = models.CharField(max_length=-1)
        ei_aper = models.CharField(max_length=-1)
        s2n_i_aper = models.CharField(max_length=-1)
        f861_auto = models.CharField(db_column='F861_auto', max_length=-1)  # Field name made lowercase.
        ef861_auto = models.CharField(db_column='eF861_auto', max_length=-1)  # Field name made lowercase.
        s2n_f861_auto = models.CharField(db_column='s2n_F861_auto', max_length=-1)  # Field name made lowercase.
        f861_petro = models.CharField(db_column='F861_petro', max_length=-1)  # Field name made lowercase.
        ef861_petro = models.CharField(db_column='eF861_petro', max_length=-1)  # Field name made lowercase.
        s2n_f861_petro = models.CharField(db_column='s2n_F861_petro', max_length=-1)  # Field name made lowercase.
        f861_aper = models.CharField(db_column='F861_aper', max_length=-1)  # Field name made lowercase.
        ef861_aper = models.CharField(db_column='eF861_aper', max_length=-1)  # Field name made lowercase.
        s2n_f861_aper = models.CharField(db_column='s2n_F861_aper', max_length=-1)  # Field name made lowercase.
        z_auto = models.CharField(max_length=-1)
        ez_auto = models.CharField(max_length=-1)
        s2n_z_auto = models.CharField(max_length=-1)
        z_petro = models.CharField(max_length=-1)
        ez_petro = models.CharField(max_length=-1)
        s2n_z_petro = models.CharField(max_length=-1)
        z_aper = models.CharField(max_length=-1)
        ez_aper = models.CharField(max_length=-1)
        s2n_z_aper = models.CharField(max_length=-1)

        class Meta:
            managed = False
            db_table = name

    return CustomModel

## Saved Objects
class Saved(models.Model):
    num = models.AutoField(db_column='Num', primary_key=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=200)  # Field name made lowercase.
    ra = models.CharField(db_column='RA', max_length=200)  # Field name made lowercase.
    dec = models.CharField(db_column='Dec', max_length=200)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Saved'
        unique_together = (('num', 'id'),)

## Tabela de centros
class Ref(models.Model):
    pid = models.CharField(db_column='PID', max_length=200)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200)  # Field name made lowercase.
    ra = models.CharField(db_column='RA', max_length=200)  # Field name made lowercase.
    dec = models.CharField(db_column='DEC', max_length=200)  # Field name made lowercase.
    epoc = models.CharField(db_column='EPOC', max_length=200)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ref'
