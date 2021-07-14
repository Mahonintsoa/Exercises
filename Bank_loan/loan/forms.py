from django import forms

class ApprovalForm(forms.Form):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    dependents = forms.IntegerField()
    applicant_income = forms.IntegerField()
    co_applicant_income = forms.IntegerField()
    loan_term = forms.IntegerField()
    loan_amt = forms.IntegerField()
    credit_history = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
    married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No','No')])
    education = forms.ChoiceField(choices=[('Graduate','Graduate'), ('Not_Graduate', 'Not_Graduate')])
    self_employed = forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
    property_area = forms.ChoiceField(choices=[('Rural','Rural'),('Semiurban','Semiurban'),('Urban','Urban')])