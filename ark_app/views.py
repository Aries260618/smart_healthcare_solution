from django.shortcuts import render,redirect
from .models import *
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def otp(request,otp_for=None):
    try:
        otp_num = random.randint(1000, 9999)
        print(f"\n\n\n --- OTP NUMBER :- {otp_num} --- \n\n\n")
        
        request.session['otp'] = otp_num
        
        print(request.session['email'])
        
        email_to_list = [request.session['email'],]

        subject = f"OTP for {otp_for} in ARK."

        email_from = settings.EMAIL_HOST_USER
        print(email_from)
        
        message = f"Your One Time Password For Verification is * {otp_num} * . Please Don't Share to any other."
        
        send_mail(subject, message, email_from, email_to_list)
        
    
    except Exception as e:
        print(f"\n\n\n{e}\n\n\n")
        
def verify_otp(request):
    email = request.session['email']

    if request.session['otp'] == int(request.POST['otp']):
        master = Patient.objects.get(email=email)
        master.IsActive = True
        master.save()
        return redirect(profile_settings)
    else:
        print("Invalid OTP...")
        msg = "Invalid OTP..."
        return render(request,"otp.html",{'msg':msg})
        
def doc_verify_otp(request):
    email = request.session['email']

    if request.session['otp'] == int(request.POST['otp']):
        master = Doctor.objects.get(email=email)
        master.IsActive = True
        master.save()
        return redirect(doctor_profile_settings)
    else:
        print("Invalid OTP...")
        msg = "Invalid OTP..."
        return render(request,"doc_otp.html",{'msg':msg})

def index(request):
    doctor = Doctor.objects.all()
    return render(request, "index.html",{'doctor':doctor})

def doctor_login(request):
    if request.method == "POST":
        try:
            doctor = Doctor.objects.get(email = request.POST['email'])

            if doctor.password == request.POST['password']:
    
                request.session['clinic_name'] = doctor.clinic_name
                request.session['email'] = doctor.email
                if doctor.IsActive == True:
                    return redirect(doctor_profile_settings)
                else:
                    otp(request,"Doctor Login")
                    return redirect(doc_otp)
        except:
            msg = 'Invalid Email or Password'
            return render(request,'doctor_login.html',{'msg_d':msg})
    else:
        return render(request,"doctor_login.html")

def login(request):
    if request.method == "POST":
        try:
            patient = Patient.objects.get(email = request.POST['email'])
            
            if patient.password == request.POST['password']:

                request.session['email'] = patient.email
                if patient.IsActive == True:
                    return redirect(profile_settings)
                else:
                    otp(request,"LOGIN")
                    return redirect(otp_page)
        except:
            msg = 'Invalid Email or Password'
            return render(request,'login.html',{'msg_d':msg})
    else:
        return render(request, "login.html")

def doctor_register(request):
    degrees = [degree for degree in Degree.objects.all()]

    if request.method == "POST":
        
        try:
            
            doctor = Doctor.objects.get(email = request.POST['email'])
            msg = 'User Already Exists'

            return render(request,'doctor_login.html',{'msg_d':msg})
        except:
            
            try:
                if request.POST['name'] == "" or request.POST['email'] == "" or request.POST['address'] == "" or request.POST['degree'] == "" or request.POST['clinic_name'] == "" or request.POST['clinic_address'] == "" or request.POST['password'] == "" or request.POST['confirm_password'] == "":
                    
                    msg = 'All Fields Are Mandatory'
                    return render(request,'doctor_register.html',{'msg_d':msg})

                elif request.POST['password'] == request.POST['confirm_password']:

                    degree = Degree.objects.get(id=int(request.POST['degree']))            

                    doctor = Doctor.objects.create(
                        name = request.POST['name'],
                        email = request.POST['email'],
                        address = request.POST['address'],
                        degree = degree,
                        clinic_name = request.POST['clinic_name'],
                        clinic_address = request.POST['clinic_address'],
                        password = request.POST['password']
                    )

                    doctor.save()
                    msg = 'Sign Up Was SuccessFull'
                    return render(request, "doctor_login.html",{'msg_s':msg})
                else:

                    print('\n\n\n stage 5 \n\n\n')

                    msg = "Password And Confirm Password Does Not Matched"
                    return render(request,'doctor_register.html',{'msg_d':msg})
            except:

                print('\n\n\n stage 6 \n\n\n')
                msg = "Opps ! Something Went Wrond , Please Trey Again Later.."
                return render(request,'doctor_register.html',{'msg_d':msg})
    else:
        return render(request,'doctor_register.html',{"degrees":degrees})

def register(request):
    if request.method == "POST":
        try:              
            patient = Patient.objects.get(email = request.POST['email'])
            msg = 'User Already Exist'

            return render(request, 'login.html',{'msg_d':msg})

        except:
            try:
                if request.POST['name'] == "" or request.POST['email'] == "" or request.POST['address'] == "" or request.POST['password'] == "" or request.POST['confirm_password'] == "":
                    msg = 'All Fields Are Mandatory'

                    return render(request, 'register.html', {'msg_d':msg})

                elif request.POST['password'] == request.POST['confirm_password']:

                    patient = Patient.objects.create(
                        name = request.POST['name'], 
                        email = request.POST['email'], 
                        address = request.POST['address'], 
                        password = request.POST['password'] 
                    )

                    patient.save()
                    msg = 'Sign Up Was SuccessFull'

                    return render(request,'login.html',{'msg_s':msg})

                else:
                    msg = 'Password And Confirm Password Does Not Matched..'
                    return render(request,'register.html',{'msg_d':msg})
            except:
                msg = 'Opps ! Something Went Wrong. Please Try Again Later'
                return render(request,'register.html',{'msg_d':msg})
    else:
        return render(request, "register.html")

def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html")

def doc_profile_update(request):
    try:
        doctor = Doctor.objects.get(email=request.session['email'])
        doctor.name = request.POST['name']
        doctor.address = request.POST['address']
        doctor.city = request.POST['city']
        doctor.state = request.POST['state']
        doctor.country = request.POST['country']
        doctor.pin = request.POST['pin']
        doctor.mobile = request.POST['mobile']
        doctor.gender = request.POST['gender']
        doctor.dob = request.POST['dob']
        doctor.description = request.POST['description']
        doctor.dob = doctor.dob.strftime("%Y-%m-%d")
        doctor.save()
        msg = 'Profile Updated SuccessFully'
        print(msg)
        return redirect(doctor_profile_settings)
    except Exception as e:
        msg = 'Something Went Wrong! Please Try Again Later..'
        print(e)
        return render(request,'doctor_profile_settings.html',{'msg':msg,'doctor':doctor})

def doctor_profile_settings(request):
    doctor = Doctor.objects.get(email=request.session['email'])
    gender = []
    for k,v in gender_choice:
        gender.append(
            {'short_tag':k, 'text':v}
        )
    print(gender)
    print('\n\n\n',doctor.dob)
    return render(request, "doctor_profile_settings.html",{'doctor':doctor,'gender':gender})

def appointments(request):
    return render(request, "appointments.html")

def patient_list(request):
    return render(request, "patient_list.html")

def patient_profile(request):
    return render(request, "patient_profile.html")

def invoices(request):
    return render(request, "invoices.html")

def search(request):
    doctor = Doctor.objects.all()
    count = 0
    count += len(doctor)
        
        
    return render(request, "search.html",{'doctor':doctor,'count':count})

def booking(request):
    return render(request, "booking.html")

def checkout(request):
    return render(request, "checkout.html")

def booking_success(request):
    return render(request, "booking_success.html")

def invoice_view(request):
    return render(request, "invoice_view.html")

def profile_settings(request):
    patient = Patient.objects.get(email = request.session['email'])
    gender = []
    for k,v in gender_choice:
        gender.append(
            {'short_tag':k, 'text':v}
        )
    print(gender)
    return render(request, "profile_settings.html",{'patient':patient,'gender':gender})

def change_password(request):
    return render(request, "change_password.html")

def contact_us(request):
    return render(request, "contact_us.html")

def logout(request):
    if 'email' in request.session:
        master = Patient.objects.get(email = request.session['email'])
        master.IsActive = False
        master.save()
        del request.session['email']
    return redirect(index)

def doctor_logout(request):
    if 'clinic_name' in request.session:
        master = Doctor.objects.get(email = request.session['email'])
        master.IsActive = False
        master.save()
        del request.session['clinic_name']
        del request.session['email']
    return redirect(index)

def otp_page(request):
    return render(request, "otp.html")

def doc_otp(request):
    return render(request,'doc_otp.html')