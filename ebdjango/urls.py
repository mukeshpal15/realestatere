from django.contrib import admin
from django.urls import path, include
from realstateapp.views import *
from django.conf import settings
from django.conf.urls.static import static
import realstateapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('demo/', demo),
    path('about/', about),
    path('property_detail/', property_detail),
    path('blog/', blog),
    path('allblogs_data/',allblogs_data),
    path('delete_blog/',delete_blog),
    path('blog_posted/',blog_posted),
    path('properties/', properties),
    path('contact/', contact),
    path('registration/', registration),
    path('login/', login),
    path('adminlogin/', adminlogin),
    path('adminlogincheck/', adminlogincheck),
    path('adminlogout/',adminlogout),
    path('adminpannel/', adminpannel),
    path('openaddproperty/', openaddproperty),
    path('saveproperty/', saveproperty),
    path('delete_property/', delete_property),
    path('openaddpropertycategory/', openaddpropertycategory),
    path('savepropertycategory/', savepropertycategory),
    path('agent_signup/',agent_signup),
    path('agent_forgot_pass/', agent_forgot_pass),
    path('password_send_to_agent/',password_send_to_agent),
    path('openaddpropertyimages/', openaddpropertyimages),
    path('savepropertyimages/', savepropertyimages),
    path('error/', error),
    path('agentdata/', agentdata),
    path('Orderdetail/',Orderdetail),
    path('make_active_agent/',make_active_agent),
    path('make_deactive_agent/',make_deactive_agent),
    path('openpropertycategory/',openpropertycategory),
    path('openmyaccount/',openmyaccount),
    path('propertypaginator/',propertypaginator),
    path('user_signup/',user_signup),
    path('userregistation/', userregistation),
    path('loginformuser/', loginformuser),
    path('user_login/',user_login),
    path('useraccount/',useraccount),
    path('user_forgot_pass/', user_forgot_pass),
    path('password_send_to_user/', password_send_to_user),
    path('send_mail_by_contact/', send_mail_by_contact),
    path('Log/', Log),
    path('openuseraccount/',openuseraccount),
    path('dele/',dele),
    path('openproperty/', openproperty),
    path('openchangeaccountdetails/',openchangeaccountdetails),
    path('agent_login/', agent_login),
    path('agentblog/',agentblog),
    path('blog_page/',blog_page),
    path('post_blog/',post_blog),
    path('openmyblogs/',openmyblogs),
    path('openchangeaccountdetails/',openchangeaccountdetails),
    path('openmyblogs/',openmyblogs),
    path('openchangeaccountdetails/',openchangeaccountdetails),
    path('savechangeaccountdetails/',savechangeaccountdetails),
    path('changeuserpassword/',changeuserpassword),
    path('openuserorder/',openuserorder),
    path('posted/',posted),
    path('orderdatasave/',orderdatasave),
    path('opencart/', opencart),
    path('deleteitem/',deleteitem),
    path('proceedtopay/',proceedtopay),
    path('pay/',app_charge),
    path('handler404/',handler404),
    path('handler404/',handler500),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

handler404 = realstateapp.views.handler404
handler500 = realstateapp.views.handler500