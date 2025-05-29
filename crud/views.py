from django.shortcuts import render, redirect
from bson.objectid import ObjectId
from. import dbcon

# Create your views here.
def create_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        password = request.POST['password']
        dbcon.col.insert_one({
            'name' : name,
            'mail' : mail,
            'password' : password #store hashed password
        })
        return redirect('read_students')
    return render(request,template_name='create.html')

def read_students(request):
    students = list(dbcon.col.find())
    for student in students:
        student['id'] = str(student['_id'])
    return render(request,template_name='read.html',context={'students':students})

def update_students(request,student_id):
    student=dbcon.col.find_one({"_id":ObjectId(student_id)})
    if request.method == "POST":
        name = request.POST['name']
        mail = request.POST['mail']
        password = request.POST['password']
        dbcon.col.update_one({"_id":ObjectId(student_id)},{"$set":{'name':name,'mail':mail,'password':password}})
        return redirect('read_students')
    return render(request, template_name='update.html', context={'student':student})

def delete_student(request,student_id):
    dbcon.col.delete_one({"_id":ObjectId(student_id)})
    return redirect('read_students')
