from django.core.paginator import *
from django.shortcuts import render, redirect
from django.conf import  settings
from realstateapp.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import *
from realstateapp.form import *
from realstateapp.models import *
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
import uuid
import string
from realstateapp.realutil import *
import json
import urllib

def demo(request):
	return render(request,'demo.html',{})
def error(request):
	#obj=PropertyData.objects.all().delete()
	#obj=PropertyImagesData.objects.all().delete()
	return render(request,'Error.html',{})

def index(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	blogs=allblogs()[0:3]
	try:
		try:	
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs})
				return render(request, 'index.html',dic)
			else:
				b=1
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs})
				return render(request, 'index.html',dic)
			
		except:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs})
				return render(request, 'index.html',dic)
			else:
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs})
				return render(request, 'index.html',dic)
	
	except Exception:
		dic={'obj':obj,'b':b, 'h':h}
		dic.update({'cdata':GetPropertyCategoryData()})
		dic.update({'blogs':blogs})
		return render(request, 'index.html',dic)


		
	
def properties(request):
	b=0
	h=0
	qs=allPropertyDataforproperty()
	LA=request.GET.get('area')
	PS=request.GET.get('status')
	PR=request.GET.get('range')

	try:


		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'properties.html',{'obj': qs, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'properties.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'properties.html',{'obj': qs, 'b':b, 'h':h})
			else:
				return render(request, 'properties.html',{'obj': qs})
	except Exception:
		return render(request, 'properties.html',{'obj': qs})	

def blog(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	dic=allblogs()
	try:	
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'blog.html',{'obj': obj, 'b':b, 'h':h,'elt':dic})
			else:
				b=1
				return render(request, 'blog.html',{'obj': obj, 'elt':dic})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'blog.html',{'obj': obj, 'b':b, 'h':h, 'elt':dic})
			else:
				return render(request, 'blog.html',{'obj': obj, 'elt':dic})
	except Exception:
		
		return render(request, 'blog.html',{'obj': obj, 'elt':dic})

def about(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'about.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'about.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'about.html',{'obj': obj, 'b':b, 'h':h})
			else:
				return render(request, 'about.html',{'obj': obj,})
	except Exception:
		return render(request, 'about.html',{'obj': obj,})

def property_detail(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'property-details.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'property-details.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'property-details.html',{'obj': obj, 'b':b, 'h':h})
			else:
				return render(request, 'property-details.html',{'obj': obj,})
	except Exception:
		return render(request, 'property-details.html',{'obj': obj,'elt':allblogs()})

	
def contact(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'contact.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'contact.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'contact.html',{'obj': obj, 'b':b, 'h':h})
			else:
				return render(request, 'contact.html',{'obj': obj,})
	except Exception:
		return render(request, 'contact.html',{'obj': obj,})

	
def registration(request):

	return render(request, 'registration.html', {})
def login(request):
	return render(request, 'login.html', {})
def adminlogin(request):
	return render(request, 'adminlogin.html', {})
def agent_forgot_pass(request):
	return render(request, 'agentforget.html', {})
def userregistation(request):
	return render(request, 'userregistation.html',{})
def loginformuser(request):
	return render(request, 'userlogin.html',{})
def user_forgot_pass(request):
	return render(request, 'userforgot.html', {})
@csrf_exempt
def adminlogincheck(request):
	if request.method=="POST":
		e=request.POST.get('email')
		p=request.POST.get('pass')
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		if result['success']:
			if e=="admin@homespace.com" and p=="1234":
				request.session['user']=e
				return redirect('/adminpannel/')
			else:
				b1='''<script type="text/javascript">
				alert("'''
				b2='''");</script>'''
				alert=b1+'Login Failed'
				return render(request, 'adminlogin.html', {'alert':alert})
		else:
			return HttpResponse("<script> alert(' Recaptcha is invalid !!'); window.location.replace('/adminlogin/') </script>")
					
	else:
		return redirect('/error/')
def adminpannel(request):
	try:
		n=request.session['user']
		return render(request, 'adminpannel.html',{} )
	except:
		return redirect('/error/')

def Orderdetail(request):
	try:
		n=request.session['user']
		obj=OrderData.objects.filter(Order_Status='Unpaid')
		dic={'obj':obj}
		return render(request, 'orderdetails.html', dic)
	except:
		return redirect('/error/')
def adminlogout(request):
	n=request.session['user']
	del request.session['user']
	request.session.flush()
	return redirect('/index/')


@csrf_exempt
def agentdata(request):
	if request.method=="POST":
		s='active'
		u= 'not active'
		agent=agent_account.objects.filter(status=s)
		notagent=agent_account.objects.filter(status=u)
		return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
	else:
		return redirect('/error/')

@csrf_exempt
def make_active_agent(request):
	if request.method=="POST":
		s='active'
		u= 'not active'
		m= request.POST.get('set')
		try:
			if agent_account.objects.filter(agent_id=m):
				t=agent_account.objects.filter(agent_id=m)
				for i in t:
					i.status=s
					i.save()
				for i in t:
					e=i.email
					p=i.password
					break
				subject='Mail From Shri Raj Property'
				msg= ''' Dear Agent,

				You Account has been activated by the admin and
				Your account Password is:- '''+p+''' 

				Thanks & Regards
				Shri Raj Property''' 
						

				email = EmailMessage(subject, msg, to=[e])
				email.send()	
				agent=agent_account.objects.filter(status=s)
				notagent=agent_account.objects.filter(status=u)
				return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
		except Exception:
			agent=agent_account.objects.filter(status=s)
			notagent=agent_account.objects.filter(status=u)
			return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
@csrf_exempt
def make_deactive_agent(request):
	if request.method=="POST":
		s='active'
		u= 'not active'
		m= request.POST.get('set')
		try:
			if agent_account.objects.filter(agent_id=m):
				t=agent_account.objects.filter(agent_id=m)
				for i in t:
					i.status=u
					i.save()
				for i in t:
					e=i.email
					p=i.password
					break
				subject='Mail From Shri Raj Property'
				msg= ''' Dear Agent,

				Your account has been deavtivated by the Admin.
				For more information contact XXXXXX.

				Thanks & Regards
				Shri Raj Property''' 
						

				email = EmailMessage(subject, msg, to=[e])
				email.send()	
				agent=agent_account.objects.filter(status=s)
				notagent=agent_account.objects.filter(status=u)
				return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
		except Exception:
			agent=agent_account.objects.filter(status=s)
			notagent=agent_account.objects.filter(status=u)
			return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})

@csrf_exempt
def openaddproperty(request):
	if request.method=="POST":
		obj=PropertyCategoryData.objects.all()
		lt=[]
		for x in obj:
			lt.append(x.Category_Name)
		dic={'category':lt,
			'pdata':GetAllPropertyData()}
		return render(request, "addproperty.html",dic)
	else:
		return redirect('/error/')

@csrf_exempt
def delete_property(request):
	if request.method=="POST":
		n=request.session['user']
		n=request.POST.get('delete')
		if PropertyData.objects.filter(Property_ID=n):
			obj=PropertyData.objects.filter(Property_ID=n)
			for i in obj:
				i.delete()
			s=PropertyImagesData.objects.filter(Property_ID=n)
			for j in s:
				j.delete()
			return HttpResponse("<script> alert('Property Is Deleted .!!'); window.location.replace('/adminpannel/') </script>")

		else:
			return HttpResponse("<script> alert('Property Is Not Deleted .!!'); window.location.replace('/openaddpropertycategory/') </script>")
@csrf_exempt
def openaddpropertycategory(request):
	if request.method=="POST":
		return render(request, "addpropertycategory.html",{'cdata':GetPropertyCategoryData()})

@csrf_exempt
def savepropertycategory(request):
	if request.method=="POST":
		form=ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
				m=form.cleaned_data['image']
				p="C00"
				x=1
				pid=p+str(x)
				while PropertyCategoryData.objects.filter(Category_ID=pid).exists():
					x=x+1
					pid=p+str(x)
				x=int(x)
				n=request.POST.get('name')
				obj=PropertyCategoryData(
					Category_ID=pid,
					Category_Name=n,
					Category_Image=m,
					)
				obj.save()
				b1='''<script type="text/javascript">
				alert("'''
				b2='''");</script>'''
				alert=b1+'Saved'+b2
				return render(request, "addpropertycategory.html",{'alert':alert,'cdata':GetPropertyCategoryData()})

	else:
		return redirect('/error/')

@csrf_exempt
def saveproperty(request):
	if request.method=="POST":
		n=request.POST.get('name')
		a=request.POST.get('about')
		property_price=request.POST.get('price')
		c=request.POST.get('category')
		y=request.POST.get('builtyear')
		ad=request.POST.get('address')
		ar=request.POST.get('area')
		bd=request.POST.get('beds')
		bt=request.POST.get('baths')
		gr=request.POST.get('garages')
		f=request.POST.get('for')
		p="P00"
		x=1
		pid=p+str(x)
		while PropertyData.objects.filter(Property_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		obj=PropertyData(
			Property_ID=pid,
			Property_Name=n,
			Property_About=a,
			Property_Address=ad,
			Property_Area=ar,
			Property_Beds=bd,
			Property_Baths=bt,
			Property_Garages=gr,
			Property_Price=property_price,
			Property_Category=c,
			Property_BuiltYear=y,
			Property_status=f
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request, 'adminpannel.html', {'alert':alert,'pdata':GetAllPropertyData()})
	else:
		return redirect('/error/')
@csrf_exempt
def agent_signup(request):
	if request.method=="POST":
		
		n= request.POST.get('name')
		g= request.POST.get('gender')
		e= request.POST.get('email')
		ad= request.POST.get('address')
		c = request.POST.get('city')
		ph= request.POST.get('phone')
		aa=request.POST.get('aadhar')
		fb=request.POST.get('facebook')
		tw=request.POST.get('twitter')
		LI=request.POST.get('linkedin')
		m=request.FILES['pic']
		u= 'not active'
		status=u
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		if agent_account.objects.filter(email=e).exists():
			message= 'User Already Exist'
			return render(request,'registration.html',{'message':message})

		elif agent_account.objects.filter(phone=ph).exists():
			message= 'User Already Exist'
			return render(request,'registration.html', {'message':message})

		else:
			u='A00'
			x=1
			uid=u+str(x)
			while agent_account.objects.filter(agent_id=uid):
				x=x+1
				uid=u+str(x)
			x=int(x)
			try:
				if result['success']:
					subject='Mail From Shri Raj Property'
					msg= ''' Hello sir,

			You are successfully registered, but your account is not active
			please wait for the owner response 

			Thanks & Regards
			Shri Raj Property''' 
					

					email = EmailMessage(subject, msg, to=[e])
					email.send()

					try:
						sus='New Agent Register'

						mess= ''' Hello sir,
			This Person want to make your agent
			detail of the person is here

			''' "Name :"+n+ ('\n') +"Gender :"+g+ ('\n')+"email :"+e+ ('\n')+"Address :"+ad+ ('\n')+"City :"+c+('\n')+"Phone :"+ph+ ('\n')+"Aadhar No. :"+aa+ ('\n') +"Facebook Link :"+fb+ ('\n') +"Twitter Link :"+tw+ ('\n') +"LinkedIn Link :"+LI+'''

					Thanks & Regards
					Shri Raj Property''' 


						
						email = EmailMessage(sus, mess, to=['testm1214@gmail.com'])
						email.send()
						print('gooooo')
						sv=agent_account(agent_id=uid,
										name=n,
										gender=g,
										email=e,
										address=ad,
										city=c,
										phone=ph,
										aadhar=aa,
										password=p,
										facebook=fb,
										twitter=tw,
										linkedin=LI,
										status=status,
										agentpic=m
										 )
						sv.save()
						print('hello')
						message='You are successfully registered.'	
						return render(request,'registration.html', {'message':message})
					except Exception:
						message='Fill The Form Again'	
						return render(request,'registration.html', {'message':message})
				else:
					return HttpResponse("<script> alert(' Recaptcha is invalid !!'); window.location.replace('/registration/') </script>")

			except Exception:
				message=' Enter Valid Mail Address'
				return render(request,'registration.html', {'message':message})
	else:
		message=' Enter Valid Mail Address'
		return render(request,'registration.html', {'message':message})

def dele(request):
	obj=agent_account.objects.all()
	obj.delete()
	return render(request, 'index.html',{})


@csrf_exempt
def openaddpropertycategory(request):
	if request.method=="POST":
		return render(request, "addpropertycategory.html",{'cdata':GetPropertyCategoryData()})
	else:
		return redirect('/error/')

@csrf_exempt
def openaddpropertyimages(request):
	if request.method=="POST":
		dic={'propertyid':GetPropertyID(),
			'propertyimagedata':GetPropertyImageData()}
		return render(request, "addpropertyimages.html",dic)
	else:
		return redirect('/error/')

@csrf_exempt
def savepropertyimages(request):
	if request.method=="POST":
		n=request.POST.get('propertyid')
		form=ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			m=form.cleaned_data['image']
			obj=PropertyImagesData(
				Property_ID=n,
				Property_Image=m
				)
			obj.save()
			dic={'propertyid':GetPropertyID(),
				'propertyimagedata':GetPropertyImageData()}
			return render(request, "addpropertyimages.html",dic)
	else:
		return redirect('/error/')

@csrf_exempt
def openpropertycategory(request):
		category=request.GET.get('cname')
		request.session['cname'] = category
		page = request.GET.get('page')
		cdata=[]
		paginator = Paginator(GetPropertyThumbData(category), 15)
		try:
			cdata = paginator.page(page)
		except PageNotAnInteger:
			cdata = paginator.page(1)
		except EmptyPage:
			cdata = paginator.page(paginator.num_pages)
		dic={'cdata':cdata,
			'category':category}
		dic.update({'catedata':GetPropertyCategoryData()})
		return render(request,"propertycategories.html",dic)
def propertypaginator(request):
	page = request.GET.get('page')
	cdata=[]
	paginator = Paginator(GetPropertyThumbData(request.session['cname']), 15)
	try:
		cdata = paginator.page(page)
	except PageNotAnInteger:
		cdata = paginator.page(1)
	except EmptyPage:
		cdata = paginator.page(paginator.num_pages)
	dic={'cdata':cdata,
		'category':request.session['cname']}
	dic.update({'catedata':GetPropertyCategoryData()})
	return render(request,"propertycategories.html",dic)
def openmyaccount(request):
	return render(request,"myaccount.html",{})

def openchangeaccountdetails(request):
	try:
		uid=request.session['user_id']
		dic=GetUserData2(uid)
		return render(request,"changeaccountdetails.html",dic)
	except:
		uid=request.session['agent_id']
		dic=GetagentData2(uid)

		return render(request,"changeaccountdetails.html",dic)

@csrf_exempt
def savechangeaccountdetails(request):
	if request.method=="POST":
		try:
			uid=request.session['user_id']
			obj=user_account.objects.filter(user_id=uid)
			obj.update(address=request.POST.get('address'))
			obj.update(city=request.POST.get('city'))
			obj.update(phone=request.POST.get('phone'))
			try:
				c=request.FILES['pic']
				for i in obj:
					i.userpic=c
					i.save()
					break;
			except:
				pass
			dic=GetUserData2(uid)
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Saved successfully'+b2
			dic.update({'alert':alert})
			return redirect('/useraccount/')
		except:
			try:
				uid=request.session['agent_id']
				obj=agent_account.objects.filter(agent_id=uid)
				obj.update(address=request.POST.get('address'))
				obj.update(city=request.POST.get('city'))
				obj.update(phone=request.POST.get('phone'))
				try:
					c=request.FILES['pic']
					for i in obj:
						i.agentpic=c
						i.save()
						break;
				except:
					pass
				dic=GetUserData2(uid)
				b1='''<script type="text/javascript">
				alert("'''
				b2='''");</script>'''
				alert=b1+'Saved successfully'+b2
				dic.update({'alert':alert})
				dic=getagentinfo(request.session['agent_id'])
				dic.update({'blogs':getblogs(request.session['agent_id']),'alert':alert })
				return render(request, 'agentdesk.html', dic)
			except:
				return redirect('/error/')
			


def user_signup(request):
	if request.method=="POST":
		n= request.POST.get('name')
		g= request.POST.get('gender')
		e= request.POST.get('email')
		ad= request.POST.get('address')
		c = request.POST.get('city')
		ph= request.POST.get('phone')
		
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		if user_account.objects.filter(email=e).exists():
			message= 'User Already Exist'
			return render(request,'userregistation.html',{'message':message})

		elif user_account.objects.filter(phone=ph).exists():
			message= 'User Already Exist'
			return render(request,'userregistation.html', {'message':message})

		else:
			u='U00'
			x=1
			uid=u+str(x)
			while user_account.objects.filter(user_id=uid):
				x=x+1
				uid=u+str(x)
			x=int(x)
			try:
				subject='Mail From Shri Raj Property'
				msg= ''' Hello sir,

		You are successfully registered, 
		your password is :'''+p+''' 

		Thanks & Regards
		Shri Raj Property''' 
				
				if result['success']:
					email = EmailMessage(subject, msg, to=[e])
					email.send()
					sv=user_account(user_id=uid, name=n, gender=g, email=e, address=ad, city=c, phone=ph,password=p)
					sv.save()
					message='You are successfully registered. password is send to your given mail account'	
					return render(request,'userregistation.html', {'message':message})
				else:
					return HttpResponse("<script> alert(' Recaptcha is invalid !!'); window.location.replace('/userregistation/') </script>")
				
			except Exception:
				message='Enter Valid Mail Address'
				return render(request,'userregistation.html', {'message':message})
@csrf_exempt
def user_login(request):
	if request.method=="POST":
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		b=0
		h=0
		e=request.POST.get('email')
		p=request.POST.get('password')
		ua = user_account.objects.filter(email=e)
		if user_account.objects.filter(email=e, password=p).exists:
			for i in ua:
				c=i.user_id
				request.session['user_id']=c
				b=1
				break
		if request.session.has_key('user_id') and b==1: 
			if result['success']:
				h=1
				dic=GetUserData(e)
				return redirect('/useraccount/')
			else:
				return HttpResponse("<script> alert(' Recaptcha is invalid !!'); window.location.replace('/loginformuser/') </script>")


		else:
			message='Please Enter Valid Details'

			return render(request,'userlogin.html',{'message': message})
def useraccount(request):
	if user_account.objects.filter(user_id=request.session['user_id']).get():
		e=''
		h=1
		b=1
		n=request.session['user_id']
		ua = user_account.objects.filter(user_id=n)
		for i in ua:
			e=i.email
			break;

		dic=GetUserData(e)
		return render(request,"myaccount.html",dic)
	else:
		return redirect('/error/')


@csrf_exempt
def agent_login(request):

	b=0
	h=0
	s='active'
	e=request.POST.get('email')
	p=request.POST.get('pass')
	ua = agent_account.objects.filter(email=e)

	''' Begin reCAPTCHA validation '''
	recaptcha_response = request.POST.get('g-recaptcha-response')
	url = 'https://www.google.com/recaptcha/api/siteverify'
	values = {
	    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
	    'response': recaptcha_response
	}
	data = urllib.parse.urlencode(values).encode()
	req =  urllib.request.Request(url, data=data)
	response = urllib.request.urlopen(req)
	result = json.loads(response.read().decode())
	''' End reCAPTCHA validation '''
	if agent_account.objects.filter(email=e, password=p).exists():
		if agent_account.objects.filter(status=s).exists():
			for i in ua:
				c=i.agent_id
				request.session['agent_id']=c
				b=1
				break

		else:
			message='Your account is not activated'
			return render(request,'login.html',{'message': message})

		if request.session.has_key('agent_id') and b==1:
			if result['success']:
				h=1
				dic=getagentinfo(request.session['agent_id'])
				dic.update({'blogs':getblogs(request.session['agent_id'])})
				return render(request, 'agentdesk.html', dic)
			else:
				return HttpResponse("<script> alert(' Recaptcha is invalid !!'); window.location.replace('/login/') </script>")
	else:
		message='Please Enter valid details'
		return render(request,'login.html',{'message': message})

@csrf_exempt
def password_send_to_user(request):
	if request.method=="POST":
		e=request.POST.get('email')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		if result['success']:
			if user_account.objects.filter(email=e).exists():
				u=user_account.objects.filter(email=e)
				for i in u:
					i.password=p
					break
				subject='Mail From Shri Raj Property'
				msg= ''' Hello sir,

				Your passwaord has been changed, 
				your password is :'''+p+''' 

				Thanks & Regards
				Shri Raj Property''' 
						
				try:
					email = EmailMessage(subject, msg, to=[e])
					email.send()
					i.save()
					return HttpResponse("<script> alert('Hello User, Your password has been sent to your registered Email. If you have not received the password, go to the contact page and send an email. Will be processed within 24 hours !!'); window.location.replace('/loginformuser/') </script>")
				except Exception:
					return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/user_forgot_pass/') </script>")
			else:
				return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/user_forgot_pass/') </script>")

		else:
			return HttpResponse("<script> alert(' Recaptcha is invalid !!'); window.location.replace('/user_forgot_pass/') </script>")


@csrf_exempt
def password_send_to_agent(request):
	if request.method=="POST":
		e=request.POST.get('email')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
		    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		    'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode()
		req =  urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		result = json.loads(response.read().decode())
		''' End reCAPTCHA validation '''
		if result['success']:
			if agent_account.objects.filter(email=e).exists():
				u=agent_account.objects.filter(email=e)
				for i in u:
					i.password=p
					break
				subject='Mail From Shri Raj Property'
				msg= ''' Hello sir,

				Your passwaord has been changed, 
				your password is :'''+p+''' 

				Thanks & Regards
				Shri Raj Property''' 
						
				try:
					email = EmailMessage(subject, msg, to=[e])
					email.send()
					i.save()
					return HttpResponse("<script> alert('Hello Agent, Your password has been sent to your registered Email. If you have not received the password, go to the contact page and send an email. Will be processed within 24 hours !!'); window.location.replace('/login/') </script>")
				except Exception:
					return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/agent_forgot_pass/') </script>")
			else:
				return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/agent_forgot_pass/') </script>")
		else:
			return HttpResponse("<script> alert(' Recaptcha is invalid !!'); window.location.replace('/agent_forgot_pass/') </script>")




def send_mail_by_contact(request):
	if request.method=="POST":
		n= request.POST.get('name')
		e= request.POST.get('email')
		ph=request.POST.get('number')
		s= request.POST.get('subject')
		m= request.POST.get('message')
		subject='Mail From Shri Raj Property'

		msg= ''' Hello sir,

	Someone contact you, 
	details are given below 
'''+"Name :" +n+('\n')+"Mail ID :"+e+('\n')+"Phone Number :"+ph+('\n')+"Subject :"+s+('\n')+"Message :"+m+'''

	Thanks & Regards
	Shri Raj Property''' 

		email = EmailMessage(subject, msg, to=['testm1214@gmail.com'])
		email.send()
		return HttpResponse("<script> alert('Thanks for investing your precious Time here. You will get the response very soon  !!'); window.location.replace('/contact/') </script>")

def openmyaccount(request):
	return render(request,"myaccount.html",{})





@csrf_exempt
def Log(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			del request.session['user_id']
			request.session.flush()
			if user_account.objects.filter(user_id=request.session['user_id']).get():
				b=1
				h=0
				return redirect('/index/')
			else:
				b=1
				return redirect('/index/')
		except Exception:
			a=request.session['agent_id']
			del request.session['agent_id']
			request.session.flush()
			if agent_account.objects.filter(agent_id=request.session['agent_id']).get():
				b=1
				h=0
				return redirect('/index/')
			else:
				b=1
				return redirect('/index/')
	except Exception:
		return redirect('/index/')

			
	
def agentblog(request):
	agentid=request.session['agent_id']
	dic=getagentinfo(agentid)
	dic.update({'blogs':getblogs(agentid)})
	return render(request, 'agentdesk.html', dic)
@csrf_exempt
def allblogs_data(request):
	if request.method=="POST":
		n=request.POST.get('set')
		obj=blog_table.objects.all()
		return render(request, 'blogsdata.html',{'dic':obj})
@csrf_exempt
def delete_blog(request):
	if request.method=="POST":
		n=request.POST.get('set')
		obj=blog_table.objects.filter(blog_no=n)
		for i in obj:
			i.delete()
		return HttpResponse("<script> alert('Blog Is Deleted !!'); window.location.replace('/blog_posted/') </script>")

 		

@csrf_exempt
def openproperty(request):
	pid=request.GET.get('pid')
	dic=GetPropertyData(pid)
	dic.update({'catedata':GetPropertyCategoryData()})
	return render(request,'property-details.html',dic)
@csrf_exempt
def blog_page(request):
	
	return render(request, 'enterblog.html',{})

@csrf_exempt
def posted(request):
	n=request.session['agent_id']
	return render(request, 'enterblog.html',{})
@csrf_exempt
def post_blog(request):
	if request.method=="POST":
		n=request.POST.get('subject')
		p=request.FILES['pic']
		m=request.POST.get('mess')
		u='U00'
		x=1
		uid=u+str(x)
		while blog_table.objects.filter(blog_no=uid):
			x=x+1
			uid=u+str(x)
		x=int(x)
		try:
			if agent_account.objects.filter(agent_id=request.session['agent_id']).get():
				sv=blog_table(
					agent_id=request.session['agent_id'],
					blog_no=uid,
					pic_of_pro=p,
					subject=n,
					Desc=m
					)
				sv.save()
				return HttpResponse("<script> alert('Your Blog Is Posted !!'); window.location.replace('/blog_page/') </script>")
		except Exception:
			obj=PropertyCategoryData.objects.all()
			lt=[]
			for x in obj:
				lt.append(x.Category_Name)
			dic={'category':lt,
			'pdata':GetAllPropertyData()}
			
			sv=blog_table(
				agent_id='admin',
				blog_no=uid,
				pic_of_pro=p,
				subject=n,
				Desc=m
				)
			sv.save()

			return HttpResponse("<script> alert('Your Blog Is Posted !!'); window.location.replace('/blog_posted/')</script>")
			
def blog_posted(request):
	return render(request,'adminpannel.html',{})

def openmyblogs(request):
	return render(request,'myblogs.html',{})
	return HttpResponse("<script> alert('Your Blog Is Posted !!'); window.location.replace('/adminlogin/') </script>")
def openmyblogs(request):
	return render(request,'myblogs.html',{})

def openuseraccount(request):
	try:
		
		uid=request.session['user_id']
		dic=GetUserData2(uid)	
		return render(request,"myaccount.html",dic)
	except Exception:
		try:
			uid=request.session['agent_id']
			dic=getagentinfo(uid)
			dic.update({'blogs':getblogs(request.session['agent_id'])})
			return render(request,'agentdesk.html', dic)
		except:
			return redirect('/error/')





@csrf_exempt
def changeuserpassword(request):
	if request.method=="POST":
		uid=request.session['user_id']
		op=request.POST.get('old')
		np=request.POST.get('new')
		obj=user_account.objects.filter(password=op,user_id=uid)
		obj.update(password=np)
		if user_account.objects.filter(password=np,user_id=uid).exists():
			dic=GetUserData2(uid)
			email=''
			obj=user_account.objects.filter(user_id=uid)
			for x in obj:
				email=x.email
				break
			subject='Alert! : Your Account Password Has Changed'
			msg= '''Hi there!
Your account password has been change from '''+op+''' to '''+np+'''.
If this was not you please report us.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
			e.send()
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Password Changed Successfully'+b2
			dic.update({'alert':alert})		
			return render(request,"myaccount.html",dic)
		else:
			dic=GetUserData2(uid)
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Incorrect Password'+b2
			dic.update({'alert':alert})
			email=''
			obj=user_account.objects.filter(user_id=uid)
			for x in obj:
				email=x.email
				break
			subject='Alert! : Someone tries to change your Pssword'
			msg= '''Hi there!
Someone tries to change your Pssword. Kindly login and change your password again.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
			e.send()
			return render(request,"myaccount.html",dic)
def openuserorder(request):
	return render(request,'myorders.html',{})
#############################################################################################################

import razorpay
#Working on Test Keys
razorpay_client = razorpay.Client(auth=("rzp_test_30ncLAFfGjrh3N", "l6tOEr4l26jJqhTHwXhny0eX"))
razorpay_client.set_app_details({"title" : "Printsathi", "version" : "1.0"})

#############################################################################################################

@csrf_exempt
def orderdatasave(request):
	if request.method=="POST":
		pid=request.POST.get('P_id')
		pname=request.POST.get('P_Name')
		pprice=request.POST.get('P_Price')
		uid=''
		try:
			data=user_account.objects.filter(user_id=request.session['user_id'])
			for i in data:
				uid=i.user_id
				break;
		except:
			try:
				data=agent_account.objects.filter(agent_id=request.session['agent_id'])
				for i in data:
					uid=i.agent_id
					break;
			except:
				return HttpResponse("<script> alert('Your are not login !!'); window.location.replace('/index/') </script>")

		o='OR00'
		x=1
		oid=o+str(x)
		while OrderData.objects.filter(Order_ID=oid).exists():
			x=x+1
			oid=o+str(x)
		x=int(x)
		if uid !='':
			obj=OrderData(
				Order_ID=oid,
				Property_ID=pid,
				Property_Name=pname,
				Buyer_ID=uid,
				Order_Status='Unpaid',
				Total_Amount=pprice,
				Amount_to_Pay=pprice,
				
				)
			obj.save()
			return redirect('/opencart/')
		else:
			return redirect('/error/')
def opencart(request):
	lt=[]
	dic={}
	did=''
	userid=''
	agentid=''
	tm=0
	try:
		obj1=user_account.objects.filter(user_id=request.session['user_id'])
		for x in obj1:
			userid=x.user_id
			break
		obj1=OrderData.objects.filter(Buyer_ID=userid, Order_Status='Unpaid')
		for z in obj1:
			obj=PropertyData.objects.filter(Property_ID=z.Property_ID)
			for x in obj:
				dic={
					'orderid':z.Order_ID,
					'orderdate':z.Order_Date,
					'status':z.Order_Status,
					'name':x.Property_Name,
					'category':x.Property_Category,
					'price':x.Property_Price,
					'address':x.Property_Address,
					'area':x.Property_Area,
					'buildyear':x.Property_BuiltYear,
				}
				tm=tm+int(x.Property_Price)
				obj2=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
				for y in obj2:
					dic.update({
						'image':y.Property_Image.url,
						
						})
				lt.append(dic)
		obj1=OrderData.objects.filter(Buyer_ID=userid,Order_Status='Unpaid')
		obj1.update(Total_Amount=str(tm),
			Amount_to_Pay=str(tm),
			)
		return render(request,'cart.html',{'cartcount':GetCartCount(request),'cartdata':lt,'totalamount':tm,'count':len(lt)})

	except Exception:
		obj1=agent_account.objects.filter(agent_id=request.session['agent_id'])
		for x in obj1:
			agentid=x.agent_id
			break
		obj1=OrderData.objects.filter(Buyer_ID=agentid, Order_Status='Unpaid')
		for z in obj1:
			obj=PropertyData.objects.filter(Property_ID=z.Property_ID)
			for x in obj:
				dic={
					'orderid':z.Order_ID,
					'orderdate':z.Order_Date,
					'status':z.Order_Status,
					'name':x.Property_Name,
					'category':x.Property_Category,
					'price':x.Property_Price,
					'address':x.Property_Address,
					'area':x.Property_Area,
					'buildyear':x.Property_BuiltYear,
				}
				tm=tm+int(x.Property_Price)
				obj2=PropertyImagesData.objects.filter(Property_ID=z.Property_ID)
				for y in obj2:
					dic.update({
						'image':y.Property_Image.url,
						
						})
				lt.append(dic)
		obj1=OrderData.objects.filter(Buyer_ID=agentid,Order_Status='Unpaid')
		obj1.update(Total_Amount=str(tm),
			Amount_to_Pay=str((tm*90)/100),
			)

	return render(request,'cart.html',{'cartcount':GetCartCount(request),'cartdata':lt,'totalamount':tm,'count':len(lt)})

def deleteitem(request):
	pid=request.GET.get('pname')
	try:
		udata=user_account.objects.filter(user_id=request.session['user_id'])
		for i in udata:
			uid=i.user_id
			break;
	except:
		udata=agent_account.objects.filter(agent_id=request.session['agent_id'])
		for i in udata:
			uid=i.agent_id
			break;

	if OrderData.objects.filter(Buyer_ID=uid).exists(): 
		odata=OrderData.objects.filter(Order_ID=pid)
		odata.delete()
		return redirect('/opencart/')
	else:
		return HttpResponse("<script> alert('Sorry !, Order is not deleted'); window.location.replace('/opencart/') </script>")
 
def proceedtopay(request):
	try:
		try:
			if user_account.objects.filter(user_id=request.session['user_id']).exists():
				userid=''
				email=''
				dic={}
				obj1=user_account.objects.filter(user_id=request.session['user_id'])
				for x in obj1:
					userid=x.user_id
					email=x.email
					break;
		except:
			if agent_account.objects.filter(agent_id=request.session['agent_id']).exists():
				userid=''
				email=''
				dic={}
				obj1=agent_account.objects.filter(agent_id=request.session['agent_id'])
				for x in obj1:
					userid=x.agent_id
					email=x.email
					break;
		o='CRT00'
		x=1
		oid=o+str(x)
		while CartData.objects.filter(Cart_ID=oid).exists():
			x=x+1
			oid=o+str(x)
		x=int(x)
		obj1=OrderData.objects.filter(Buyer_ID=userid, Order_Status='Unpaid')
		for z in obj1:
			obj=CartData(Cart_ID=oid,Order_ID=z.Order_ID, Email=email, Buyer_ID=userid)
			obj.save()
			dic={'cid':oid,
				'orderid':z.Order_ID,
				'tamount':z.Total_Amount,
				'pamount':z.Amount_to_Pay,
				'amounttopay':float(z.Amount_to_Pay)*100,
				}
			request.session['cartid'] = oid
			try:
				obj=user_account.objects.filter(user_id=request.session['user_id'])
			except:
				obj=agent_account.objects.filter(agent_id=request.session['agent_id'])
			for x in obj:
				dic.update({
					'uname':x.name,
					'uemail':x.email,
					'uphone':x.phone
					})
			order_amount = int(dic['amounttopay'])
			order_currency = 'INR'
			order_receipt = dic['cid'] 
			options={
				'amount':order_amount,
				'currency':order_currency,
				'receipt':order_receipt,
				'payment_capture':'0'
			}
			dic.update(razorpay_client.order.create(options))
		return render(request,'proceedtopay.html', dic)
	except:
		return redirect('/agent_login/')


#Step 4
@csrf_protect
@csrf_exempt
def app_charge(request):
	dic={}
	email=''
	PID=''
	razorpay_order_id = request.POST.get('razorpay_order_id')
	razorpay_payment_id = request.POST.get('razorpay_payment_id')
	razorpay_signature = request.POST.get('razorpay_signature')
	params_dict = {
    'razorpay_order_id': razorpay_order_id,
    'razorpay_payment_id': razorpay_payment_id,
    'razorpay_signature': razorpay_signature}
	if razorpay_client.utility.verify_payment_signature(params_dict):
		obj=CartData.objects.filter(Cart_ID=request.session['cartid'])
		for x in obj:
			obj1=OrderData.objects.filter(Order_ID=x.Order_ID)
			obj1.update(Payment_ID=razorpay_payment_id,Order_Status='Paid')
			dic={'cid':x.Cart_ID,'pid':razorpay_payment_id}
			for j in obj1:
				PID=j.Property_ID
				break;
			obj3=PropertyData.objects.filter(Property_ID=PID)
			obj3.update(Property_status='SOLD')
		obj.delete()

		msg = '''Hi there!,
Your payment for Cart ID '''+request.session['cartid']+'''is successful!
Your Payment ID is '''+razorpay_payment_id+'''

Thanks & Regards,
Srirajco.com'''
		sub='Srirajco - Payment Successful'
		try:
			obj=user_account.objects.filter(user_id=request.session['user_id'])
		except:
			obj=agent_account.objects.filter(agent_id=request.session['agent_id'])
		for x in obj:
			email=x.email
			break;
		email = EmailMessage(sub, msg, to=email)
		email.send()
		return render(request,'paymentsuccess.html',dic)
	else:
		obj=CartData.objects.filter(Cart_ID=request.session['cartid'])
		for x in obj:
			print(x.Order_ID)
			obj1=OrderData.objects.filter(Order_ID=x.Order_ID)
			obj1.update(Payment_ID=razorpay_payment_id,Order_Status='Payment Failed')
			dic={'cid':x.Cart_ID,'pid':razorpay_payment_id}
		msg = '''Hi there!,
Your payment for Order ID '''+request.session['order_id']+'''is failed!
Your Payment ID is '''+razorpay_payment_id+'''
we apologize for this. Kindly send a mail to us regarding this problem.

Thanks & Regards,
Srirajco.com'''
		sub='Srirajco - Payment Failed'
		try:
			obj=user_account.objects.filter(user_id=request.session['user_id'])
		except:
			obj=agent_account.objects.filter(agent_id=request.session['agent_id'])
		for x in obj:
			email=x.email
			break;
		email = EmailMessage(sub, msg, to=[request.session['user_email']])
		email.send()
		return render(request,'paymentfailure.html',dic)
