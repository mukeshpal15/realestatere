from django.db import models
from datetime import date
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'
class PropertyCategoryData(models.Model):
	Category_ID=models.CharField(max_length=100)
	Category_Name=models.CharField(max_length=50)
	Category_Image=models.ImageField(upload_to="categoryimages/")
	class Meta:
		db_table="PropertyCategoryData"

class PropertyData(models.Model):
	Property_ID=models.CharField(max_length=100)
	Property_Name=models.CharField(max_length=100)
	Property_About=models.CharField(max_length=1000)
	Property_Address=models.CharField(max_length=1000)
	Property_Area=models.CharField(max_length=1000)
	Property_Beds=models.CharField(max_length=50)
	Property_Baths=models.CharField(max_length=50)
	Property_Garages=models.CharField(max_length=50)
	Property_Price=models.CharField(max_length=50)
	Property_Category=models.CharField(max_length=100)
	Property_BuiltYear=models.CharField(max_length=50)
	Property_status=models.CharField(max_length=50, default='FOR SALE')
	Property_location=models.CharField(max_length=100)
	class Meta:
		db_table="PropertyData"

class PropertyImagesData(models.Model):
	Property_ID=models.CharField(max_length=100)
	Property_Image=models.ImageField(upload_to="propertyimages/")
	class Meta:
		db_table="PropertyImagesData"

class agent_account(models.Model):
	agent_id=models.CharField(max_length=20)
	name=models.CharField(max_length=40)
	gender=models.CharField(max_length=10)
	email=models.CharField(max_length=50)
	address=models.CharField(max_length=400)
	city=models.CharField(max_length=20)
	phone=models.CharField(max_length=15)
	aadhar=models.CharField(max_length=16)
	password=models.CharField(max_length=40)
	facebook=models.CharField(max_length=150, default='NA')
	twitter=models.CharField(max_length=150, default='NA')
	linkedin=models.CharField(max_length=150, default='NA')
	status = models.CharField(max_length=10)
	agentpic=models.ImageField(upload_to='agentpic')
	class Meta:
		db_table="agent_account"

class user_account(models.Model):
	user_id=models.CharField(max_length=20)
	name=models.CharField(max_length=40)
	gender=models.CharField(max_length=10)
	email=models.CharField(max_length=50)
	address=models.CharField(max_length=400)
	city=models.CharField(max_length=20)
	phone=models.CharField(max_length=15)
	password=models.CharField(max_length=40)
	userpic=models.ImageField(upload_to="userpic/" ,blank=True)
	class Meta:
		db_table="user_account"

class myaccount(models.Model):
	name = models.CharField(max_length=10)
	pic = models.ImageField(upload_to='pic')
	class Meta:
		db_table="myaccount"

class blog_table(models.Model):
	agent_id = models.CharField(max_length=20)
	blog_no = models.CharField(max_length=50)
	pic_of_pro =models.ImageField(upload_to='blog_pic')
	date = models.DateField(auto_now=True)
	subject = models.CharField(max_length=60)
	Desc = models.CharField(max_length=200)
	class Meta:
		db_table="blog_table"
	

class OrderData(models.Model):
	Order_ID=models.CharField(max_length=100)
	Order_Date=models.DateField(auto_now=True)
	Property_ID=models.CharField(max_length=100)
	Property_Name=models.CharField(max_length=100)
	Buyer_ID=models.CharField(max_length=100)
	Payment_ID=models.CharField(max_length=100, blank=True)
	Order_Status=models.CharField(max_length=100)
	Total_Amount=models.CharField(max_length=100)
	Amount_to_Pay=models.CharField(max_length=100)
	class Meta:
		db_table="OrderData"

class CartData(models.Model):
	Cart_ID=models.CharField(max_length=100)
	Order_ID=models.CharField(max_length=50)
	Email=models.CharField(max_length=100)
	Buyer_ID=models.CharField(max_length=100)
	class Meta:
		db_table="CartData"		
			
