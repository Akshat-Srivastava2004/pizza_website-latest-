from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib import messages
from .models import Feedback,CardInfo,PizzaInfo,Ordersummary
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'index.html')
    

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')  
        password = request.POST.get('unique')
        password_repeat = request.POST.get('unique01')

        if password == password_repeat:
            new_user = User.objects.create(
                username=username,
                email=email, 
            )
            new_user.set_password(password)
            new_user.save()
            subject = 'Welcome to our Website toptoppings'
            message = 'Thank you for signing up on our Website. We are excited to have you!'
            from_email = 'srivastavaakshat086@gmail.com'  
            recipient_list = [new_user.email]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect('login')
    return render(request, 'login_signup.html')
def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pword=request.POST.get('pwd')

        user=auth.authenticate(username=uname,password=pword)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,"Invalid password")
            return redirect('login')
    return render(request,'login_signup.html') 

def Home(request):
    return render(request, 'home.html')
def payment(request):
    if request.method=='POST':
        cname=request.POST.get('cname')
        cnum=request.POST.get('cnum')
        edate=request.POST.get('edate')
        cvvv=request.POST.get('cvvv')
        
        new=CardInfo.objects.create(
           cardholder_name=cname,
           card_number=cnum,
           expiry_date=edate,
           cvv=cvvv,
        )
        new.save()
        messages.success(request, "Order Placed successfully!")
    return render(request,'Payment.html')
def gallery(request):
    return render(request, 'gallery.html')
@login_required
def handle_order_post(request):
    if request.method == 'POST':
        pizza_Name = request.POST.get('pizza_Name')
        pizza_Size = request.POST.get('pizza_Size')
        pizza_price = request.POST.get('pizza_price')
        pizza_description = request.POST.get('pizza_description')

        user=request.user
        
        new_note = Ordersummary.objects.create(
            user=user,
            name=pizza_Name,
            size=pizza_Size,
            price=pizza_price,
            description=pizza_description,
        )
        new_note.save()
        return redirect('ordersummary')

def show_order_form(request):
    Pizza_detail = PizzaInfo.objects.all()
    parameter = {
        "Pizza_detail": Pizza_detail
    }
    return render(request, 'Order.html', parameter)
def Order(request):
    if request.method == 'POST':
        return handle_order_post(request)
    else:
        return show_order_form(request)
def ordersummary(request):
    user = request.user
    ordersummary = Ordersummary.objects.filter(user=user).order_by('-id')[:1]

    if request.method == 'POST':
        # Delete all previous orders, keeping only the latest one
        Ordersummary.objects.filter(user=user).exclude(id=ordersummary[0].id).delete()
        messages.success(request, "Your previous orders have been deleted, keeping the latest one.")
        return redirect('ordersummary')
    else:
        parameters = {
            "user": user,
            "ordersummary": ordersummary
        }
        return render(request, 'ordersummary.html', parameters)
def logout(request):
    auth.logout(request)
    return redirect('login')
def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')  
        subject = request.POST.get('subject')
        message= request.POST.get('message')

        new_feedback=Feedback.objects.create(
        customer_name=name,
        customer_email=email,
        title=subject,
        message=message,
        )
        new_feedback.save()
        messages.success(request, "Thank you For Your Feedback ")
        return redirect('contact')
    return render(request,'contact.html')


   
