from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from core.forms import CustomerForm
from core.models import Customer


@login_required
def home(request):
    return render(request, 'home.html')

class Signup(View):
    def get(self, request):
        form = UserCreationForm(request.GET)
        print("katega")
        return render(request, 'Signup.html', {'form': form})


    def post(self,request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form})

class Index(View):
    def get(self, request):
        form = CustomerForm(request.GET)
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        print('Printing the form data...\n', form.data)

        if form.is_valid():
            print("Form is valid")
            try:
                obj = form.save(commit=False)

                cust_dict = form.data
                print('Printing the value of cust_dict = form.data...\n', cust_dict)

                obj.user = request.user
                print(obj.user)

                principal = int(cust_dict['ammount'])
                print(type(principal), 'Principal: ', principal)
                tenure = int(cust_dict['tenure'])
                print(type(tenure), 'Tenure: ', tenure)
                rate = int(cust_dict['rate'])
                print(type(rate), 'Rate: ', rate)

                amount = principal * pow((1 + rate/100), tenure)
                print(type(amount), 'Amount: ', amount)
                emi = int(amount/(tenure*12))
                print(emi)

                obj.Emi = emi
                # wtf do you wanna achieve by this
                # kuch bhi mat likh
                # cust = Customer.objects.all()
                # for customers in cust:
                #     print(customers.user)
                #     customers.rate = customers.rate / (12 * 100)
                #     customers.tol = customers.tol * 12
                #
                #     emi = (customers.amount * customers.rate * pow(1 + customers.rate, customers.tol)) / (
                #         pow(1 + customers.rate, customers.tol))


                obj.save()
                print("The Emi was saved in the database")

                return redirect('/show/')
            except:
                print("The Emi did not save in the database")
            pass

        else:
            form = CustomerForm()
        return render(request, 'index.html', {'form': form})



class Show(View):

    def get(self, request):

        print('The current user is "{}"'.format(request.user))
        Emi = Customer.objects.filter(user=request.user)
        print(Emi)
        print('Printing the loans of the user')
        for cust in Emi:
            print(cust.user, cust.Emi)

        return render(request, "show.html", {'cust': cust})
