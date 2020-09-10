
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
from django.db.models import Q
from Paytm import Checksum


def demo(request):
	n=8
	request.session['pop']=n
	s=popup(request)
	return redirect('/index/')
def error(request):
	#obj=PropertyData.objects.all().delete()
	#obj=PropertyImagesData.objects.all().delete()
	return render(request,'Error.html',{})

def index(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	blogs=allblogs()[0:3]
	bnnr=bannerimage.objects.all()
	
	g=popup(request)
	k=8
	try:
		try:	
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs, 'bnnr':bnnr, 'g':g, 'k':k})
				return render(request, 'index.html',dic)
			else:
				b=1
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs,'bnnr':bnnr, 'g':g, 'k':k})
				return render(request, 'index.html',dic)
			
		except:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs, 'bnnr':bnnr, 'g':g, 'k':k})
				return render(request, 'index.html',dic)
			else:
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				dic.update({'blogs':blogs, 'bnnr':bnnr, 'g':g, 'k':k})
				return render(request, 'index.html',dic)
	
	except Exception:
		dic={'obj':obj,'b':b, 'h':h}
		dic.update({'cdata':GetPropertyCategoryData()})
		dic.update({'blogs':blogs, 'bnnr':bnnr, 'g':g, 'k':k})
		return render(request, 'index.html',dic)


		
	
def properties(request):
	b=0
	h=0
	qs=allPropertyDataforproperty(request)
	area=request.GET.get('area')
	status=request.GET.get('status')
	loaction=request.GET.get('loaction')
	bedrooms=request.GET.get('bedrooms')
	bathrooms=request.GET.get('bathrooms')
	price=request.GET.get('range')
	CIR=request.GET.get('cname')

	if area !='' and area is not None:
		qs=allPropertyDataforpropertyarea(area)
	elif status !='' and status is not None:
		qs=allPropertyDataforpropertystatus(status)
	elif loaction !='' and loaction is not None:
		qs=allPropertyDataforpropertyloaction(loaction)
	elif bedrooms !='' and bedrooms is not None:
		qs=allPropertyDataforpropertybedrooms(bedrooms)
	elif bathrooms !='' and bathrooms is not None:
		qs=allPropertyDataforpropertybathrooms(bathrooms)
	elif price !='' and price is not None:
		qs=allPropertyDataforpropertyprice(price)
	elif CIR !='' and CIR is not None:
		qs=allPropertyDataforpropertydiversion(CIR)

		#two
	elif status !='' and status is not None and area !='' and area is not None:
		qs=allPropertyDataforpropertyAS(area,status)
	elif loaction !='' and loaction is not None and area !='' and area is not None:
		qs=allPropertyDataforpropertyAL(area,loaction)
	elif bedrooms !='' and bedrooms is not None and area !='' and area is not None:
		qs=allPropertyDataforpropertyAB(area,bedrooms)
	elif bathrooms !='' and bathrooms is not None and area !='' and area is not None:
		qs=allPropertyDataforpropertyABA(area,bathrooms)
	elif price !='' and price is not None and area !='' and area is not None:
		qs=allPropertyDataforpropertyAPR(area,price)

	#TWO status
	elif loaction !='' and loaction is not None or status !='' and status is not None:
		qs=allPropertyDataforpropertySL(status,loaction)
	elif bedrooms !='' and bedrooms is not None or status !='' and status is not None:
		qs=allPropertyDataforpropertySBE(status,bedrooms)
	elif bathrooms !='' and bathrooms is not None or status !='' and status is not None:
		qs=allPropertyDataforpropertySBA(status,bathrooms)
	elif price !='' and price is not None or status !='' and status is not None:
		qs=allPropertyDataforpropertySPR(status,price)

	elif area !='' and area is not None or loaction !='' and loaction is not None or status !='' and status is not None or bedrooms !='' and bedrooms is not None or bathrooms !='' and bathrooms is not None or price !='' and price is not None:
		qs=allPropertyDataforpropertyall(area,status,loaction,bedrooms,bathrooms,price)

	try:


		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'properties.html',{'obj': qs, 'b':b, 'h':h, 'cdata':GetPropertyCategoryData()})
			else:
				b=1

				return render(request, 'properties.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'properties.html',{'obj': qs, 'b':b, 'h':h, 'cdata':GetPropertyCategoryData()})
			else:
				return render(request, 'properties.html',{'obj': qs, 'cdata':GetPropertyCategoryData()})
	except Exception:
		qs[2]=40
		return render(request, 'properties.html',{'obj': qs, 'cdata':GetPropertyCategoryData()})	
def banner(request):
	return render(request, 'banner.html', {})


def bannerimg(request):
	if request.method=="POST":
		
		d=request.FILES['mapload']
		
		obj=bannerimage.objects.filter(id=2)
		for i in obj:
			i.image=d
			i.save()
			break
		return HttpResponse("<script> alert(' Image is uploaded !!'); window.location.replace('/banner/') </script>")
	else:
		return redirect('/banner/')

@csrf_exempt
def foroffr(request):
	
	if request.method=="POST":
		n=request.POST.get('email')

		obj=foroffer(
			Email_ID=n,
			)
		obj.save()
		subject='Mail From Shri Raj Property'
		msgg= ''' Dear Sir,

someone contact you for offer
 his  Phone is :- '''+n+''' 

Thanks & Regards
Shri Raj Property''' 
		msg=''' Thank you very much, to select our services now our representatives will contact you shortly or 
		else if you have any urgent work then you may contact +91 70005 96002

		Thanks & Regards
		Shri Raj Property'''

		ph=n
		sm=sendmsg(ph,msg)
		pph='7000596002'
		msg=''' Dear Sir,

someone contact you for offer
 his  Phone is :- '''+n+''' 

Thanks & Regards
Shri Raj Property'''
		sm=sendmsg(pph,msg)		

#		email = EmailMessage(subject, msg, to=['shrirajproperty00@gmail.com'])
#		#email.send()
		return HttpResponse("<script> alert(' Your request is send !!'); window.location.replace('/index/') </script>")


def imgforoffer(request):
	if request.method=="POST":
		
		d=request.FILES['pic']
		
		obj=bannerimage.objects.filter(id=2)
		for i in obj:
			i.offer=d
			i.save()
			break
		return HttpResponse("<script> alert(' Image is uploaded !!'); window.location.replace('/banner/') </script>")
	else:
		return redirect('/banner/')

def blog(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	dic=allblogs()
	blg=Testimonialdate.objects.all()
	try:	
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'blog.html',{'blg':blg, 'obj': obj, 'b':b, 'h':h,'elt':dic,'cdata':GetPropertyCategoryData()})
			else:
				b=1
				return render(request, 'blog.html',{'blg':blg, 'obj': obj, 'elt':dic,'cdata':GetPropertyCategoryData()})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'blog.html',{'blg':blg, 'obj': obj, 'b':b, 'h':h, 'elt':dic,'cdata':GetPropertyCategoryData()})
			else:
				return render(request, 'blog.html',{'blg':blg, 'obj': obj, 'elt':dic,'cdata':GetPropertyCategoryData()})
	except Exception:
		
		return render(request, 'blog.html',{'blg':blg, 'obj': obj, 'elt':dic, 'cdata':GetPropertyCategoryData()})

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
				return render(request, 'about.html',{'obj': obj, 'b':b, 'h':h,'cdata':GetPropertyCategoryData()})
			else:
				b=1
				return render(request, 'about.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'about.html',{'obj': obj, 'b':b, 'h':h, 'cdata':GetPropertyCategoryData()})
			else:
				return render(request, 'about.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
	except Exception:
		return render(request, 'about.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})

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
				return render(request, 'contact.html',{'obj': obj, 'b':b, 'h':h, 'cdata':GetPropertyCategoryData()})
			else:
				b=1
				return render(request, 'contact.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'contact.html',{'obj': obj, 'b':b, 'h':h, 'cdata':GetPropertyCategoryData()})
			else:
				return render(request, 'contact.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
	except Exception:
		return render(request, 'contact.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})

	
def registration(request):

	return render(request, 'registration.html', {'cdata':GetPropertyCategoryData()})
def login(request):
	return render(request, 'login.html', {'cdata':GetPropertyCategoryData()})
def adminlogin(request):
	return render(request, 'adminlogin.html', {'cdata':GetPropertyCategoryData()})
def admin_forgot_pass(request):
	return render(request, 'adminforget.html', {'cdata':GetPropertyCategoryData()})
def agent_forgot_pass(request):
	return render(request, 'agentforget.html', {'cdata':GetPropertyCategoryData()})
def userregistation(request):
	return render(request, 'userregistation.html',{'cdata':GetPropertyCategoryData()})
def loginformuser(request):
	return render(request, 'userlogin.html',{'cdata':GetPropertyCategoryData()})
def user_forgot_pass(request):
	return render(request, 'userforgot.html', {'cdata':GetPropertyCategoryData()})


@csrf_exempt
def adminlogincheck(request):
	if request.method=="POST":
		e=request.POST.get('email')
		p=request.POST.get('pass')

		if admind.objects.filter(email=e , password=p).exists():
			obj=admind.objects.filter(email=e , password=p)
			ad=''
			for i in obj:
				ad=i.position
				break
			if ad=='Admin':
				request.session['user']=e
				return redirect('/adminpannel/')
			elif admind.objects.filter(email=e , password=p).exists():

				request.session['cpanel']=e
				return redirect('/adminpannel/')

		else:
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Login Failed'
			return render(request, 'adminlogin.html', {'alert':alert})
						
	else:
		return redirect('/error/')
def adminpannel(request):
	b=1
	h=1
	try:
		try:
			
				n=request.session['user']
				h=0
				return render(request, 'adminpannel.html', {'b':b, 'h':h})
		except:
				n=request.session['cpanel']

				return render(request, 'adminpannel.html',{'b':b, 'h':h} )
	except:
		return redirect('/error/')


@csrf_exempt
def addadmin(request):
	if request.method=="POST":
		obj=admind.objects.all()
		return render(request, 'addadmin.html',{'admin':obj})
	else:
		return redirect('/error/')
@csrf_exempt
def saveadmin(request):
	if request.method=="POST":
		e=request.POST.get('email')
		ph=request.POST.get('phone')
		p=request.POST.get('pass')
		obj=admind(email=e, password=p, phone=ph)
		obj.save()
		return HttpResponse("<script> alert('Admin is added .!!'); window.location.replace('/adminpannel/') </script>")
	else:
		return redirect('/error/')

@csrf_exempt
def deleteadmin(request):
	if request.method=="POST":
		n=request.POST.get('data')
		obj=admind.objects.filter(email=n)
		obj.delete()
		return HttpResponse("<script> alert('Admin is deleted .!!'); window.location.replace('/adminpannel/') </script>")
	else:
		return redirect('/error/')
def adminchangepassword(request):
	try:
		uid=request.session['cpanel']
		return render(request, 'adminchangepass.html', {})
	except:
		return redirect('/error/')

@csrf_exempt
def changeadminpassword(request):
	if request.method=="POST":
		uid=request.session['cpanel']
		op=request.POST.get('old')
		np=request.POST.get('new')
		obj=admind.objects.filter(password=op,email=uid)
		obj.update(password=np)
		if admind.objects.filter(password=np,email=uid).exists():
			
			email=''
			ph=''
			obj=admind.objects.filter(email=uid)
			for x in obj:
				email=x.email
				ph=x.phone
				break
			subject='Alert! : Your Account Password Has Changed'
			msg= '''Hi there!
Your account password has been change from '''+op+''' to '''+np+'''.
If this was not you please report us.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
#			e.send()
			
			sm=sendmsg(ph,msg)		
			return HttpResponse("<script> alert('Password Changed Successfully.!!'); window.location.replace('/adminpannel/') </script>")

	else:
		return redirect('/error/')

@csrf_exempt
def deletecategory(request):
	if request.method=="POST":
		m= request.POST.get('set')
		userdata=PropertyCategoryData.objects.filter(Category_ID=m)
		userdata.delete()
		return HttpResponse("<script> alert('Category is deleted.!!'); window.location.replace('/adminpannel/') </script>")
	else:
		return redirect('/error/')

def Orderdetail(request):
	try:
		try:
			n=request.session['user']
			obj=OrderData.objects.filter(Order_Status='Unpaid')
			dic={'obj':obj}
			return render(request, 'orderdetails.html', dic)
		except:
			n=request.session['cpanel']
			obj=OrderData.objects.filter(Order_Status='Unpaid')
			dic={'obj':obj}
			return render(request, 'orderdetails.html', dic)
	except:
		return redirect('/error/')
def adminlogout(request):
	try:
		n=request.session['user']
		del request.session['user']
		request.session.flush()
		return redirect('/index/')
	except:
		n=request.session['cpanel']
		del request.session['cpanel']
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
def userdata(request):
	if request.method=="POST":
		userdata=user_account.objects.all()
		return render(request, 'usersdata.html', {'user': userdata})
	else:
		return redirect('/error/')

@csrf_exempt
def deleteuseraccount(request):
	if request.method=="POST":
		m= request.POST.get('set')
		userdata=user_account.objects.filter(user_id=m)
		userdata.delete()
		return redirect('/userdata/')
	else:
		return redirect('/error/')
@csrf_exempt
def testimonial(request):
	if request.method=="POST":
		n=request.POST.get('pass')
		obj=Testimonialdate.objects.all()
		return render(request, 'testimonial.html', {'obj':obj})
	else:
		return redirect('/error/')

@csrf_exempt
def testimonialdatasave(request):
	if request.method=="POST":
		n=request.POST.get('name')
		pic=request.FILES['pic']
		para=request.POST.get('feed')
		p="T00"
		x=1
		pid=p+str(x)
		while Testimonialdate.objects.filter(TestID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		data=Testimonialdate(TestID=pid,name=n, img=pic, feedback=para)
		data.save()
		return HttpResponse("<script> alert('data is save.!!'); window.location.replace('/adminpannel/') </script>")
	else:
		return redirect('/error/')

@csrf_exempt
def deletetestimonial(request):
	if request.method=="POST":
		m= request.POST.get('set')
		userdata=Testimonialdate.objects.filter(TestID=m)
		userdata.delete()
		return HttpResponse("<script> alert('data is delete.!!'); window.location.replace('/adminpannel/') </script>")
	else:
		return redirect('/error/')

@csrf_exempt
def updatepost(request):
	try:
		try:
			n=request.session['user']
			if request.method=="POST":
				m= request.POST.get('set')
				p=request.POST.get('pp')
				obj=agent_account.objects.filter(agent_id=m)
				for i in obj:
					i.Post=p
					i.save()
					break
				return HttpResponse("<script> alert('Post is updated .!!'); window.location.replace('/adminpannel/') </script>")
		except:
			n=request.session['cpanel']
			if request.method=="POST":
				m= request.POST.get('set')
				p=request.POST.get('pp')
				obj=agent_account.objects.filter(agent_id=m)
				for i in obj:
					i.Post=p
					i.save()
					break
				return HttpResponse("<script> alert('Post is updated .!!'); window.location.replace('/adminpannel/') </script>")
	except:
		return redirect('/error/')
	

@csrf_exempt
def make_active_agent(request):
	if request.method=="POST":
		s='active'
		u= 'not active'
		m= request.POST.get('set')
		if agent_account.objects.filter(agent_id=m):
			t=agent_account.objects.filter(agent_id=m)
			for i in t:
				i.status=s
				i.save()
				break
			op=agent_account.objects.filter(agent_id=m)
			for i in op:
				e=i.email
				p=i.password
				ph=i.phone
				break
			subject='Mail From Shri Raj Property'
			msg= ''' Dear Agent,

			You Account has been activated by the admin and
			Your account Password is:- '''+p+''' 

			Thanks & Regards
			Shri Raj Property''' 
					

			email = EmailMessage(subject, msg, to=[e])
			#email.send()
			
			sm=sendmsg(ph,msg)
			print('kkkkkkkkkkkkkk')	
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
					ph=i.phone
					break
				subject='Mail From Shri Raj Property'
				msg= ''' Dear Agent,

				Your account has been deavtivated by the Admin.
				For more information contact +917000596002.

				Thanks & Regards
				Shri Raj Property''' 
						

				email = EmailMessage(subject, msg, to=[e])
				#email.send()
				
				sm=sendmsg(ph,msg)	
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
		st=request.POST.get('streat')
		di=request.POST.get('direction')
		d=request.POST.get('Diversion')
		ad=request.POST.get('address')
		ar=request.POST.get('area')
		bd=request.POST.get('beds')
		bt=request.POST.get('baths')
		gr=request.POST.get('garages')
		f=request.POST.get('for')
		city=request.POST.get('city')
		facility=request.POST.get('Facilities')
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
			Property_Streat=st,
			Property_Direction=di,
			property_Diversion=d,
			Property_BuiltYear=y,
			Property_status=f,
			Property_location=city,
			property_Facility=facility
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request, 'adminpannel.html', {'alert':alert,'pdata':GetAllPropertyData()})
	else:
		return redirect('/error/')

def addplot(request):
	return render(request, 'addplot.html', {})
@csrf_exempt
def saveplot(request):
	if request.method=="POST":
		n=request.POST.get('name')
		a=request.POST.get('about')
		ar=request.POST.get('area')
		across=request.POST.get('across')
		property_price=request.POST.get('price')
		st=request.POST.get('streat')
		ad=request.POST.get('address')
		di=request.POST.get('direction')
		city=request.POST.get('city')
		c=request.POST.get('catagery')
		d=request.POST.get('Diversion')
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
			Property_across=across,
			Property_Price=property_price,
			Property_Streat=st,
			Property_Direction=di,
			property_Diversion=d,
			Property_Category=c,
			Property_status=f,
			Property_location=city
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request, 'adminpannel.html', {'alert':alert,'pdata':GetAllPropertyData()})
	else:
		return redirect('/error/')

def dataofplot(request):

	obj=PropertyData.objects.filter(Q(Property_Category='Farm') | Q(Property_Category='Plot') | Q(Property_Category='Shop') | Q(Property_Category='Hall'))
	return render(request, 'dataofplot.html', {'obj':obj})
def matarial(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'meterials.html',{'obj': obj, 'b':b, 'h':h,'cdata':GetPropertyCategoryData()})
			else:
				b=1
				return render(request, 'meterials.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'meterials.html',{'obj': obj, 'b':b, 'h':h, 'cdata':GetPropertyCategoryData()})
			else:
				return render(request, 'meterials.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
	except Exception:
		return render(request, 'meterials.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
	

def sendemailformatarial(request):
	if request.method=="POST":
		n=request.POST.get('name')
		p=request.POST.get('number')
		ad=request.POST.get('address')
		mt=request.POST.get('mistry')
		ti=request.POST.get('tilesfitting')
		car=request.POST.get('carpenter')
		pu=request.POST.get('Putty')
		pl=request.POST.get('Plummer')
		sus='Order of Laver'

		msg= ''' Hello sir,
	Someone order on the laver

	''' "Name :"+n+ ('\n') +"Phone :"+p+ ('\n')+"Address :"+ad+ ('\n')+"Raj Mistry :"+mt+ ('\n')+"Marbel or Tiles Fitting :"+ti+('\n')+"Carpenter :"+car+ ('\n')+"Putty, Painting and Wall Ceiling :"+pu+ ('\n') +"Plumber, Electrician :"+pl+'''

	Thanks & Regards
	Shri Raj Property''' 
		email = EmailMessage(sus, msg, to=['shrirajproperty00@gmail.com'])
		#email.send()
		ph='7000596002'
		sm=sendmsg(ph,msg)
		return HttpResponse("<script> alert(' Your request is send. Please wait for the response !!'); window.location.replace('/matarial/') </script>")

def sendemailmaterial(request):
	if request.method=="POST":
		n=request.POST.get('name')
		ph=request.POST.get('number')
		ad=request.POST.get('address')
		me=request.POST.get('message')
		subject='Order for Material'
		msg= ''' Hello sir,
	Someone order for material
''' "Name : "+n+('\n')+"Phone : "+ph+('\n')+"Address : "+ad+('\n')+"Material :"+me+'''

Thanks & Regards
Shri Raj Property''' 
		email = EmailMessage(subject, msg, to=['shrirajproperty00@gmail.com'])
		#email.send()
		ph='7000596002'
		sm=sendmsg(ph,msg)
		
		return HttpResponse("<script> alert(' Your request is send. Please wait for the response !!'); window.location.replace('/matarial/') </script>")

def mapaproval(request):
	try:
		userid=''
		dic={}
		lt=[]
		b=1
		h=1

		try:
			obj1=user_account.objects.filter(user_id=request.session['user_id'])
			userid=''
			for x in obj1:
				userid=x.user_id
				break
			h=0
		except:
			obj1=agent_account.objects.filter(agent_id=request.session['agent_id'])
			agentid=''
			for x in obj1:
				userid=x.agent_id
				break
			h=0
		obj=mapapproval.objects.filter(Buyer_ID=userid)
		for i in obj:
			dic={
			'Property_ID':i.Property_ID,
			'Land_Paper':i.Land_Paper,
			'Map_by_engineer':i.Map_by_engineer,
			'Copy_of_Tax':i.Copy_of_Tax,
			'other_details':i.other_details,
			'map_approved':i.map_approved
			} 
			lt.append(dic)
		return render(request, 'mapaproval.html', {'obj':lt,'cdata':GetPropertyCategoryData(), 'b':b, 'h':h})
	except:

		return render(request, 'mapaproval.html', {'cdata':GetPropertyCategoryData()})

def Mapaproved(request):
	obj=mapapproval.objects.all()
	return render(request, 'orderofmapaproval.html', {'obj':obj})


from wsgiref.util import FileWrapper
import mimetypes
import os

@csrf_exempt
def downloadaprovedmap(request,ide):

	obj=mapapproval.objects.filter(Property_ID=ide)
	file_path=''
	file_name=''
	for x in obj:
		file_name = x.map_approved.name
	file_path = settings.MEDIA_ROOT +'/'+ file_name
	file_wrapper = FileWrapper(open(file_path,'rb'))
	file_mimetype = mimetypes.guess_type(file_path)
	response = HttpResponse(file_wrapper, content_type=file_mimetype )
	response['X-Sendfile'] = file_path
	response['Content-Length'] = os.stat(file_path).st_size
	response['Content-Disposition'] = 'attachment; filename=%s' % file_name 
	return response
	
	

def savemapaproval(request):
	if request.method=="POST":
		Lp=request.FILES['LandPaper']
		mbe=request.FILES['mapbyEngineer']
		ct=request.FILES['CopyofTax']
		de= request.POST.get('details')
		p="M00"
		x=1
		pid=p+str(x)
		while mapapproval.objects.filter(Property_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		try:
			try:
				obj1=user_account.objects.filter(user_id=request.session['user_id'])
				userid=''
				for x in obj1:
					userid=x.user_id
					break
				ob=mapapproval(
					Property_ID=pid,
					Buyer_ID=userid,
					Land_Paper=Lp,
					Map_by_engineer=mbe,
					Copy_of_Tax=ct,
					other_details=de)
				ob.save()
				return HttpResponse("<script> alert(' Your data is send. Please wait for the response !!'); window.location.replace('/mapaproval/') </script>")


			except Exception:
				obj1=agent_account.objects.filter(agent_id=request.session['agent_id'])
				agentid=''
				for x in obj1:
					agentid=x.agent_id
					break
				ob=mapapproval(
					Property_ID=pid,
					Buyer_ID=agentid,
					Land_Paper=Lp,
					Map_by_engineer=mbe,
					Copy_of_Tax=ct,
					other_details=de)
				ob.save()
				return HttpResponse("<script> alert(' Your data is send. Please wait for the response !!'); window.location.replace('/mapaproval/') </script>")
		except:
			return HttpResponse("<script> alert('Login Know!!'); window.location.replace('/loginformuser/') </script>")
def uploadmap(request):
	if request.method=="POST":
		n=request.POST.get('pid')
		d=request.FILES['mapload']
		if mapapproval.objects.filter(Property_ID=n).exists():
			obj=mapapproval.objects.filter(Property_ID=n)
			obj.update(map_approved=d)
			return redirect('/Mapaproved/')
		else:
			return redirect('/error/')
	else:
		return redirect('/error/')


def loan(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'loan.html',{'obj': obj, 'b':b, 'h':h,'cdata':GetPropertyCategoryData()})
			else:
				b=1
				return render(request, 'loan.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'loan.html',{'obj': obj, 'b':b, 'h':h, 'cdata':GetPropertyCategoryData()})
			else:
				return render(request, 'loan.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
	except Exception:
		return render(request, 'loan.html',{'obj': obj, 'cdata':GetPropertyCategoryData()})
	

@csrf_exempt	
def sendloandetaial(request):
	if request.method=="POST":
		loan= request.POST.get('loan')
		name= request.POST.get('name')
		e= request.POST.get('email')
		ph= request.POST.get('number')
		c = request.POST.get('city')
		st= request.POST.get('state')
		dob=request.POST.get('dob')
		ep=request.POST.get('employee')
		income=request.POST.get('income')
		LR=request.POST.get('loanrequired')
		u='L00'
		x=1
		uid=u+str(x)
		while Loandetails.objects.filter(loan_id=uid):
			x=x+1
			uid=u+str(x)
		x=int(x)

		ob=Loandetails(
			loan_id=uid,
			Loan_Type=loan,
			Name=name,
			Email_ID=e,
			Phone=ph,
			City=c,
			State=st,
			DOB=dob,
			employee=ep,
			Income=income,
			Loan_Required=LR
			)
		ob.save()
		subject='Loan Mail From Shri Raj Property'
		msg= ''' Hello sir,

Someone Need a Loan,
there is detaile
'''  "Loan Type :"+loan+('\n')+"Name :"+name+ ('\n') +"Email ID :"+e+ ('\n')+"Phone :"+ph+ ('\n')+"City :"+c+ ('\n')+"State :"+st+('\n')+"DOB :"+dob+ ('\n')+"Employee :"+ep+ ('\n') +"Income:"+income+ ('\n') +"Loan Required :"+LR+'''


Thanks & Regards
Shri Raj Property''' 
					

		email = EmailMessage(subject, msg, to=['shrirajproperty00@gmail.com'])
		#email.send()
		ph='7000596002'
		sm=sendmsg(ph,msg)
		return HttpResponse("<script> alert(' Your request is send. Please wait for the response !!'); window.location.replace('/loan/') </script>")


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
				
				subject='Mail From Shri Raj Property'
				msg= ''' Hello sir,

		You are successfully registered, but your account is not active
		please wait for the owner response 

		Thanks & Regards
		Shri Raj Property''' 
				

				email = EmailMessage(subject, msg, to=[e])
				#email.send()
				
				sm=sendmsg(ph,msg)

				try:
					sus='New Agent Register'

					msg= ''' Hello sir,
		This Person want to make your agent
		detail of the person is here

		''' "Name :"+n+ ('\n') +"Gender :"+g+ ('\n')+"email :"+e+ ('\n')+"Address :"+ad+ ('\n')+"City :"+c+('\n')+"Phone :"+ph+ ('\n')+"Aadhar No. :"+aa+ ('\n') +"Facebook Link :"+fb+ ('\n') +"Twitter Link :"+tw+ ('\n') +"LinkedIn Link :"+LI+'''

				Thanks & Regards
				Shri Raj Property''' 


					
					email = EmailMessage(sus, msg, to=['shrirajproperty00@gmail.com'])
					#email.send()
					phe='7000596002'
					sm=sendmsg(phe,msg)
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
					obj=bankaccount(agent_id=uid)
					obj.save()
					message='You are successfully registered.'	

					return HttpResponse("<script> alert('You are successfully registered. !!'); window.location.replace('/login/') </script>")
				except Exception:
					message='Fill The Form Again'	
					return render(request,'registration.html', {'message':message})
			

			except Exception:
				message=' Enter Valid Mail Address'
				return render(request,'registration.html', {'message':message})
	else:
		message=' Enter Valid Mail Address'
		return render(request,'registration.html', {'message':message})


def showdocument(request):
	return render(request, 'showdocuments.html',{'elt':documents.objects.all()})

@csrf_exempt
def openaddpropertycategory(request):
	if request.method=="POST":
		return render(request, "addpropertycategory.html",{'cdata':GetPropertyCategoryData()})
	else:
		return redirect('/error/')
@csrf_exempt
def openadddocuments(request):
	
	return render(request, "adddocument.html",{'cdata':documents.objects.all()})

@csrf_exempt		
def savedocuments(request):
	if request.method=="POST":
		u='D00'
		x=1
		uid=u+str(x)
		while documents.objects.filter(Doc_ID=uid):
			x=x+1
			uid=u+str(x)
		x=int(x)
		t=request.POST.get('title')
		f=request.FILES['doc']
		ob=documents(Doc_ID=uid, title=t, file=f)
		ob.save()
		return HttpResponse("<script> alert(' Data is save !!'); window.location.replace('/openadddocuments/') </script>")

		
	else:
		return redirect('/error/')

@csrf_exempt		
def delete(request):
	if request.method=="POST":
		d=request.POST.get('delete')
		ob=documents.objects.filter(Doc_ID=d)
		ob.delete()
		return HttpResponse("<script> alert(' Data is deleted !!'); window.location.replace('/openadddocuments/') </script>")
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
def openaddpropertyvideo(request):
	if request.method=="POST":
		dic={'propertyid':GetPropertyID(),
			'propertyvideodata':GetPropertyVideoData()}
		return render(request, "addpropertyvideo.html",dic)
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
def savepropertyvideos(request):
	if request.method=="POST":
		n=request.POST.get('propertyid')
		m=request.FILES['image']
		obj=PropertyVideo(
			Property_ID=n,
			property_video=m

			)
		obj.save()
		dic={'propertyid':GetPropertyID(),
			'propertyvideodata':GetPropertyVideoData()}
		return render(request, "addpropertyvideo.html",dic)
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
		dic.update({'catedata':GetPropertyCategoryData(),'cddata':GetPropertyCategoryData()})
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
						i.agentpic_is_aadharcard=c
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
			
def openbankccountdetails(request):
	try:
		uid=request.session['agent_id']
		obj=bankaccount.objects.filter(agent_id=uid)
		dic={}
		for i in obj:
			dic={
			'pic':i.checkpic.url,
			'name':i.accountholdername,
			'bank':i.bankname,
			'account':i.accountno,
			'ifsc':i.IFSC
			}
			break

		return render(request,"agentbank.html",dic)
	except:
		return redirect('/error/')

	
def Changebankdata(request):
	
		uid=request.session['agent_id']
		obj=bankaccount.objects.filter(agent_id=uid)
		dic={}
		for i in obj:
			dic={
			'pic':i.checkpic.url,
			'name':i.accountholdername,
			'bank':i.bankname,
			'account':i.accountno,
			'ifsc':i.IFSC
			}
			break
		
		return render(request,"bankaccountdetails.html", dic)
	
def saveaccountdetails(request):
	if request.method=="POST":
		uid=request.session['agent_id']
		

		n=request.POST['name']
		b=request.POST.get('bank')
		accno=request.POST.get('accountno')
		ifsc=request.POST.get('ifsc')
		
		if agent_account.objects.filter(agent_id=uid).exists():
			obj=bankaccount.objects.filter(agent_id=uid)
			
			obj.update(accountholdername=n)
			obj.update(bankname=b)
			obj.update(accountno=accno)
			obj.update(IFSC=ifsc)
		try:
			pi=request.FILES['pic']
			for i in obj:
				i.checkpic=pi
				i.save()
				break;
		except:
			pass

		return HttpResponse("<script> alert(' Bank Details are saved !!'); window.location.replace('/openbankccountdetails/') </script>")
		
	else:
		return redirect('/error/')
def Commission(request):
	return render(request, 'commission.html',{})
@csrf_exempt
def user_signup(request):
	if request.method=="POST":
		n= request.POST.get('name')
		g= request.POST.get('gender')
		e= request.POST.get('email')
		ad= request.POST.get('address')
		c = request.POST.get('city')
		ph= request.POST.get('phone')
		pic='userpic/Card.jpg'
		
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		
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
				
				
				email = EmailMessage(subject, msg, to=[e])
				#email.send()
				
				
				sm=sendmsg(ph,msg)
				sv=user_account(user_id=uid, name=n, gender=g, email=e, address=ad, city=c, phone=ph,password=p, userpic=pic)
				sv.save()
				message='You are successfully registered. password is send to your given mail account'	
				return render(request,'userregistation.html', {'message':message})
			except:
				message='You are not successfully registered.'	
				return render(request,'userregistation.html', {'message':message})					
			
	else:
		message='Please fill the details'	
		return render(request,'userregistation.html', {'message':message})
@csrf_exempt
def user_login(request):
	if request.method=="POST":
		b=0
		h=0
		e=request.POST.get('email')
		p=request.POST.get('pass')
		l=0
		if user_account.objects.filter(email=e, password=p).exists():
			ua = user_account.objects.filter(email=e)
			l=1
		elif user_account.objects.filter(phone=e, password=p).exists():
			ua = user_account.objects.filter(phone=e)
			l=1
		else:
			l=0
		if l==1:
			for i in ua:
				c=i.user_id
				request.session['user_id']=c
				b=1
				break
			if request.session.has_key('user_id') and b==1: 
				
				h=1
				dic=GetUserData(e)
				return redirect('/useraccount/')
			else:
				return HttpResponse("<script> alert(' Please Enter Valid Details !!'); window.location.replace('/loginformuser/') </script>")


		else:
			message='Please Enter Valid Details'

			return render(request,'userlogin.html',{'message': message})
def useraccount(request):
	try:
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
	except:
		b=1
		if request.session.has_key('agent_id') and b==1:
			
			h=1
		dic=getagentinfo(request.session['agent_id'])
		dic.update({'blogs':getblogs(request.session['agent_id'])})
		return render(request, 'agentdesk.html', dic)

	else:
		return redirect('/error/')


@csrf_exempt
def agent_login(request):

	b=0
	h=0
	l=0
	s='active'
	e=request.POST.get('email')
	p=request.POST.get('pass')

	if agent_account.objects.filter(email=e, password=p).exists():
		ua = agent_account.objects.filter(email=e)
		l=1
	elif agent_account.objects.filter(phone=e, password=p).exists():
		ua = agent_account.objects.filter(phone=e)
		l=1
	else:
		l=0
	if l==1:
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
			
			h=1
			dic=getagentinfo(request.session['agent_id'])
			dic.update({'blogs':getblogs(request.session['agent_id'])})
			return render(request, 'agentdesk.html', dic)
		else:
			return HttpResponse("<script> alert(' Please Enter valid details !!'); window.location.replace('/login/') </script>")
	else:
		message='Please Enter valid details'
		return render(request,'login.html',{'message': message})

@csrf_exempt
def password_send_to_user(request):
	if request.method=="POST":
		e=request.POST.get('email')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		
		if user_account.objects.filter(email=e).exists():
			u=user_account.objects.filter(email=e)
			for i in u:
				i.password=p
				ph=i.phone
				break
			subject='Mail From Shri Raj Property'
			msg= ''' Hello sir,

			Your passwaord has been changed, 
			your password is :'''+p+''' 

			Thanks & Regards
			Shri Raj Property''' 
					
			try:
				email = EmailMessage(subject, msg, to=[e])
				#email.send()
				
				sm=sendmsg(ph,msg)
				i.save()
				return HttpResponse("<script> alert('Hello User, Your password has been sent to your registered Email. If you have not received the password, go to the contact page and send an email. Will be processed within 24 hours !!'); window.location.replace('/loginformuser/') </script>")
			except Exception:
				return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/user_forgot_pass/') </script>")
		else:
			return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/user_forgot_pass/') </script>")

@csrf_exempt
def password_send_to_Admin(request):
	if request.method=="POST":
		e=request.POST.get('phone')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		
		
		if admind.objects.filter(phone=e).exists():
			u=admind.objects.filter(phone=e)
			print('fggkjhgfd')
			for i in u:
				i.password=p
				ph=i.phone
				
				break
			subject='Mail From Shri Raj Property'
			msg= ''' Hello sir,

			Your passwaord has been changed, 
			your password is :'''+p+''' 

			Thanks & Regards
			Shri Raj Property''' 
					
			try:
				
				#email.send()
				
				sm=sendmsg(ph,msg)
				i.save()
				print('lllllllllllllllllllllllllllllllllll')
				return HttpResponse("<script> alert('Hello sir, Your password has been sent to your Phone number. If you have not received the password, go to the contact page and send an email. Will be processed within 24 hours !!'); window.location.replace('/adminlogin/') </script>")
			except Exception:
				return HttpResponse("<script> alert('Please Enter The Valid Phone number .!!'); window.location.replace('/admin_forgot_pass/') </script>")
		else:
			return HttpResponse("<script> alert('Please Enter The Valid Phone number  .!!'); window.location.replace('/admin_forgot_pass/') </script>")
	
		

@csrf_exempt
def password_send_to_agent(request):
	if request.method=="POST":
		e=request.POST.get('email')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		
		
		if agent_account.objects.filter(email=e).exists():
			u=agent_account.objects.filter(email=e)
			for i in u:
				i.password=p
				ph=i.phone
				break
			subject='Mail From Shri Raj Property'
			msg= ''' Hello sir,

			Your passwaord has been changed, 
			your password is :'''+p+''' 

			Thanks & Regards
			Shri Raj Property''' 
					
			try:
				email = EmailMessage(subject, msg, to=[e])
				#email.send()
				
				sm=sendmsg(ph,msg)
				i.save()
				return HttpResponse("<script> alert('Hello Agent, Your password has been sent to your registered Email. If you have not received the password, go to the contact page and send an email. Will be processed within 24 hours !!'); window.location.replace('/login/') </script>")
			except Exception:
				return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/agent_forgot_pass/') </script>")
		else:
			return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/agent_forgot_pass/') </script>")
	



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

		email = EmailMessage(subject, msg, to=['shrirajproperty00@gmail.com'])
#		email.send()
		ph='7000596002'
		sm=sendmsg(ph,msg)
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

def singleinfo(request):
	

		n=request.session['cpanel']
		return render(request,'singleinfo.html', dic)

@csrf_exempt
def detailofagents(request):
	if request.method=="POST":
		n=request.POST.get('set')
		dic=GetagentData3(n)
		return render(request,'singleinfo.html', dic)
 		

@csrf_exempt
def openproperty(request):
	try:
		b=1
		h=1
		try:
			n=request.session['agent_id'] 
			b=1	
			h=0
			pid=request.GET.get('pid')
			dic=GetPropertyData(request, pid)
			dic.update({'catedata':GetPropertyCategoryData(),'b':b, 'h':h})
			return render(request,'property-details.html',dic)
		except:
			n=request.session['user_id'] 
			b=1	
			h=0
			pid=request.GET.get('pid')
			dic=GetPropertyData(request, pid)
			dic.update({'catedata':GetPropertyCategoryData(),'b':b, 'h':h})
			return render(request,'property-details.html',dic)
	except:
		pid=request.GET.get('pid')
		dic=GetPropertyData(request, pid)
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
def changeaadhar(request):
	try:
		if request.method=="POST":
			uid=request.session['agent_id']
			op=request.POST.get('aadhar')
			ap=request.FILES['pic']
			np=request.POST.get('agent')
			obj=agent_account.objects.filter(agent_id=np)
			obj.update(aadhar=op)
			for i in obj:
				i.agentpic=ap
				i.save()
				break
			return HttpResponse("<script> alert(' Aadhar number Changed Successfully !!'); window.location.replace('/openuseraccount/') </script>")
	except:
		return HttpResponse("<script> alert(' Aadhar number is not Changed Successfully !!'); window.location.replace('/openuseraccount/') </script>")



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
			ph=''
			obj=user_account.objects.filter(user_id=uid)
			for x in obj:
				email=x.email
				ph=x.phone
				break
			subject='Alert! : Your Account Password Has Changed'
			msg= '''Hi there!
Your account password has been change from '''+op+''' to '''+np+'''.
If this was not you please report us.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
#			e.send()
			
			sm=sendmsg(ph,msg)
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
#			e.send()
			return render(request,"myaccount.html",dic)

@csrf_exempt
def changeagentpassword(request):
	if request.method=="POST":
		uid=request.session['agent_id']
		op=request.POST.get('old')
		np=request.POST.get('new')
		obj=agent_account.objects.filter(password=op,agent_id=uid)
		obj.update(password=np)
		if agent_account.objects.filter(password=np,agent_id=uid).exists():
			dic=GetUserData2(uid)
			email=''
			ph=''
			obj=agent_account.objects.filter(agent_id=uid)
			for x in obj:
				email=x.email
				ph=x.phone
				break
			subject='Alert! : Your Account Password Has Changed'
			msg= '''Hi there!
Your account password has been change from '''+op+''' to '''+np+'''.
If this was not you please report us.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
#			e.send()
			
			sm=sendmsg(ph,msg)
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Password Changed Successfully'+b2
			dic.update({'alert':alert})		
			return HttpResponse("<script> alert(' Password Changed Successfully !!'); window.location.replace('/openuseraccount/') </script>")
		else:
			dic=GetUserData2(uid)
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Incorrect Password'+b2
			dic.update({'alert':alert})
			email=''
			obj=agent_account.objects.filter(agent_id=uid)
			for x in obj:
				email=x.email
				break
			subject='Alert! : Someone tries to change your Pssword'
			msg= '''Hi there!
Someone tries to change your Pssword. Kindly login and change your password again.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
#			e.send()

			return HttpResponse("<script> alert(' Someone tries to change your Pssword !!'); window.location.replace('/openuseraccount/') </script>")
def openuserorder(request):
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
		obj1=OrderData.objects.filter(Buyer_ID=userid)
		for z in obj1:
			obj=PropertyData.objects.filter(Property_ID=z.Property_ID)
			obj2=PropertyImagesData.objects.filter(Property_ID=z.Property_ID)
			for x in obj:
				for y in obj2:
					
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
						'payment':z.Payment_ID,
						'image':y.Property_Image.url,
					}
					tm=tm+int(x.Property_Price)
				
					lt.append(dic)
		obj1=OrderData.objects.filter(Buyer_ID=userid)
		obj1.update(Total_Amount=str(tm),
			Amount_to_Pay=str(tm),
			)
		return render(request,'myorders.html',{'cartcount':GetCartCount(request),'cartdata':lt,'totalamount':tm,'count':len(lt)})

	except Exception:
		obj1=agent_account.objects.filter(agent_id=request.session['agent_id'])
		for x in obj1:
			agentid=x.agent_id
			break
		obj1=OrderData.objects.filter(Buyer_ID=agentid)
		for z in obj1:
			obj=PropertyData.objects.filter(Property_ID=z.Property_ID)
			obj2=PropertyImagesData.objects.filter(Property_ID=z.Property_ID)
			for x in obj:
				for y in obj2:
					
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
						'payment':z.Payment_ID,
						'image':y.Property_Image.url,
					}
					tm=tm+int(x.Property_Price)
				
					lt.append(dic)
					obj2=OrderData.objects.filter(Buyer_ID=agentid,Order_Status='Unpaid')
					obj2.update(Amount_to_Pay=x.Property_Price)
		obj1=OrderData.objects.filter(Buyer_ID=agentid,Order_Status='Unpaid')
		obj1.update(Total_Amount=str(tm))
		

	return render(request,'myorders.html',{'cartcount':GetCartCount(request),'cartdata':lt,'totalamount':tm,'count':len(lt)})
	
#############################################################################################################

import razorpay
#Working on Test Keys
razorpay_client = razorpay.Client(auth=("rzp_test_30ncLAFfGjrh3N", "l6tOEr4l26jJqhTHwXhny0eX"))
razorpay_client.set_app_details({"title" : "Srirajco", "version" : "1.0"})

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
	pm=0
	try:
		obj1=user_account.objects.filter(user_id=request.session['user_id'])
		for x in obj1:
			userid=x.user_id
			break
		obj1=OrderData.objects.filter(Buyer_ID=userid, Order_Status='Unpaid')
		for z in obj1:
			obj=PropertyData.objects.filter(Property_ID=z.Property_ID)
			obj2=PropertyImagesData.objects.filter(Property_ID=z.Property_ID)
			for x in obj:
				for y in obj2:
					
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
						'payment':z.Payment_ID,
						'image':y.Property_Image.url,
					}
					tm=tm+int(x.Property_Price)
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
			obj2=PropertyImagesData.objects.filter(Property_ID=z.Property_ID)
			for x in obj:
				for y in obj2:
					
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
						'payment':z.Payment_ID,
						'image':y.Property_Image.url,
					}
					tm=tm+int(x.Property_Price)
				
					lt.append(dic)
					obj2=OrderData.objects.filter(Buyer_ID=agentid,Order_Status='Unpaid')
					obj2.update(Amount_to_Pay=x.Property_Price)
					break;
		obj1=OrderData.objects.filter(Buyer_ID=agentid,Order_Status='Unpaid')
		obj1.update(Total_Amount=str(tm))

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

MERCHANT_KEY = 'RI9JfwDrRA%7FCKu'

def proceedtopay(request):
#	b=1	
#	h=0
#	return render(request,'paytms.html', {'b':b, 'h':h})

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
		odb=z.Order_ID
		request.session['order']=z.Order_ID
		obj=CartData(Cart_ID=oid,Order_ID=z.Order_ID, Email=email, Buyer_ID=userid)
		obj.save()
		dic={
			'MID':'UjaSHP50592702896118',
			'ORDER_ID':z.Order_ID,
			'TXN_AMOUNT':z.Amount_to_Pay,
			}
		request.session['cartid'] = oid

		try:
			obj=user_account.objects.filter(user_id=request.session['user_id'])
		except:
			obj=agent_account.objects.filter(agent_id=request.session['agent_id'])
		for x in obj:
			dic.update({
				'CUST_ID':x.email,
				
				'INDUSTRY_TYPE_ID':'Retail',
				'WEBSITE':'WEBSTAGING',
				'CHANNEL_ID':'WEB',
				'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
				
				})
	dic['CHECKSUMHASH']=Checksum.generate_checksum(dic, MERCHANT_KEY)
	return render(request, 'paytm.html', {'dic': dic})

@csrf_exempt	
def handlerequest(request):
#	return HttpResponse('done')



	form = request.POST
	response_dict={}

	for i in form.keys():
		response_dict[i]=form[i]
		if i == 'CHECKSUMHASH':
			checksum=form[i]
	verify= Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
	if verify:
		if response_dict['RESPCODE'] == '01':
			print('Payment successful !!')
			return render(request, 'paymentstatus.html', {'response': response_dict})

					
		else:
			print('order was not successful because'+ response_dict['RESPMSG'])
			return render(request, 'paymentfailure.html', {'response': response_dict})


@csrf_exempt
def txndata(request):
	if request.method=="POST":
		od=request.POST.get('odid')
		tx=request.POST.get('txnid')
		st=request.POST.get('sted')
		amnt=request.POST.get('amnt')
		d=''
		try:
			obj=OrderData.objects.filter(Buyer_ID=request.session['agent_id'], Order_ID=od)
		except:
			obj=OrderData.objects.filter(Buyer_ID=request.session['user_id'], Order_ID=od)

		obj.update(Order_Status=st)
		obj.update(Amount_to_Pay=amnt)
		obj.update(Payment_ID=tx)
		for i in obj:
			d=i.Property_ID
			break
		pt=PropertyData.objects.filter(Property_ID=d)
		pt.update(Property_status='SOLD')		
		return HttpResponse("<script> alert('Payment Successful !!'); window.location.replace('/opencart/') </script>")

@csrf_exempt
def txnfail(request):
	if request.method=="POST":
		od=request.POST.get('odid')
		tx=request.POST.get('txnid')
		st=request.POST.get('sted')
		amnt=request.POST.get('amnt')
		d=''
		try:
			obj=OrderData.objects.filter(Buyer_ID=request.session['agent_id'], Order_ID=od)
		except:
			obj=OrderData.objects.filter(Buyer_ID=request.session['user_id'], Order_ID=od)

		obj.update(Order_Status=st)
		obj.update(Amount_to_Pay=amnt)
		obj.update(Payment_ID=tx)
		for i in obj:
			d=i.Property_ID
			break
		pt=PropertyData.objects.filter(Property_ID=d)
		pt.update(Property_status='SOLD')		
		return HttpResponse("<script> alert('Payment is not successful  !!'); window.location.replace('/opencart/') </script>")


#Step 4
@csrf_protect
@csrf_exempt
def app_charge(request):
	dic={}
	email=''
	PID=''
	oid=''
	razorpay_order_id = request.POST.get('razorpay_order_id')
	razorpay_payment_id = request.POST.get('razorpay_payment_id')
	razorpay_signature = request.POST.get('razorpay_signature')
	print(razorpay_order_id)
	print(razorpay_payment_id)
	print(razorpay_signature)
	params_dict = {
    'razorpay_order_id': razorpay_order_id,
    'razorpay_payment_id': razorpay_payment_id,
    'razorpay_signature': razorpay_signature}
	
	n=razorpay_client.utility.verify_payment_signature(params_dict)
	print(n)
	try:
		print('hlo')
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
		print('asdf')
		print('hrllo')
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
		email = EmailMessage(sub, msg, to=[email])
		#email.send()
		return render(request,'paymentsuccess.html',dic)
	except:
		obj=CartData.objects.filter(Cart_ID=request.session['cartid'])
		for x in obj:
			oid=x.Order_ID
			obj1=OrderData.objects.filter(Order_ID=x.Order_ID)
			obj1.update(Payment_ID=razorpay_payment_id,Order_Status='Payment Failed')
			dic={'cid':x.Cart_ID,'pid':razorpay_payment_id}
		msg = '''Hi there!,
Your payment for Order ID '''+oid+'''is failed!
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
		email = EmailMessage(sub, msg, to=[email])
		#email.send()
		return render(request,'paymentfailure.html',dic)




def handler404(request):
    return render(request, 'error500.html',{})
def handler500(request):
	return render(request, 'error500.html',{})