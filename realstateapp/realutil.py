from realstateapp.models import *

def popup(request):
	try:
		if 8==request.session['pop']:
			return 8
		else:
			return 0
	except:
		return 0

	




def GetPropertyID():
	obj=PropertyData.objects.all()
	lt=[]
	dic={}
	for x in obj:
		dic={'ID':x.Property_ID,
			'Name':x.Property_Name}
		lt.append(dic)
	return lt
def GetPropertyName(pid):
	obj=PropertyData.objects.filter(Property_ID=pid)
	n=''
	for x in obj:
		n=x.Property_Name
	return n
def GetPropertyImageCount(pid):
	obj=PropertyImagesData.objects.filter(Property_ID=pid)
	count=0
	for x in obj:
		count=count+1
	return str(count)
def GetPropertyVideoCount(pid):
	obj=PropertyVideo.objects.filter(Property_ID=pid)
	count=0
	for x in obj:
		count=count+1
	return str(count)
def GetPropertyImageData():
	obj=PropertyImagesData.objects.all()
	lt=[]
	dic={}
	pid=[]
	pname=[]
	pcount=[]
	for x in obj:
		pid.append(x.Property_ID)
	for x in obj:
		pname.append(GetPropertyName(x.Property_ID))
	for x in obj:
		pcount.append(GetPropertyImageCount(x.Property_ID))
		
	pid=list(set(pid))
	pname=list(set(pname))
	pcount=list(set(pcount))
	for (a,b,c) in zip(pid,pname,pcount):
		dic={'property_id':a,
			'property_name':b,
			'image_count':c}
		lt.append(dic)
	return lt

def GetPropertyVideoData():
	obj=PropertyVideo.objects.all()
	lt=[]
	dic={}
	pid=[]
	pname=[]
	pcount=[]
	for x in obj:
		pid.append(x.Property_ID)
	for x in obj:
		pname.append(GetPropertyName(x.Property_ID))
	for x in obj:
		pcount.append(GetPropertyVideoCount(x.Property_ID))
		
	pid=list(set(pid))
	pname=list(set(pname))
	pcount=list(set(pcount))
	for (a,b,c) in zip(pid,pname,pcount):
		dic={'property_id':a,
			'property_name':b,
			'video_count':c}
		lt.append(dic)
	return lt
def GetPropertyCategoryData():
	obj=PropertyCategoryData.objects.all()
	dic={}
	lt=[]
	for x in obj:
		dic={'cid':x.Category_ID,
			'cname':x.Category_Name,
			'cimage':x.Category_Image.url}
		lt.append(dic)
	return lt


def GetAllPropertyData():
	obj=PropertyData.objects.all()
	dic={}
	lt=[]
	for x in obj:
		dic={'pid':x.Property_ID,
			'pname':x.Property_Name,
			'pprice':x.Property_Price,
			'pcategory':x.Property_Category,
			'pyear':x.Property_BuiltYear,
			'for':x.Property_status,
			'location':x.Property_location}
		lt.append(dic)
	return lt

def getuserinfo(user_id):
	dic={}
	obj=user_account.objects.filter(user_id=user_id)
	for i in obj:
		dic={
			'name': i.name
		}
		break
	return dic

def GetPropertyThumbData(category):
	obj=PropertyData.objects.filter(Property_Category=category)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt


def GetPropertyData(request, pid):
	obj=PropertyData.objects.filter(Property_ID=pid)
	dic={}
	try:
		if agent_account.objects.filter(agent_id = request.session['agent_id']):
			for x in obj:
				dic={
				'id':x.Property_ID,
				'name':x.Property_Name,
				'price':x.Property_Price,
				'about':x.Property_About,
				'address':x.Property_Address,
				'area':x.Property_Area,
				'across':x.Property_across,
				'beds':x.Property_Beds,
				'baths':x.Property_Baths,
				'garages':x.Property_Garages,
				'category':x.Property_Category,
				'builtyear':x.Property_BuiltYear,
				'for':x.Property_status,
				'location':x.Property_location,
				'pricepersqft':str(float(x.Property_Price)/float(x.Property_Area)),
				}
				obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
				obj2=PropertyVideo.objects.filter(Property_ID=x.Property_ID)
				lt=[]
				lt2=[]
				for y in obj1:
					lt.append(y.Property_Image.url)
				dic.update({'image':lt})
				for y2 in obj2:
					lt2.append(y2.property_video)
				dic.update({'video':lt2})
				for y in obj1:
					dic.update({'coverimage':y.Property_Image.url})
					break
			return dic
	except:
		for x in obj:
			dic={
			'id':x.Property_ID,
			'name':x.Property_Name,
			'price':x.Property_Price,
			'about':x.Property_About,
			'address':x.Property_Address,
			'area':x.Property_Area,
			'beds':x.Property_Beds,
			'baths':x.Property_Baths,
			'garages':x.Property_Garages,
			'category':x.Property_Category,
			'builtyear':x.Property_BuiltYear,
			'for':x.Property_status,
			'location':x.Property_location,
			'pricepersqft':str(float(x.Property_Price)/float(x.Property_Area)),
			}
			obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
			obj2=PropertyVideo.objects.filter(Property_ID=x.Property_ID)
			lt=[]
			lt2=[]
			for y in obj1:
				lt.append(y.Property_Image.url)
			dic.update({'image':lt})
			for y2 in obj2:
				lt2.append(y2.property_video)
			dic.update({'video':lt2})
			for y in obj1:
				dic.update({'coverimage':y.Property_Image.url})
				break
			return dic


def getagentinfo(agent_id):
	dic={}
	obj=agent_account.objects.filter(agent_id=agent_id)
	for i in obj:
		dic={
			'agentid':i.agent_id,
			'name':i.name,
			'email': i.email,
			'address':i.address,
			'city':i.city,
			'phone': i.phone,
			'aadharno':i.aadhar,
			'aadhar': i.agentpic.url,
			'pic':i.agentpic_is_aadharcard.url,
			'post':i.Post
		}
		break
	return dic
def getblogs(agent_id):
	dic={}
	lt=[]
	lt2=[]
	obj=blog_table.objects.filter(agent_id=agent_id)
	for i in obj:
		dic={
		'blog_no': i.blog_no,
		'pic_of_pro': i.pic_of_pro,
		'date': i.date,
		'subject': i.subject,
		'Desc': i.Desc
		}
		lt.append(dic)
	b=len(lt)-1
	for x in range(b,-1,-1):
		lt2.append(lt[x])
	return lt2

def allblogs():
	dic={}
	lt=[]
	lt2=[]
	obj=blog_table.objects.all()
	for i in obj:
		dic={
		'blog_no': i.blog_no,
		'pic_of_pro': i.pic_of_pro.url,
		'date': i.date,
		'subject': i.subject,
		'Desc': i.Desc
		}
		lt.append(dic)
	b=len(lt)-1
	for x in range(b,-1,-1):
		lt2.append(lt[x])
	return lt2
	

def GetUserData(email):
	obj=user_account.objects.filter(email=email)
	dic={}
	for x in obj:
		dic={
			'userid':x.user_id,
			'name':x.name,
			'gender':x.gender,
			'email':x.email,
			'address':x.address,
			'city':x.city,
			'phone':x.phone,
			'pic':x.userpic.url,

		}
		break
	return dic

def GetUserData2(uid):
	obj=user_account.objects.filter(user_id=uid)
	dic={}
	for x in obj:
		dic={
			'userid':x.user_id,
			'name':x.name,
			'gender':x.gender,
			'email':x.email,
			'address':x.address,
			'city':x.city,
			'phone':x.phone,
			'pic':x.userpic.url,
			
		}
		break
	return dic

def GetagentData2(uid):
	obj=agent_account.objects.filter(agent_id=uid)
	dic={}
	for x in obj:
		dic={
			'userid':x.agent_id,
			'name':x.name,
			'gender':x.gender,
			'email':x.email,
			'address':x.address,
			'city':x.city,
			'phone':x.phone,
			'aadhar':x.agentpic.url,
			'pic':x.agentpic_is_aadharcard.url,

		}
		break
	return dic

def GetagentData3(uid):
	dic1={}
	lt=[]
	obj=agent_account.objects.filter(agent_id=uid)
	dic={}
	for x in obj:
		dic={
			'userid':x.agent_id,
			'name':x.name,
			'gender':x.gender,
			'email':x.email,
			'address':x.address,
			'city':x.city,
			'phone':x.phone,
			'aadhar':x.agentpic.url,
			'pic':x.agentpic_is_aadharcard.url,
			'Aadharno':x.aadhar,
			'fb':x.facebook,
			'tw':x.twitter,
			'ln':x.linkedin,
			'status':x.status,
			'post':x.Post
		}
		break
	sub=bankaccount.objects.filter(agent_id=uid)
	for i in sub:
		dic.update({
			'accountholder':i.accountholdername,
			'checkpic':i.checkpic.url,
			'bankname':i.bankname,
			'accountnumber':i.accountno,
			'ifsc':i.IFSC
			})
	od=OrderData.objects.filter(Buyer_ID=uid)
	for i in od:
		dic1={
			'Order_ID':i.Order_ID,
			'Order_Date':i.Order_Date,
			'Property_ID':i.Property_ID,
			'Property_Name':i.Property_Name,
			'Buyer_ID':i.Buyer_ID,
			'Payment_ID':i.Payment_ID,
			'Order_Status':i.Order_Status,
			'Total_Amount':i.Total_Amount,
			'Amount_to_Pay':i.Amount_to_Pay
		}
		pt=PropertyImagesData.objects.filter(Property_ID=i.Property_ID)
		for j in pt:
			dic1.update({'image':j.Property_Image.url})
		lt.append(dic1)

	 
	dic.update({'od':lt})

	return dic
##################################search bar#######################################
def allPropertyDataforproperty(request):
	obj=PropertyData.objects.all()
	dic={}
	lt=[]
	try:
		if agent_account.objects.filter(agent_id= request.session['agent_id']):
			for x in obj:
				dic={
				'id':x.Property_ID,
				'name':x.Property_Name,
				'price':x.Property_Price,
				'address':x.Property_Address,
				'area':x.Property_Area,
				'across':x.Property_across,
				'beds':x.Property_Beds,
				'baths':x.Property_Baths,
				'garages':x.Property_Garages,
				'for':x.Property_status,
				'location':x.Property_location,
				}
				obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
				for y in obj1:
					dic.update({'image':y.Property_Image.url})
					break
				lt.append(dic)
			return lt
	except:
		for x in obj:
			dic={
			'id':x.Property_ID,
			'name':x.Property_Name,
			'price':x.Property_Price,
			'address':x.Property_Address,
			'area':x.Property_Area,
			'beds':x.Property_Beds,
			'baths':x.Property_Baths,
			'garages':x.Property_Garages,
			'for':x.Property_status,
			'location':x.Property_location,
			}
			obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
			for y in obj1:
				dic.update({'image':y.Property_Image.url})
				break
			lt.append(dic)
		return lt

def allPropertyDataforpropertyarea(area):
	obj=PropertyData.objects.filter(Property_Area=area)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

def allPropertyDataforpropertystatus(status):
	obj=PropertyData.objects.filter(Property_status=status)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt


def allPropertyDataforpropertyloaction(loaction):
	obj=PropertyData.objects.filter(Property_location=loaction)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt
def allPropertyDataforpropertybedrooms(bedrooms):
	obj=PropertyData.objects.filter(Property_Beds=bedrooms)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt
def allPropertyDataforpropertybathrooms(bathrooms):
	obj=PropertyData.objects.filter(Property_Baths=bathrooms)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt
def allPropertyDataforpropertyprice(price):
	obj=PropertyData.objects.filter(Property_Price=price)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt


#########for TWO

def allPropertyDataforpropertyAS(area,status):
	obj=PropertyData.objects.filter(Property_Area=area,Property_status=status)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt
def allPropertyDataforpropertyAL(area,loaction):
	obj=PropertyData.objects.filter(Property_Area=area,Property_location=loaction)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

def allPropertyDataforpropertyAB(area,bedrooms):
	obj=PropertyData.objects.filter(Property_Area=area,Property_Beds=bedrooms)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt
def allPropertyDataforpropertyABA(area,bathrooms):
	obj=PropertyData.objects.filter(Property_Area=area,Property_Baths=bathrooms)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt
def allPropertyDataforpropertyAPR(area,price):
	obj=PropertyData.objects.filter(Property_Area=area,Property_Price=price)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt
###########TWO STATUS 


def allPropertyDataforpropertySL(status,loaction):
	obj=PropertyData.objects.filter(Property_status=status,Property_loaction=loaction)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

def allPropertyDataforpropertySBE(status,bedrooms):
	obj=PropertyData.objects.filter(Property_status=status,Property_Beds=bedrooms)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

def allPropertyDataforpropertySBA(status,bathrooms):
	obj=PropertyData.objects.filter(Property_status=status,Property_Baths=bathrooms)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

def allPropertyDataforpropertySPR(status,price):
	obj=PropertyData.objects.filter(Property_status=status,Property_Price=price)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

def allPropertyDataforpropertyall(area,status,loaction,bedrooms,bathrooms,price):
	obj=PropertyData.objects.filter(Property_Area=area,Property_location=loaction,Property_status=status,Property_Beds=bedrooms,Property_Baths=bathrooms,Property_Price=price)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

def allPropertyDataforpropertydiversion(CIR):
	obj=PropertyData.objects.filter(property_Diversion=CIR)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'across':x.Property_across,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status,
		'location':x.Property_location
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt


###################################################################################################################
def GetCartCount(request):
	try:
		try:
			obj=user_account.objects.filter(email=request.session['user_email'])
			userid=''
			for x in obj:
				userid=x.User_ID
			obj=OrderData.objects.filter(Buyer_ID=userid,Order_Status='Unpaid')
			return len(obj)
		except:
			obj=agent_account.objects.filter(email=request.session['agent_id'])
			userid=''
			for x in obj:
				userid=x.User_ID
			obj=OrderData.objects.filter(Buyer_ID=userid,Order_Status='Unpaid')
			return len(obj)

	except:
		return 0
#############################################################

import requests
def sendmsg(ph,msg):
	try:

		url = "https://www.fast2sms.com/dev/bulk"

		querystring = {"authorization":"pJFuR4e1ZXH7UgOsjdNkmoWwtCEqfYn5v0iS9aVGxKc6M83yThf5ZwkME37e8ODYcXiq0bNrzh4Jx2Pm","sender_id":"SHRIRA","message":msg,"language":"english","route":"p","numbers":ph}

		headers = {
    				'cache-control': "no-cache"
					}

		response = requests.request("GET", url, headers=headers, params=querystring)

		print(response.text)
	except:
		pass
