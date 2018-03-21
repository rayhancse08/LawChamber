from django.db import models


class AboutUs(models.Model):
    titles=models.CharField(max_length=200)
    body=models.TextField()

class Contact(models.Model):
    address=models.TextField()
    phoneNumber=models.CharField(max_length=200)
    email=models.EmailField()

class Bank(models.Model):
    name=models.CharField(max_length=200,help_text="Enter a Bank name (e.g. Brack,DutchBangla)")

    def __str__(self):
        return self.name

class Branch(models.Model):
    bank=models.ForeignKey('Bank', on_delete=models.SET_NULL, null=True)
    name=models.CharField("Branch Name",max_length=200,help_text="Enter branch name")
    address=models.CharField("Branch Address",max_length=200,help_text="Enter branch address")

    def __str__(self):
        return self.name





class File(models.Model):
    name=models.CharField("File Name",max_length=200,help_text="Enter File Name")
    bill=models.CharField("Bill Amount",max_length=200,help_text="Enter Bill Amount")
    bank=models.ForeignKey('Bank', on_delete=models.SET_NULL, null=True)
    branch=models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True)
    account_no=models.CharField("Account No",max_length=200,help_text="Enter Account No")



    def __str__(self):
        return self.name

class Doc(models.Model):
    file=models.ForeignKey('File', on_delete=models.SET_NULL, null=True)
    name=models.CharField("Doc Name",max_length=200,help_text="Enter Doc Name")
    doc = models.FileField(default=False, help_text="Upload Doc")

    def __str__(self):
        return self.name