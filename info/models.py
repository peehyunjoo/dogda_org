from django.db import models

# Create your models here.
import datetime

class member(models.Model):
    idx = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    reg_date = models.DateField()

    def __str__(self):
        return self.id

class admin_member(models.Model):
    idx = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=11)
    level = models.CharField(max_length=1)
    reg_date = models.DateField()

    def __str__(self):
        return self.id

class notice(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.idx + self.title

class dogda_info(models.Model):
    idx = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    dogda_name = models.CharField(max_length=20)
    dogda_birth = models.CharField(max_length=8)
    dogda_gender = models.CharField(max_length=1)
    dogda_type = models.CharField(max_length=20)
    reg_date = models.DateField()

    class Meta:
        unique_together = ('id', 'dogda_name')

    def __str__(self):
        return self.id+ self.dogda_name+self.dogda_birth

class dogda_vaccination_info(models.Model):
    idx = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    dogda_name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    vaccination_date = models.CharField(max_length=8)
    reg_date = models.DateField()

    class Meta:
        unique_together = ('id', 'dogda_name','type','vaccination_date')

    def __str__(self):
        return self.id+self.dogda_name+self.type+self.vaccination_date

class diary(models.Model):
    idx = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    dogda_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateField()
    flowers = models.CharField(max_length=8)

    def __str__(self):
        return self.id+self.dogda_name+self.title+self.content+self.flowers+self.reg_date

# Create your models here.
