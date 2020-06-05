from realstateapp.models import *

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
			'for':x.Property_status}
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
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages,
		'for':x.Property_status
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt


def GetPropertyData(pid):
	obj=PropertyData.objects.filter(Property_ID=pid)
	dic={}
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
		'pricepersqft':str(float(x.Property_Price)/float(x.Property_Area))
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		lt=[]
		for y in obj1:
			lt.append(y.Property_Image.url)
		dic.update({'image':lt})
		for y in obj1:
			dic.update({'coverimage':y.Property_Image.url})
			break
	return dic


def getagentinfo(agent_id):
	dic={}
	obj=agent_account.objects.filter(agent_id=agent_id)
	for i in obj:
		dic={
			'name':i.name,
			'email': i.email,
			'address':i.address,
			'city':i.city,
			'phone': i.phone,
			'pic': i.agentpic.url
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
			'userpic':x.userpic.url,

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
			'userpic':x.userpic.url,
			
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
			'pic':x.agentpic.url,
		}
		break
	return dic

def allPropertyDataforproperty():
	obj=PropertyData.objects.all()
	dic={}
	lt=[]
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
		'for':x.Property_status
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt


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
