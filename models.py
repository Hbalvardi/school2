from django.db import models
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.core.validators import MinValueValidator, MaxValueValidator
# import os

# def validate_video_file(value):
#     ext = os.path.splitext(value.name)[1]
#     valid_extensions = ['.mp4', '.mov', '.avi']
#     if  ext.lower() in valid_extensions:
#         raise ValidationError('فرمت ویدیو باید mp4 , mov یا avi باشد.')
    
# def validate_pdf_file(value):
#     ext = os.path.splitext(value.name)[1]
#     if  ext.lower() != '.pdf':
#         raise ValidationError('فرمت فایل باید pdf باشد.')

# def validate_excel_file(value):
#     ext = os.path.splitext(value.name)[1]
#     if  ext.lower() != '.xls':
#         raise ValidationError('فرمت فایل باید xls باشد.')


# class News(models.Model):
#     title = models.CharField(max_length=30)
#     text = models.TextField()
#     picture = models.ImageField(upload_to='parvareshy/picture', blank=True, null=True)
#     video = models.FileField(upload_to='parvareshy/video', blank=True, null=True, validators=[validate_video_file])
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'title : {self.title}'
    

# class Teacher(models.Model):
#     name = models.CharField(max_length=30)
#     lastname = models.TextField(blank=True, null=True)
#     description= models.TextField(blank=True, null= True)
#     pdf_file = models.FileField(upload_to='teacher/pdf', blank=True, null=True, validators=[validate_pdf_file])
#     video = models.FileField(upload_to='teacher/video', blank=True, null=True, validators=[validate_video_file])
    
#     def __str__(self):
#         return f'title : {self.title}'

# class Classes(models.Model):
#     grade = models.PositiveIntegerField(validators=[MinValueValidator(7), MaxValueValidator(12)])
#     name = models.CharField(max_length=13)

#     def __str__(self):
#         return f'name : {self.name}'
    
# class Students(models.Model):
#     first_name = models.CharField(max_length=15)
#     last_name = models.CharField(max_length=17)
#     national_number = models.CharField(max_length=10)
#     class_name = models.ForeignKey(Classes, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.first_name}  {self.last_name}'
