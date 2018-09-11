from django.db import models

class User(models.Model):
	'''This class simulates a user with a name,username and e-mail as attributes'''
	name = models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	email = models.EmailField(max_length=70) #unique=True

	def __str__(self):
		'''this function returns the name,lastname and email of the instance'''
		return self.name+" "+self.lastname+" "+self.email


class Occupation(models.Model):
	'''This class simulates an occupation with the occupation name as attribute'''
	occupation=models.CharField(max_length=200)

	def __str__(self):
		'''this function returns the occupation name of the instance'''
		return self.occupation
			
			



class Userhasoccupation(models.Model):

	'''This class simulates the connection
	 between a user and an occupation
	 .User id and occupation id are used
	  as foreign keys to the database schema'''
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	occup_id=models.ForeignKey(Occupation,on_delete=models.CASCADE)

	def __str__(self):
		'''this function returns the occupation name of the instance'''
		return str(self.user_id)+" "+str(self.occup_id)


			







