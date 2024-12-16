from django import forms

from p2.models import *

class BankCustomerForm(forms.Form):
   creditscore = forms.CharField(help_text="Enter CreditScore")

   geography_choices = (('France', 'France'), ('Spain', 'Spain'), ('Germany', 'Germany'))
   geography_choice = forms.ChoiceField(choices=geography_choices)
   
   gender_choices = (('Female', 'Female'), ('Male', 'Male'))
   gender_choice = forms.ChoiceField(choices=gender_choices)

   age = forms.CharField(help_text="Enter Age")
   tenure = forms.CharField(help_text="Enter Tenure")
   balance = forms.CharField(help_text="Enter Balance")
   num_products = forms.CharField(help_text="Enter NumOfProducts")
   has_card = forms.CharField(help_text="Enter HasCrCard (1 or 0)")
   is_active_member = forms.CharField(help_text="Enter IsActiveMember (1 or 0)")
   estimated_salary = forms.CharField(help_text="Enter EstimatedSalary")
   complain = forms.CharField(help_text="Enter Complain")
   satisfaction_score = forms.CharField(help_text="Enter Satisfaction Score")


   card_type_choices = (('DIAMOND', 'DIAMOND'), ('GOLD', 'GOLD'), ('SILVER', 'SILVER'), ('PLATINUM', 'PLATINUM') )   
   card_type_choice = forms.ChoiceField(choices=card_type_choices)
   
