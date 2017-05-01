from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

#to remove redundancy batches have been termed to a seperate table.. represents computer science or electronics
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.course_name
#same case as the s6c.. reperesents s6c or s6d
class Batch(models.Model):
    cbname = models.CharField(max_length=15)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    cbid = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.cbname


#users base details
class User(models.Model):
    name = models.CharField(max_length=20)
    adm_no = models.IntegerField(primary_key=True)#its selected as primary key as selected audience is students and teachers.. hereby we can eliminate multiple accounts
    phone_no = models.IntegerField()
    cbid = models.ForeignKey(Batch, on_delete=models.CASCADE)#foreign key to batch.. etc s6c
    password = models.CharField(max_length = 100)#must be hashed using MD5
    isadmin = models.IntegerField(default=0)#used to verify if its admin

    def __str__(self):
        return self.name
