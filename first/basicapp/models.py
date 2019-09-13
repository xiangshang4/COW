from django.db import models
from django.utils import timezone
# option value
appType_choices = [
('Current Account','Current Account'),
('Time Deposit','Time Deposit'),
('High Yield Demand Deposit Account','High Yield Demand Deposit Account'),
]
curr_choices=[
('USD','USD'),
('JPY','JPY'),
('SGD','SGD'),
('CNY','CNY'),
]
type_biz_choice=[
('Private Limited/Public Company',' Private Limited/Public Company'),
('Representative Office (IE)',' Representative Office (IE)'),
('Sole Proprietorship',' Sole Proprietorship'),
('Partnership / Joint Venture',' Partnership / Joint Venture'),
('Branch',' Branch'),
('Others',r'Association / Club / Society / Trusts/ Estate / Others'),
]
#Model
class Open_Acc_App(models.Model):
    date=models.DateField(default=timezone.now)
    type_of_application=models.CharField(max_length=256,choices=appType_choices)
    currency=models.CharField(max_length=256,choices=curr_choices)
    registered_name=models.CharField(max_length=256)
    bank_account_name=models.CharField(max_length=256)
    registered_address=models.CharField(max_length=256)
    mailing_address=models.CharField(max_length=256)
    nature_of_business=models.CharField(max_length=256)
    telephone_No=models.IntegerField()
    business_registration_No=models.CharField(max_length=256) #Numerical?
    place_of_incorporation=models.CharField(max_length=256)
    paidup_capital=models.CharField(max_length=256)
    date_of_incorporation=models.DateField()
    number_of_staff=models.IntegerField()
    type_of_business=models.CharField(max_length=256, choices=type_biz_choice)
