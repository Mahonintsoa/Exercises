from django.db import models

# Create your models here.
class Approvals(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    GRADUATED_CHOICES = (
        ('Graduate', 'Graduated'),
        ('Not_Graduate', 'Not_Graduated')
    )
    SELF_EMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )


    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dependants = models.IntegerField(default=0)
    applicant_income = models.IntegerField(default=0)
    co_applicant_income = models.IntegerField(default=0)
    loan_amt = models.IntegerField(default=0)
    loan_term = models.IntegerField(default=0)
    credit_history = models.IntegerField(default=0)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    education = models.CharField(max_length=26, choices= GRADUATED_CHOICES)
    self_employed = models.CharField(max_length=15, choices = SELF_EMPLOYED_CHOICES)
    property_area = models.CharField(max_length=15, choices= PROPERTY_CHOICES)



    def __str__(self):
        return self.firstname