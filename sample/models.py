from django.db import models

class Sample(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        db_table="sample_table"

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.username

    def get_user(self):
        return {"username":self.username,"password":self.password}



    class Meta:
        db_table="users"