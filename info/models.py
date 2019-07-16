from django.db import models
import datetime

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
    content = models.TextField()

    def __str__(self):
        return self.title+self.content

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
    flowers = models.CharField(max_length=8, default='', blank=True)       #null=True로하면 return시 not "NoneType" 에러 나므로 null=True는 사용 하지않는다.


    def __str__(self):
        return self.id + self.dogda_name + self.title + self.content+self.flowers+str(self.reg_date)


# Create your models here.
