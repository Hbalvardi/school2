from django.shortcuts import render, redirect
# from .forms import Teacher_form , Classes_form , News_form

def home(request):
    return render(request,'index.html')

# def blog_detail(request):
#     return render(request,'blog-detail.html')

# def manage_students(request):
#     return render(request,'manage-students.html')

# def messages(request):
#     return render(request,'messages.html')


# def home(request):
#     return render(request, 'home-3.html')

# def base(request):
#     return render(request,'base.html')
     
     
# def teacher(request):
#     if request.method == 'POST':
#         form = Teacher_form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_list')  
#     else:
#         form = Teacher_form()
    
#     return render(request, 'teacher-action.html', {'form': form})


# def news(request):
#     if request.method == 'POST':
#         form = News_form(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher_list')  
#     else:
#         form = News_form()
    
#     return render(request, 'blog-detail.html', {'form': form})



# def create_class(request):
#     if request.method == 'POST':
#         form = Classes_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('class_list') 
#     else:
#         form = Classes_form()
    
#     return render(request, 'manage-students.html', {'form': form})