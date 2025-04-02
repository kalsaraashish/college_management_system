import json
import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

from college_management_app.models import CustomUser, Courses, Subjects, Staffs, Students, Attendance, LeaveReportStaff, \
    AttendanceReport, LeaveReportStudent, StudentNotice, StaffNotice

from django.urls import reverse

from college_management_app.forms import AddStudentForm, EditStudentForm

from college_management_app.models import SessionYearModel
from django.views.decorators.csrf import csrf_exempt


def admin_home(request):
    student_count1=Students.objects.all().count()
    staff_count=Staffs.objects.all().count()
    subject_count=Subjects.objects.all().count()
    course_count=Courses.objects.all().count()

    course_all=Courses.objects.all()
    course_name_list=[]
    subject_count_list=[]
    student_count_list_in_course=[]
    for course in course_all:
        subjects=Subjects.objects.filter(course_id=course.id).count()
        students=Students.objects.filter(course_id=course.id).count()
        course_name_list.append(course.course_name)
        subject_count_list.append(subjects)
        student_count_list_in_course.append(students)

    subjects_all=Subjects.objects.all()
    subject_list=[]
    student_count_list_in_subject=[]
    for subject in subjects_all:
        course = Courses.objects.filter(id=subject.course_id.id).first()  # Avoids exception
        if course:  # Ensures course exists before proceeding
            student_count = Students.objects.filter(course_id=course.id).count()
            subject_list.append(subject.subject_name)
            student_count_list_in_subject.append(student_count)
        else:
            print(f"Warning: Course not found for subject {subject.subject_name}")

    staffs=Staffs.objects.all()
    attendance_present_list_staff=[]
    attendance_absent_list_staff=[]
    staff_name_list=[]
    for staff in staffs:
        if staff.admin:  # Ensure admin exists before accessing its ID and username
            subject_ids = Subjects.objects.filter(staff_id=staff.admin.id)
            attendance = Attendance.objects.filter(subject_id__in=subject_ids).count()
            leaves = LeaveReportStaff.objects.filter(staff_id=staff.id, leave_status=1).count()

            attendance_present_list_staff.append(attendance)
            attendance_absent_list_staff.append(leaves)
            staff_name_list.append(staff.admin.username)
        else:
            print(f"Warning: Staff {staff.id} does not have an associated CustomUser.")

    students_all=Students.objects.all()
    attendance_present_list_student=[]
    attendance_absent_list_student=[]
    student_name_list=[]
    for student in students_all:
        attendance=AttendanceReport.objects.filter(student_id=student.id,status=True).count()
        absent=AttendanceReport.objects.filter(student_id=student.id,status=False).count()
        leaves=LeaveReportStudent.objects.filter(student_id=student.id,leave_status=1).count()
        attendance_present_list_student.append(attendance)
        attendance_absent_list_student.append(leaves+absent)
        student_name_list.append(student.admin.username)



    return render(request,"hod_template/home_content.html",{"student_count":student_count1,"staff_count":staff_count,"subject_count":subject_count,"course_count":course_count,"course_name_list":course_name_list,"subject_count_list":subject_count_list,"student_count_list_in_course":student_count_list_in_course,"student_count_list_in_subject":student_count_list_in_subject,"subject_list":subject_list,"staff_name_list":staff_name_list,"attendance_present_list_staff":attendance_present_list_staff,"attendance_absent_list_staff":attendance_absent_list_staff,"student_name_list":student_name_list,"attendance_present_list_student":attendance_present_list_student,"attendance_absent_list_student":attendance_absent_list_student})

def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        mobile_number = request.POST.get("mobile_number")

        if 'profile_pic' in request.FILES:
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.staffs.mobile_number = mobile_number
            user.staffs.profile_pic = profile_pic
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))

def add_course(request):
    return render(request,"hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get("course")

        # Check if the course already exists
        if Courses.objects.filter(course_name=course).exists():
            messages.error(request, "Course already exists!")
            return HttpResponseRedirect(reverse("add_course"))

        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully Added Course")
        except:
            messages.error(request, "Failed To Add Course")

        return HttpResponseRedirect(reverse("add_course"))

def add_student(request):
    # courses=Courses.objects.all()
    form=AddStudentForm()
    return render(request,"hod_template/add_student_template.html",{"form":form})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            session_year_id = form.cleaned_data["session_year_id"]
            course_id = form.cleaned_data["course"]
            sex = form.cleaned_data["sex"]
            mobile_number = form.cleaned_data.get("mobile_number", "")  # Get mobile number safely

            # Handling profile picture upload to "student_pics" folder
            profile_pic = request.FILES.get("profile_pic", None)
            if profile_pic:
                fs = FileSystemStorage(location="media/student_pics")
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = f"student_pics/{filename}"  # Store relative path, not absolute URL
            else:
                profile_pic_url = "student_pics/default.jpg"  # Keep consistent with default

            user = CustomUser.objects.create_user(
                username=username, password=password, email=email,
                last_name=last_name, first_name=first_name, user_type=3
            )
            user.students.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.students.course_id = course_obj
            session_year = SessionYearModel.object.get(id=session_year_id)
            user.students.session_year_id = session_year
            user.students.gender = sex
            user.students.profile_pic = profile_pic_url
            user.students.mobile_number = mobile_number  # Save mobile number

            user.save()

            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        else:
            return render(request, "hod_template/add_student_template.html", {"form": form})


def add_subject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/add_subject_template.html",{"staffs":staffs,"courses":courses})

def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject=Subjects(subject_name=subject_name,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Subject")
            return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.error(request, "Failed to Add Subject")
            return HttpResponseRedirect(reverse("add_subject"))

def manage_staff(request):
    query = request.GET.get('q', '')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # AJAX request
        staffs = Staffs.objects.filter(
            Q(admin__first_name__icontains=query) |
            Q(admin__last_name__icontains=query) |
            Q(admin__username__icontains=query)
        )

        staff_list = [
            {
                'id': staff.admin.id,
                'first_name': staff.admin.first_name,
                'last_name': staff.admin.last_name,
                'username': staff.admin.username,
                'profile_pic': staff.profile_pic.url if staff.profile_pic else None,
                'email': staff.admin.email,
                'mobile_number': staff.mobile_number,
                'address': staff.address,
                'last_login': staff.admin.last_login.strftime('%Y-%m-%d %H:%M:%S') if staff.admin.last_login else "Never",
                'date_joined': staff.admin.date_joined.strftime('%Y-%m-%d'),
                'edit_url': f"/edit_staff/{staff.admin.id}/",
                'delete_url': f"/delete_staff/{staff.id}/"
            } for staff in staffs
        ]
        return JsonResponse({'staffs': staff_list})

    staffs = Staffs.objects.all()
    return render(request, 'hod_template/manage_staff_template.html', {'staffs': staffs})

def manage_student(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Check if it's an AJAX request
        query = request.GET.get('q', '').strip()
        students = Students.objects.filter(
            Q(admin__first_name__icontains=query) |
            Q(admin__last_name__icontains=query) |
            Q(admin__username__icontains=query)
        )[:10]  # Limit results

        student_data = []
        for student in students:
            student_data.append({
                "id": student.id,
                "first_name": student.admin.first_name,
                "last_name": student.admin.last_name,
                "username": student.admin.username,
                "email": student.admin.email,
                "mobile_number": student.mobile_number,
                "address": student.address,
                "gender": student.gender,
                "profile_pic": student.profile_pic.url if student.profile_pic else "",
                "session_year": f"{student.session_year_id.session_start_year} TO {student.session_year_id.session_end_year}",
                "course": student.course_id.course_name,
                "last_login": student.admin.last_login.strftime('%Y-%m-%d %H:%M:%S') if student.admin.last_login else "Never",
                "date_joined": student.admin.date_joined.strftime('%Y-%m-%d'),
                "edit_url": f"/edit_student/{student.admin.id}/",
                "delete_url": f"/delete_student/{student.id}/"
            })

        return JsonResponse({"students": student_data})

    # Normal Page Load
    students = Students.objects.all()
    return render(request, 'hod_template/manage_student_template.html', {'students': students})

def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "hod_template/manage_course_template.html", {"courses": courses})

def manage_subject(request):
    subjects = Subjects.objects.all()
    return render(request, "hod_template/manage_subject_template.html", {"subjects": subjects})

def edit_staff(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff_template.html",{"staff":staff,"id":staff_id})

def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        staff_id=request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        mobile_number = request.POST.get("mobile_number")
        print("FILES RECEIVED:", request.FILES)
        try :
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.mobile_number=mobile_number

            # Check if a new profile picture was uploaded
            if 'profile_pic' in request.FILES:
                profile_pic = request.FILES['profile_pic']
                print(profile_pic)

                # Store in 'media/staff_pics/' instead of default location
                fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'staff_pics'))

                # Remove old profile picture if it exists
                if staff_model.profile_pic:
                    old_pic_path = os.path.join(settings.MEDIA_ROOT, str(staff_model.profile_pic))
                    if os.path.exists(old_pic_path):
                        os.remove(old_pic_path)

                # Save the new file
                filename = fs.save(profile_pic.name, profile_pic)

                # Store relative path in the database (not a full URL)
                staff_model.profile_pic = f'staff_pics/{filename}'

            staff_model.save()

            messages.success(request, "Successfully Edited Staff")
            return HttpResponseRedirect(reverse("manage_staff"))
        except:
            messages.error(request, "Failed to Edit Staff")
            return HttpResponseRedirect(reverse("manage_staff"))


def delete_staff(request, staff_id):
    try:
        staff = Staffs.objects.get(id=staff_id)
        staff.delete()
        messages.success(request, "Staff deleted successfully!")
    except Staffs.DoesNotExist:
        messages.error(request, "Staff not found!")
    except Exception as e:
        messages.error(request, f"Failed to delete staff: {str(e)}")

    return HttpResponseRedirect(reverse("manage_staff"))


def edit_student(request,student_id):
    request.session['student_id']=student_id
    # courses=Courses.objects.all()
    student = Students.objects.get(admin=student_id)
    form=EditStudentForm()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['address'].initial = student.address
    form.fields['mobile_number'].initial = student.mobile_number
    form.fields['course'].initial = student.course_id.id
    form.fields['sex'].initial = student.gender
    form.fields['session_year_id'].initial = student.session_year_id.id
    return render(request, "hod_template/edit_student_template.html",{"form":form,"id":student_id,"username":student.admin.username})

def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")

    student_id = request.session.get("student_id")
    if student_id is None:
        return HttpResponseRedirect(reverse("manage_student"))

    form = EditStudentForm(request.POST, request.FILES)
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        address = form.cleaned_data["address"]
        mobile_number = form.cleaned_data.get("mobile_number", "")
        session_year_id = form.cleaned_data["session_year_id"]
        course_id = form.cleaned_data["course"]
        sex = form.cleaned_data["sex"]

        try:
            # Update CustomUser (linked to student)
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            # Update student details
            student = Students.objects.get(admin=student_id)
            student.address = address
            student.mobile_number = mobile_number
            session_year = SessionYearModel.object.get(id=session_year_id)
            student.session_year_id = session_year
            student.gender = sex
            course = Courses.objects.get(id=course_id)
            student.course_id = course

            # Handling profile picture upload
            if 'profile_pic' in request.FILES:
                profile_pic = request.FILES['profile_pic']

                # Save in "media/student_pics" folder
                fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'student_pics'))

                # Remove old profile picture if it exists
                if student.profile_pic:
                    old_pic_path = os.path.join(settings.MEDIA_ROOT, str(student.profile_pic))
                    if os.path.exists(old_pic_path):
                        os.remove(old_pic_path)

                # Save the new profile picture
                filename = fs.save(profile_pic.name, profile_pic)

                # Store the relative path in the database
                student.profile_pic = f'student_pics/{filename}'

            student.save()
            del request.session['student_id']

            # Success message
            messages.success(request, "Successfully Edited Student")
            return HttpResponseRedirect(reverse("manage_student"))

        except Exception as e:
            print(f"Error occurred: {e}")
            messages.error(request, "Failed to Edit Student")
            return HttpResponseRedirect(reverse("manage_student"))

    else:
        form = EditStudentForm(request.POST)
        student = Students.objects.get(admin=student_id)
        return render(request, "hod_template/edit_student_template.html",
                      {"form": form, "id": student_id, "username": student.admin.username})


def delete_student(request, student_id):
    try:
        student = Students.objects.get(id=student_id)
        student.delete()
        messages.success(request, "Student deleted successfully!")
    except Students.DoesNotExist:
        messages.error(request, "Student not found!")
    except Exception as e:
        messages.error(request, f"Failed to delete student: {str(e)}")

    return HttpResponseRedirect(reverse("manage_student"))


def edit_subject(request,subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/edit_subject_template.html",{"subject":subject,"staffs":staffs,"courses":courses,"id":subject_id})


def edit_subject_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject.staff_id=staff
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()
            messages.success(request, "Successfully Edited Subject")
            return HttpResponseRedirect(reverse("manage_subject"))
        except:
            messages.error(request, "Failed to Edit Subject")
            return HttpResponseRedirect(reverse("manage_subject"))

def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course_template.html",{"course":course,"id":course_id})

def edit_course_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course")
        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()
            messages.success(request, "Successfully Edited Course")
            return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id":course_id}))
        except:
            messages.error(request, "Failed to Edit Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))

def manage_session(request):
    session_years = SessionYearModel.object.all()
    return render(request, "hod_template/manage_session_template.html", {"session_years": session_years})

def add_session_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("manage_session"))
    else:
        session_start_year=request.POST.get("session_start")
        session_end_year = request.POST.get("session_end")

        try:
            sessionyear=SessionYearModel(session_start_year=session_start_year,session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Successfully Added Session")
            return HttpResponseRedirect(reverse("manage_session"))

        except:
            messages.error(request, "Failed to Added Session")
            return HttpResponseRedirect(reverse("manage_session"))

def edit_session_year(request, session_id):
    if request.method == "POST":
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")

        try:
            session = SessionYearModel.object.get(id=session_id)
            session.session_start_year = session_start
            session.session_end_year = session_end
            session.save()
            messages.success(request, "Session Year Updated Successfully!")
        except SessionYearModel.DoesNotExist:
            messages.error(request, "Session Year Not Found!")
        except Exception as e:
            messages.error(request, f"Failed to Update Session Year: {str(e)}")

        return HttpResponseRedirect(reverse("manage_session"))

    else:
        session = SessionYearModel.object.get(id=session_id)
        return render(request, "hod_template/edit_session_year_template.html", {"session": session})


def delete_session_year(request, session_id):
    try:
        session = SessionYearModel.object.get(id=session_id)
        session.delete()
        messages.success(request, "Session Year Deleted Successfully!")
    except SessionYearModel.DoesNotExist:
        messages.error(request, "Session Year Not Found!")
    except Exception as e:
        messages.error(request, f"Failed to Delete Session Year: {str(e)}")

    return HttpResponseRedirect(reverse("manage_session"))


@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def staff_feedback_message(request):
    from college_management_app.models import FeedBackStaffs
    feedbacks=FeedBackStaffs.objects.all()
    return render(request,"hod_template/staff_feedback_template.html",{"feedbacks":feedbacks})

def student_feedback_message(request):
    from college_management_app.models import FeedBackStudent
    feedbacks=FeedBackStudent.objects.all()
    return render(request,"hod_template/student_feedback_template.html",{"feedbacks":feedbacks})


@csrf_exempt
def student_feedback_message_replied(request):
    from college_management_app.models import  FeedBackStudent
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


@csrf_exempt
def staff_feedback_message_replied(request):
    from college_management_app.models import FeedBackStaffs
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStaffs.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

def staff_leave_view(request):
    from college_management_app.models import LeaveReportStaff
    leaves=LeaveReportStaff.objects.all()
    return render(request,"hod_template/staff_leave_view.html",{"leaves":leaves})

def student_leave_view(request):
    from college_management_app.models import LeaveReportStudent
    leaves=LeaveReportStudent.objects.all()
    return render(request,"hod_template/student_leave_view.html",{"leaves":leaves})

def student_approve_leave(request,leave_id):
    from college_management_app.models import LeaveReportStudent
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view"))

def student_disapprove_leave(request,leave_id):
    from college_management_app.models import LeaveReportStudent
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("student_leave_view"))

def staff_approve_leave(request,leave_id):
    from college_management_app.models import LeaveReportStaff
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_view"))

def staff_disapprove_leave(request,leave_id):
    from college_management_app.models import LeaveReportStaff
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("staff_leave_view"))

def admin_view_attendance(request):
    subjects=Subjects.objects.all()
    session_year_id=SessionYearModel.object.all()
    return render(request,"hod_template/admin_view_attendance.html",{"subjects":subjects,"session_year_id":session_year_id})

@csrf_exempt
def admin_get_attendance_dates(request):
    from college_management_app.models import Attendance
    subject=request.POST.get("subject")
    session_year_id=request.POST.get("session_year_id")
    subject_obj=Subjects.objects.get(id=subject)
    session_year_obj=SessionYearModel.object.get(id=session_year_id)
    attendance=Attendance.objects.filter(subject_id=subject_obj,session_year_id=session_year_obj)
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date),"session_year_id":attendance_single.session_year_id.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj),safe=False)


@csrf_exempt
def admin_get_attendance_student(request):
    from college_management_app.models import Attendance,AttendanceReport
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    list_data=[]

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"hod_template/admin_profile.html",{"user":user})


def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            # if password!=None and password!="":
            #     customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))

def delete_subject(request, subject_id):
    try:
        subject = Subjects.objects.get(id=subject_id)
        subject.delete()
        messages.success(request, "Subject Deleted Successfully!")
    except Subjects.DoesNotExist:
        messages.error(request, "Subject Not Found!")
    except Exception as e:
        messages.error(request, f"Failed to Delete Subject: {str(e)}")

    return HttpResponseRedirect(reverse("manage_subject"))  # Redirect to manage_subject_template.html

def delete_course(request, course_id):
    try:
        course = Courses.objects.get(id=course_id)
        course.delete()
        messages.success(request, "Course Deleted Successfully!")
    except Courses.DoesNotExist:
        messages.error(request, "Course Not Found!")
    except Exception as e:
        messages.error(request, f"Failed to Delete Course: {str(e)}")

    return HttpResponseRedirect(reverse("manage_course"))  # Redirect to manage course page


def add_student_notice(request):
    notices = StudentNotice.objects.all()
    return render(request, "hod_template/add_student_notice.html",{"notices":notices})

def add_student_notice_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")

        try:
            notice = StudentNotice(title=title, content=content)
            notice.save()
            messages.success(request, "Successfully Added Notice")
            return HttpResponseRedirect(reverse("add_student_notice"))
        except:
            messages.error(request, "Failed to Add Notice")
            return HttpResponseRedirect(reverse("add_student_notice"))

def view_student_notices(request):
    notices = StudentNotice.objects.all().order_by('-created_at')
    return render(request, 'hod_template/view_student_notices.html', {'notices': notices})


def edit_student_notice(request, notice_id):
    try:
        notice = StudentNotice.objects.get(id=notice_id)
    except StudentNotice.DoesNotExist:
        messages.error(request, "Notice Not Found!")
        return HttpResponseRedirect(reverse("add_student_notice"))

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        try:
            notice.title = title
            notice.content = content
            notice.save()
            messages.success(request, "Notice Updated Successfully!")
        except Exception as e:
            messages.error(request, f"Failed to Update Notice: {str(e)}")

        return HttpResponseRedirect(reverse("view_student_notices"))

    return render(request, "hod_template/edit_student_notice_template.html", {"notice": notice})


def delete_student_notice(request, notice_id):
    try:
        notice = StudentNotice.objects.get(id=notice_id)
        notice.delete()
        messages.success(request, "Notice Deleted Successfully!")
    except StudentNotice.DoesNotExist:
        messages.error(request, "Notice Not Found!")
    except Exception as e:
        messages.error(request, f"Failed to Delete Notice: {str(e)}")

    return HttpResponseRedirect(reverse("view_student_notices"))


def add_staff_notice(request):
    notices = StaffNotice.objects.all()
    return render(request, "hod_template/add_staff_notice.html",{"notices":notices})

def add_staff_notice_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")

        try:
            notice = StaffNotice(title=title, content=content)
            notice.save()
            messages.success(request, "Successfully Added Notice")
            return HttpResponseRedirect(reverse("add_staff_notice"))
        except:
            messages.error(request, "Failed to Add Notice")
            return HttpResponseRedirect(reverse("add_staff_notice"))

def view_staff_notices(request):
    notices = StaffNotice.objects.all().order_by('-created_at')
    return render(request, 'hod_template/view_staff_notices.html', {'notices': notices})


def edit_staff_notice(request, notice_id):
    try:
        notice = StaffNotice.objects.get(id=notice_id)
    except StaffNotice.DoesNotExist:
        messages.error(request, "Notice Not Found!")
        return HttpResponseRedirect(reverse("add_staff_notice"))

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        try:
            notice.title = title
            notice.content = content
            notice.save()
            messages.success(request, "Notice Updated Successfully!")
        except Exception as e:
            messages.error(request, f"Failed to Update Notice: {str(e)}")

        return HttpResponseRedirect(reverse("view_staff_notices"))

    return render(request, "hod_template/edit_staff_notice_template.html", {"notice": notice})


def delete_staff_notice(request, notice_id):
    try:
        notice = StaffNotice.objects.get(id=notice_id)
        notice.delete()
        messages.success(request, "Notice Deleted Successfully!")
    except StaffNotice.DoesNotExist:
        messages.error(request, "Notice Not Found!")
    except Exception as e:
        messages.error(request, f"Failed to Delete Notice: {str(e)}")

    return HttpResponseRedirect(reverse("view_staff_notices"))