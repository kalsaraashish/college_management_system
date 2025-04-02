import json
import os

from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt



def staff_home(request):
    from college_management_app.models import Subjects, Courses, Students, Attendance, Staffs, LeaveReportStaff, AttendanceReport,StaffNotice
    #For Fetch All Student Under Staff
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    course_id_list=[]
    for subject in subjects:
        course=Courses.objects.get(id=subject.course_id.id)
        course_id_list.append(course.id)

    final_course=[]
    #removing Duplicate Course ID
    for course_id in course_id_list:
        if course_id not in final_course:
            final_course.append(course_id)

    students_count=Students.objects.filter(course_id__in=final_course).count()

    #Fetch All Attendance Count
    attendance_count=Attendance.objects.filter(subject_id__in=subjects).count()

    #Fetch All Approve Leave
    staff=Staffs.objects.get(admin=request.user.id)
    profile_pic = staff.profile_pic.url if staff.profile_pic else None  # Get profile picture URL
    leave_count=LeaveReportStaff.objects.filter(staff_id=staff.id,leave_status=1).count()
    subject_count=subjects.count()

    #Fetch Attendance Data by Subject
    subject_list=[]
    attendance_list=[]
    for subject in subjects:
        attendance_count1=Attendance.objects.filter(subject_id=subject.id).count()
        subject_list.append(subject.subject_name)
        attendance_list.append(attendance_count1)

    students_attendance=Students.objects.filter(course_id__in=final_course)
    student_list=[]
    student_list_attendance_present=[]
    student_list_attendance_absent=[]
    for student in students_attendance:
        attendance_present_count=AttendanceReport.objects.filter(status=True,student_id=student.id).count()
        attendance_absent_count=AttendanceReport.objects.filter(status=False,student_id=student.id).count()
        student_list.append(student.admin.username)
        student_list_attendance_present.append(attendance_present_count)
        student_list_attendance_absent.append(attendance_absent_count)

    notices = StaffNotice.objects.all().order_by('-created_at')[:5]  # Fetch latest 5 notices


    return render(request,"staff_template/staff_home_template.html",{"students_count":students_count,"attendance_count":attendance_count,"leave_count":leave_count,"subject_count":subject_count,"subject_list":subject_list,"attendance_list":attendance_list,"student_list":student_list,"present_list":student_list_attendance_present,"absent_list":student_list_attendance_absent,"notices":notices,"profile_pic": profile_pic})


# ✅ Staff Take Attendance Page
def staff_take_attendance(request):
    from college_management_app.models import Subjects, SessionYearModel
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYearModel.object.all()
    return render(request, "staff_template/staff_take_attendance.html", {"subjects": subjects, "session_years": session_years})


# ✅ Get Students for Attendance
@csrf_exempt
def get_students(request):
    from college_management_app.models import Students, Subjects, SessionYearModel

    subject_id = request.POST.get("subject")
    session_year_id = request.POST.get("session_year")

    try:
        subject = Subjects.objects.get(id=subject_id)
        session_model = SessionYearModel.object.get(id=session_year_id)
        students = Students.objects.filter(course_id=subject.course_id, session_year_id=session_model)

        list_data = [{"id": student.admin.id, "name": f"{student.admin.first_name} {student.admin.last_name}"} for student in students]

        return JsonResponse(list_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ✅ Save Attendance Without Duplication
@csrf_exempt
def save_attendance_data(request):
    from college_management_app.models import Subjects, Attendance, AttendanceReport, SessionYearModel, Students

    student_ids = request.POST.get("student_ids")
    subject_id = request.POST.get("subject_id")
    attendance_date = request.POST.get("attendance_date")
    session_year_id = request.POST.get("session_year_id")

    try:
        if not (student_ids and subject_id and attendance_date and session_year_id):
            return HttpResponse("ERR: Missing required parameters")

        subject = Subjects.objects.get(id=subject_id)
        session = SessionYearModel.object.get(id=session_year_id)
        student_list = json.loads(student_ids)

        # ✅ Check if attendance already exists for the same date
        attendance, created = Attendance.objects.get_or_create(
            subject_id=subject,
            attendance_date=attendance_date,
            session_year_id=session
        )

        # ✅ Store attendance without duplicating
        for stud in student_list:
            student = Students.objects.get(admin=stud['id'])
            AttendanceReport.objects.update_or_create(
                student_id=student,
                attendance_id=attendance,
                defaults={"status": stud['status']}
            )

        print("Returning:", "OK" if created else "UPDATED")  # 🔍 Debugging
        return HttpResponse("OK" if created else "UPDATED")

    except Exception as e:
        print("Error in save_attendance_data:", str(e))  # 🔍 Debugging
        return HttpResponse(f"ERR: {str(e)}")


# ✅ Staff Update Attendance Page
def staff_update_attendance(request):
    from college_management_app.models import Subjects, SessionYearModel
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_year_id = SessionYearModel.object.all()
    print(session_year_id)
    return render(request, "staff_template/staff_update_attendance.html", {"subjects": subjects, "session_year_id": session_year_id})


# ✅ Get Unique Attendance Dates
@csrf_exempt
def get_attendance_dates(request):
    from college_management_app.models import Attendance, Subjects, SessionYearModel

    subject_id = request.POST.get("subject")
    session_year_id = request.POST.get("session_year_id")

    try:
        subject = Subjects.objects.get(id=subject_id)
        session_year = SessionYearModel.object.get(id=session_year_id)

        # ✅ Fetch DISTINCT attendance dates
        attendance_dates = Attendance.objects.filter(subject_id=subject, session_year_id=session_year) \
                                             .values("attendance_date").distinct()

        attendance_list = [{"id": str(date["attendance_date"]), "attendance_date": str(date["attendance_date"])} for date in attendance_dates]

        return JsonResponse(attendance_list, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ✅ Get Students for Attendance Update
@csrf_exempt
def get_attendance_student(request):
    from college_management_app.models import Attendance, AttendanceReport

    attendance_date = request.POST.get("attendance_date")

    try:
        # ✅ Get only ONE attendance record per date
        attendance_record = Attendance.objects.filter(attendance_date=attendance_date).first()

        if not attendance_record:
            return JsonResponse({"error": "No attendance found for this date"}, status=404)

        attendance_data = AttendanceReport.objects.filter(attendance_id=attendance_record)
        list_data = [
            {
                "id": student.student_id.admin.id,
                "name": f"{student.student_id.admin.first_name} {student.student_id.admin.last_name}",
                "status": student.status
            }
            for student in attendance_data
        ]

        return JsonResponse(list_data, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# ✅ Save Updated Attendance
@csrf_exempt
def save_updateattendance_data(request):
    from college_management_app.models import Attendance, AttendanceReport, Students

    student_ids = request.POST.get("student_ids")
    attendance_date = request.POST.get("attendance_date")

    try:
        attendance = Attendance.objects.filter(attendance_date=attendance_date).first()

        if not attendance:
            return HttpResponse("ERR: Attendance Record Not Found")

        student_list = json.loads(student_ids)

        for stud in student_list:
            student = Students.objects.get(admin=stud['id'])
            attendance_report, _ = AttendanceReport.objects.get_or_create(
                student_id=student,
                attendance_id=attendance,
                defaults={"status": stud['status']}
            )

            # ✅ Update status instead of re-creating record
            if not _:
                attendance_report.status = stud['status']
                attendance_report.save()

        return HttpResponse("OK")

    except Exception as e:
        return HttpResponse(f"ERR: {str(e)}")


def staff_apply_leave(request):
    from college_management_app.models import Staffs, LeaveReportStaff

    staff_obj = Staffs.objects.get(admin=request.user.id)
    leave_data=LeaveReportStaff.objects.filter(staff_id=staff_obj)
    return render(request,"staff_template/staff_apply_leave.html",{"leave_data":leave_data})

def staff_apply_leave_save(request):
    from college_management_app.models import Staffs, LeaveReportStaff

    if request.method!="POST":
        return HttpResponseRedirect(reverse("staff_apply_leave"))
    else:
        leave_date=request.POST.get("leave_date")
        leave_msg=request.POST.get("leave_msg")

        staff_obj=Staffs.objects.get(admin=request.user.id)
        try:
            leave_report=LeaveReportStaff(staff_id=staff_obj,leave_date=leave_date,leave_message=leave_msg,leave_status=0)
            leave_report.save()
            messages.success(request, "Successfully Applied for Leave")
            return HttpResponseRedirect(reverse("staff_apply_leave"))
        except:
            messages.error(request, "Failed To Apply for Leave")
            return HttpResponseRedirect(reverse("staff_apply_leave"))

def staff_feedback(request):
    from college_management_app.models import Staffs, FeedBackStaffs

    staff_id=Staffs.objects.get(admin=request.user.id)
    feedback_data=FeedBackStaffs.objects.filter(staff_id=staff_id)
    return render(request,"staff_template/staff_feedback.html",{"feedback_data":feedback_data})

def staff_feedback_save(request):
    from college_management_app.models import Staffs, FeedBackStaffs

    if request.method!="POST":
        return HttpResponseRedirect(reverse("staff_feedback_save"))
    else:
        feedback_msg=request.POST.get("feedback_msg")

        staff_obj=Staffs.objects.get(admin=request.user.id)
        try:
            feedback=FeedBackStaffs(staff_id=staff_obj,feedback=feedback_msg,feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully Sent Feedback")
            return HttpResponseRedirect(reverse("staff_feedback"))
        except:
            messages.error(request, "Failed To Send Feedback")
            return HttpResponseRedirect(reverse("staff_feedback"))


def staff_profile(request):
    from college_management_app.models import Staffs, CustomUser
    user=CustomUser.objects.get(id=request.user.id)
    staff=Staffs.objects.get(admin=user)
    return render(request,"staff_template/staff_profile.html",{"user":user,"staff":staff})

def staff_profile_save(request):
    from college_management_app.models import Staffs, CustomUser
    if request.method!="POST":
        return HttpResponseRedirect(reverse("staff_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        address=request.POST.get("address")
        password=request.POST.get("password")
        print("FILES RECEIVED:", request.FILES)
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!= None and password!="":
                customuser.set_password(password)
            customuser.save()

            staff=Staffs.objects.get(admin=customuser.id)
            staff.address=address
            if 'profile_pic' in request.FILES:
                profile_pic = request.FILES['profile_pic']
                print(profile_pic)

                # Store in 'media/staff_pics/' instead of default location
                fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'staff_pics'))

                # Remove old profile picture if it exists
                if staff.profile_pic:
                    old_pic_path = os.path.join(settings.MEDIA_ROOT, str(staff.profile_pic))
                    if os.path.exists(old_pic_path):
                        os.remove(old_pic_path)

                # Save the new file
                filename = fs.save(profile_pic.name, profile_pic)

                # Store relative path in the database (not a full URL)
                staff.profile_pic = f'staff_pics/{filename}'
            staff.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("staff_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("staff_profile"))


