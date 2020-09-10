from django.db import models
from datetime import datetime, date
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'
class PropertyCategoryData(models.Model):
	Category_ID=models.CharField(max_length=100)
	Category_Name=models.CharField(max_length=50)
	Category_Image=models.ImageField(upload_to="categoryimages/")
	def __str__ (self):
		return self.Category_Name

	def delete(self, *args, **kwargs):
		self.Category_Image.delete()
		super().delete(*args, **kwargs)

class PropertyData(models.Model):
	Property_ID=models.CharField(max_length=100)
	Property_Name=models.CharField(max_length=100)
	Property_About=models.CharField(max_length=1000)
	Property_Address=models.CharField(max_length=1000)
	Property_Area=models.CharField(max_length=1000, default='')
	Property_across=models.CharField(max_length=1000, default='')
	Property_Beds=models.CharField(max_length=50, default='NA')
	Property_Baths=models.CharField(max_length=50, default='NA')
	Property_Garages=models.CharField(max_length=50, default='NA')
	Property_Price=models.CharField(max_length=50)
	Property_Category=models.CharField(max_length=100)
	Property_Streat=models.CharField(max_length=50, default='NA')
	Property_Streat=models.CharField(max_length=50, default='NA')
	Property_Direction=models.CharField(max_length=100)
	property_Facility= models.TextField()
	property_Diversion=models.CharField(max_length=100)
	Property_BuiltYear=models.CharField(max_length=50, default='NA')
	Property_status=models.CharField(max_length=50, default='FOR SALE')
	Property_location=models.CharField(max_length=100)
	def __str__ (self):
		return self.Property_Name

class PropertyImagesData(models.Model):
	Property_ID=models.CharField(max_length=100)
	Property_Image=models.ImageField(upload_to="propertyimages/")	
	def __str__ (self):
		return self.Property_ID

	def delete(self, *args, **kwargs):
		self.Property_Image.delete()
		super().delete(*args, **kwargs)


class PropertyVideo(models.Model):
	Property_ID=models.CharField(max_length=100)
	Video_image=models.ImageField(upload_to='video_pic/', default='', blank=True)
	property_video=models.FileField(upload_to="property_video/", default='', blank=True)
	def __str__ (self):
		return self.Property_ID

	def delete(self, *args, **kwargs):
		self.property_video.delete()
		super().delete(*args, **kwargs)
		

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
	Post=models.CharField(max_length=50, default='Normal')
	facebook=models.CharField(max_length=150, default='NA')
	twitter=models.CharField(max_length=150, default='NA')
	linkedin=models.CharField(max_length=150, default='NA')
	status = models.CharField(max_length=10)
	agentpic=models.ImageField(upload_to='agentpic')
	agentpic_is_aadharcard=models.ImageField(upload_to='profileid/',default='profilepic/image.png')
	def __str__ (self):
		return self.agent_id

class bankaccount(models.Model):
	agent_id=models.CharField(max_length=100, default='NA')
	accountholdername=models.CharField(max_length=100, default='NA')
	checkpic=models.ImageField(upload_to="checkbookpics/", default='checkbookpics/WhatsApp_Image_2020-02-17_at_21.14.44.jpeg')
	bankname=models.CharField(max_length=100, default='NA')
	accountno=models.CharField(max_length=100, default='NA')
	IFSC=models.CharField(max_length=100, default='NA')
	def __str__ (self):
		return self.agent_id
		

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
	def __str__ (self):
		return self.user_id

class myaccount(models.Model):
	name = models.CharField(max_length=10)
	pic = models.ImageField(upload_to='pic')
	def __str__ (self):
		return self.name

class blog_table(models.Model):
	agent_id = models.CharField(max_length=20)
	blog_no = models.CharField(max_length=50)
	pic_of_pro =models.ImageField(upload_to='blog_pic')
	date = models.DateField(auto_now=True)
	subject = models.CharField(max_length=60, default='')
	Desc = models.TextField()
	def __str__ (self):
		return self.subject

	def delete(self, *args, **kwargs):
		self.pic_of_pro.delete()
		super().delete(*args, **kwargs)
	

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
	def __str__ (self):
		return self.Order_ID

class CartData(models.Model):
	Cart_ID=models.CharField(max_length=100)
	Order_ID=models.CharField(max_length=50)
	Email=models.CharField(max_length=100)
	Buyer_ID=models.CharField(max_length=100)
	def __str__ (self):
		return self.Buyer_ID	
			

class mapapproval(models.Model):
	date=models.DateTimeField()
	Property_ID=models.CharField(max_length=100)
	Buyer_ID=models.CharField(max_length=100)
	Land_Paper=models.FileField(upload_to="map_approval/")
	Map_by_engineer=models.ImageField(upload_to="map_by_engineer/") 
	Copy_of_Tax=models.FileField(upload_to="map_approval/")
	other_details=models.TextField(default='')
	map_approved=models.ImageField(upload_to="aproved_map/", default='')
	def __str__ (self):
		return self.Buyer_ID


class Loandetails(models.Model):
	date = models.DateField(auto_now=True)
	loan_id=models.CharField(max_length=100)
	Loan_Type=models.CharField(max_length=100)
	Name=models.CharField(max_length=100)
	Email_ID=models.CharField(max_length=100)
	Phone=models.CharField(max_length=100)
	City=models.CharField(max_length=100)
	State=models.CharField(max_length=100)
	DOB=models.CharField(max_length=100)
	employee=models.CharField(max_length=100)
	Income=models.CharField(max_length=100)
	Loan_Required=models.CharField(max_length=100)
	def __str__ (self):
		return self.loan_id

		
class bannerimage(models.Model):
	image=models.ImageField(upload_to="bannerimg/")
	offer=models.ImageField(upload_to="offer/", default='')
	class Meta:
		db_table="bannerimage"		

class foroffer(models.Model):
	datetime = models.DateTimeField(auto_now=True)
	Email_ID=models.CharField(max_length=100)
	def __str__ (self):
		return self.Email_ID


class documents(models.Model):
	Doc_ID=models.CharField(max_length=100)
	title=models.CharField(max_length=100)
	file=models.FileField(upload_to="documents/")

	def __str__ (self):
		return self.title

	def delete(self, *args, **kwargs):
		self.file.delete()
		super().delete(*args, **kwargs)

			


class admind(models.Model):
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	position=models.CharField(max_length=100, default='',blank=True)
	def __str__ (self):
		return self.email
		

class Testimonialdate(models.Model):
	TestID=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	img=models.ImageField(upload_to="testimonialimg/")
	feedback=models.TextField(default='')
	def __str__ (self):
		return self.name

	def delete(self, *args, **kwargs):
		self.img.delete()
		super().delete(*args, **kwargs)
		