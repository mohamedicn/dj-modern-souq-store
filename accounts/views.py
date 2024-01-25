from django.contrib import messages
from django.shortcuts import render ,redirect ,get_object_or_404
from orders.models import Order,OrderDetails
from.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login ,authenticate
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django_countries import countries
from.tokens import accout_actvation_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from project import settings
from django.contrib.auth import logout
from django.http import JsonResponse
from products.models import Product
def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and accout_actvation_token.check_token(user, token):
        # activate the user's account
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated!')
        login(request, user)
        return redirect('/')
    else:
        messages.error(request, 'Invalid activation link.')
        return redirect('/')


def signup(request):
    if request.user.is_authenticated:  
        return redirect('/')
    
    if request.method == 'POST':
        first_name=None
        scand_name=None
        email=None
        password=None
        passwordconfigration=None
        
        if 'first_name' in request.POST : first_name=request.POST['first_name']
        else :messages.error(request,'Error in First Name !')
        
        if 'scand_name' in request.POST : scand_name=request.POST['scand_name']
        else :messages.error(request,'Error in Scand Name !')
        
        if 'email' in request.POST : email=request.POST['email']
        else : messages.error(request,'Error in Email !')
        
        if 'password' in request.POST: password=request.POST['password']
        else : messages.error(request,'Error in password !')
        
        if 'passwordconfigration' in request.POST: passwordconfigration=request.POST['passwordconfigration']
        else : messages.error(request,'Error in Password Configration !')
        
        context={'first_name':first_name,
                    'scand_name':scand_name,
                    'email':email}
        if first_name and scand_name and email and password and passwordconfigration:
            if User.objects.filter(email=email).exists():
                messages.error(request,'This Email Name is taken !')
                return render(request,'registration/signup.html',context)
            else:
                if password != passwordconfigration:
                    messages.error(request,'The two password fields didn’t match.')
                    return render(request,'registration/signup.html',context)
                else:
                    username = email.split("@")[0]
                    user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=scand_name,
                    is_active=False,
                    email=email,
                    password=password
                    )
                    user.save()
        else:
            messages.error(request,'Please fill in all fields !')
            return render(request,'registration/signup.html',context)
        mailsubject='activate your account'
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = accout_actvation_token.make_token(user)
        message=f"Hi {user.username},\n\nPlease click on the following link to activate your account:\n\n{get_current_site(request).domain}/accounts/activate_account/{uid}/{token}/\n\nThanks!\n"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,] 
        emailmessage=send_mail(mailsubject,message,email_from,recipient_list)
        
        if emailmessage:
            messages.success(request,f'User has been registered successfully , go to {email} to activate your account ! ')
            return redirect('/accounts/signin')
        else:
            messages.error(request,f'filed to send email to  {email} ! ')
            return redirect('/accounts/signup')
    else:
        return render(request,'registration/signup.html')

def check_email_availability(request):
    email = request.GET.get("email")
    response_data = {}
    if User.objects.filter(email=email).exists():
        response_data["available"] = False
    else:
        response_data["available"] = True
    return JsonResponse(response_data)

def signin(request):
    if request.user.is_authenticated:  
        return redirect('/')
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Go to'+email+'to active your account !')
                return redirect('/accounts/signin')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('/accounts/signin')
    else:
        return render(request, 'registration/signin.html')

# def log_out(request):
#     context ={'log_out' : log_out}
#     return render(request, 'registration/logged_out.html',context)

def log_out(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/accounts/login/')
def profile(request,slug):
    profile=get_object_or_404(Profile,slug=slug)
    if request.user.id == profile.user.id:
        context={'profile':profile}
        return render(request,'profile.html',context)
    else:
        return HttpResponseForbidden("You don't have permission to view this profile.")

@login_required(login_url='/accounts/login/')
def edit_profile(request ,slug):
    country_list = list(countries)
    if request.method == 'POST':
        if request.user is not None:
            user_profile = Profile.objects.get(user=request.user)
            context={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'phone': user_profile.phone,
                'country': user_profile.country,
                'country_list': country_list,
                'adress': user_profile.adress,
            }
            if request.POST['first_name'] and request.POST['last_name'] and request.POST['email'] and request.POST['phone'] and request.POST['country']  and request.POST['adress']:
                request.user.first_name= request.POST['first_name']
                request.user.last_name= request.POST['last_name']
                if request.POST['email'] != request.user.email:
                    if User.objects.filter(email=request.POST['email']).exists():
                        messages.error(request, 'Email is already taken.')
                        return render(request, 'editprofile.html', context)
                    request.user.email = request.POST['email']
                user_profile.phone= request.POST['phone']
                if 'country' in request.POST:
                    user_profile.country = request.POST['country']
                user_profile.adress= request.POST['adress']
                request.user.save()
                user_profile.save()
                messages.success(request,'Your Data Has Been Saved')
                context1={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'phone': user_profile.phone,
                'country': user_profile.country,
                'country_list': country_list,
                'adress': user_profile.adress,
                }
                slug = user_profile.slug
                return redirect ('/accounts/profile/' +slug+ '/editprofile')
            else:
                messages.error(request,'Please fill in all fields !')
                return render(request, 'editprofile.html',context)
        return render(request, 'editprofile.html',context)
    else:
        if request.user is not None:
            user_profile = Profile.objects.get(user=request.user)
            context={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'phone': user_profile.phone,
                'country': user_profile.country,
                'country_list': country_list,
                'adress': user_profile.adress,
            }
        return render(request, 'editprofile.html',context)
    
from operator import itemgetter
def order(request ,slug):
    profile=get_object_or_404(Profile,slug=slug)
    if request.user.id == profile.user.id:
        orders= Order.objects.all().filter(is_finished=True,user=request.user)
        sorted_orders = sorted(orders, key=lambda order: order.status == 'تم الشحن', reverse=True)
        context= {'sorted_orders' : sorted_orders ,}
        return render(request, 'about_me/orders.html',context)
    else:
        return HttpResponseForbidden("You don't have permission to view this profile.")

def order_details(request ,slug,pk):
    profile=get_object_or_404(Profile,slug=slug)
    if request.user.id == profile.user.id:
        # order = get_object_or_404(Order, id=pk)
        order_details = OrderDetails.objects.filter(order__id=pk)
        return render (request, 'about_me/order_details.html',{'order_details':order_details})
    else:
        return HttpResponseForbidden("You don't have permission to view this profile.")


# @login_required(login_url='/accounts/login/')
def product_favorites(request,slug):
    product_fav=Product.objects.get(slug=slug)
    if Profile.objects.filter(user=request.user,productfavorites=product_fav).exists():
        messages.error(request,'Product in favorite already')
        return redirect('/' + str(slug))
    else:
        userprofile=Profile.objects.get(user=request.user)
        userprofile.productfavorites.add(product_fav)
        messages.success(request,'Product has been favorite')
        return redirect('/' + str(slug))

# @login_required(login_url='/accounts/login/')
def showproduct_favorites(request,slug):
    profile=get_object_or_404(Profile,slug=slug)
    if request.user.id == profile.user.id:
        userinfo=Profile.objects.get(user=request.user)
        order_details=userinfo.productfavorites.all()
        context={'order_details': order_details }
        return render(request,'about_me/favorite.html',context)
    else:
        return HttpResponseForbidden("You don't have permission to view this profile.")

