from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	is_instructor = models.BooleanField(default=False)
	phone = models.IntegerField()
	gender = models.CharField(choices=GENDER, max_length=1)

	def __str__(self):
		return f'{ self.user.username } Profile'
		
	@property
	def courses(self, request):
		instance = self
		qs = Course.objects.filter(instance)
		return qs

# class IsUser(User):
# 	is_student = models.BooleanField(default=False)
# 	is_instructor = models.BooleanField(default=False)

# class InstructorProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
# 	image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

# 	def __str__(self):
# 		return self.user.username 

# 	@property
# 	def posts(self):
# 		return self.post_set.all().order_by('-date_posted')

# class StudentProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
# 	image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

# 	def __str__(self):
# 		return f'{ self.user.username } Profile'

# Create your models here.
