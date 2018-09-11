from django.shortcuts import render,redirect, get_object_or_404
from joblist.models import User, Occupation, Userhasoccupation
from fm.views import AjaxCreateView,AjaxUpdateView,AjaxDeleteView
from .forms import UserForm,OccupationForm,UserhasoccupationForm
from django.urls import reverse_lazy
from joblist.utility_functions import string_manipulation



# Render the HTML template index.html with the data in the context variable
def index(request):
	template_name="index.html"
	# Generate counts of users
	num_users = User.objects.all().count()
    # Generate counts of occupations
	num_occupations = User.objects.all().count()
    # Generate counts of connections
	num_connections = Userhasoccupation.objects.all().count()
	context = {
        'num_users': num_users,
        'num_occupations': num_occupations,
        'num_connections': num_connections,
    }
	return render(request,template_name,context=context)


#user list
def user_list(request):
    users = User.objects.all()
    template_name='user_list.html'
    context = {'users': users}
    return render(request, template_name, context)


# user view
def user_view(request, pk, template_name='user_detail.html'):
	user= get_object_or_404(User, pk=pk)
	occupations = Userhasoccupation.objects.filter(user_id=user.id)
	return render(request, template_name, {'object':user,'occupations':occupations})
	
    
#occupation list
def occupation_list(request):
    occupations = Occupation.objects.all()
    template_name='occupation_list.html'
    context = {'occupations': occupations}
    return render(request, template_name, context)

# occupation view
def occupation_view(request, pk, template_name='occupation_detail.html'):
    occupation= get_object_or_404(Occupation, pk=pk)    
    return render(request, template_name, {'object':occupation})


#userhasoccupation list
def userhasoccupation_list(request):
    userhasoccupations = Userhasoccupation.objects.all()
    template_name='userhasoccupation_list.html'
    context = {'userhasoccupations': userhasoccupations}
    return render(request, template_name, context)



### CRUD USERS ###
class UserCreateView(AjaxCreateView):
	model=User
	form_class = UserForm


class UserUpdateView(AjaxUpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')

class UserDeleteView(AjaxDeleteView):
    model = User
    success_url = reverse_lazy('users')

### CRUD OCCUPATIONS ###
class OccupationCreateView(AjaxCreateView):
	model=Occupation
	form_class = OccupationForm


class OccupationUpdateView(AjaxUpdateView):
    model = Occupation
    form_class = OccupationForm
    success_url = reverse_lazy('occupations')

class OccupationDeleteView(AjaxDeleteView):
    model = Occupation
    success_url = reverse_lazy('occupations')


### CRUD USERHASOCCUPATIONS ###
class UserhasoccupationCreateView(AjaxCreateView):
	model=Userhasoccupation
	form_class = UserhasoccupationForm


class UserhasoccupationUpdateView(AjaxUpdateView):
    model = Userhasoccupation
    form_class = UserhasoccupationForm
    success_url = reverse_lazy('userhasoccupations')

class UserhasoccupationDeleteView(AjaxDeleteView):
    model = Userhasoccupation
    success_url = reverse_lazy('userhasoccupations')



# def new_connection(request):
# 	occupations = Occupation.objects.all() #fetch all the occupations from the db
# 	template='new_connection.html'
# 	user_message = ''
# 	if request.method=='POST':
# 		#fetch and check name
# 		name = request.POST.get('your_name')
# 		checked_name=string_manipulation.check_string(name)
# 		#fetch and check lastname
# 		lastname = request.POST.get('your_lastname')
# 		checked_lastname=string_manipulation.check_string(lastname)
# 		#fetch email
# 		email=request.POST.get('your_email')

# 		### CREATION OF INSTANCES(USER,OCCUPATION,USERHASOCCUPATION) WITHOUT CHECK ###
# 		# occupation=request.POST.get('occupations_option')
# 		# if occupation:
# 		# 	user_instance=User.objects.create(name=checked_name,lastname=checked_lastname,email=email)
# 		# 	occup_instance=Occupation.objects.create(occupation=occupation)
# 		# 	uho_instance=Userhasoccupation.objects.create(occup_id=occup_instance,user_id=user_instance)
# 		# 	user_message = "You fill out correctly the fields"
# 		# else:
# 		# 	user_message = "You need to fullfill the occupation field!!!"

# 		### CREATION OF INSTANCES(USER,OCCUPATION,USERHASOCCUPATION) WITH CHECK ###
# 		if (checked_name=="Please give a valid string!!!" and checked_lastname=="Please give a valid string!!!"):
# 			user_message="Please fill out correctly all the fields!!!"
# 			return render(request,template,{'occupations': occupations, 'message':user_message})
# 		if(checked_name=="Please give a valid string!!!"):
# 			u_message=checked_name+"\n You need to fill out a name without numbers or spaces at the beginning or end"     
# 			return render(request,template,{'occupations': occupations, 'message':u_message})
# 		if(checked_lastname=="Please give a valid string!!!"):
# 			u_message=checked_lastname+"\n You need to fill out a lastname without numbers or spaces at the beginning or end"     
# 			return render(request,template,{'occupations': occupations, 'message':u_message})
# 		else: 
# 			request.POST.get('occupations_option')
# 			occupation = request.POST.get('occupations_option')
# 			print(occupation)
# 			print(type(occupation))
# 		if occupation:
# 			user_instance=User.objects.create(name=checked_name,lastname=checked_lastname,email=email)
# 			occup_instance=Occupation.objects.create(occupation=occupation)
# 			uho_instance=Userhasoccupation.objects.create(occup_id=occup_instance,user_id=user_instance)
# 			user_message = "You fill out correctly the fields!!!"
# 		else:
# 			user_message = "You need to fullfill the occupation field!!!"
# 	return render(request,template,{'occupations': occupations, 'message':user_message})


def new_connection(request):
	occupations = Occupation.objects.all() #fetch all the occupations from the db
	template='new_connection.html'
	user_message = ''
	if request.method=='POST':
		#fetch and check name
		name = request.POST.get('your_name')
		checked_name=string_manipulation.check_string(name)
		#fetch and check lastname
		lastname = request.POST.get('your_lastname')
		checked_lastname=string_manipulation.check_string(lastname)
		#fetch email
		email=request.POST.get('your_email')

		### CREATION OF INSTANCES(USER,OCCUPATION,USERHASOCCUPATION) WITHOUT CHECK ###
		# occupation=request.POST.get('occupations_option')
		# if occupation:
		# 	user_instance=User.objects.create(name=checked_name,lastname=checked_lastname,email=email)
		# 	occup_instance=Occupation.objects.create(occupation=occupation)
		# 	uho_instance=Userhasoccupation.objects.create(occup_id=occup_instance,user_id=user_instance)
		# 	user_message = "You fill out correctly the fields"
		# else:
		# 	user_message = "You need to fullfill the occupation field!!!"

		### CREATION OF INSTANCES(USER,OCCUPATION,USERHASOCCUPATION) WITH CHECK ###
		if (checked_name=="Please give a valid string!!!" and checked_lastname=="Please give a valid string!!!"):
			user_message="Please fill out correctly all the fields!!!"
			return render(request,template,{'occupations': occupations, 'message':user_message})
		if(checked_name=="Please give a valid string!!!"):
			u_message=checked_name+"\n You need to fill out a name without numbers or spaces at the beginning or end"     
			return render(request,template,{'occupations': occupations, 'message':u_message})
		if(checked_lastname=="Please give a valid string!!!"):
			u_message=checked_lastname+"\n You need to fill out a lastname without numbers or spaces at the beginning or end"     
			return render(request,template,{'occupations': occupations, 'message':u_message})
		else: 
			request.POST.getlist('occupations_option')
			occupation_list = request.POST.getlist('occupations_option')
			print(occupation_list)
			print(type(occupation_list))
		user_instance=User.objects.create(name=checked_name,lastname=checked_lastname,email=email)
		if occupation_list:
			for current_occupation in occupation_list:
				# occup_instance=Occupation.objects.create(occupation=occupation)
				occup_instance=Occupation.objects.get(occupation=current_occupation)

				# return id of occupation with name =current_occupation

				uho_instance=Userhasoccupation.objects.create(occup_id=occup_instance,user_id=user_instance)
				user_message = "You fill out correctly the fields!!!"
		else:
			user_message = "You need to fullfill the occupation field!!!"
	return render(request,template,{'occupations': occupations, 'message':user_message})