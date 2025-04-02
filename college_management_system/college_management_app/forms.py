from django import forms
from django.forms import TextInput

from college_management_app.models import Courses, Subjects, Staffs

from college_management_app.models import SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control","placeholder": "Enter Email"}))
    password = forms.CharField(label="Password", max_length=50,widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Enter Passowrd"}))
    first_name = forms.CharField(label="First Name", max_length=50,widget=TextInput(attrs={"class": "form-control","placeholder": "Enter First Name"}))
    last_name = forms.CharField(label="Last Name", max_length=50,widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Last name"}))
    username = forms.CharField(label="Username", max_length=50,widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Username"}))
    address = forms.CharField(label="Address", max_length=50,widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter Address"}))
    mobile_number = forms.CharField(
        label="Mobile Number",
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Mobile Number"})
    )
    course_list = []
    courses = Courses.objects.all()
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    session_list = []
    try:
        session = SessionYearModel.object.all()
        for ses in session:
            small_ses = (ses.id, str(ses.session_start_year) + " TO " + str(ses.session_end_year))
            session_list.append(small_ses)
    except:
        session_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    course = forms.ChoiceField(label="Course", choices=course_list,widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=gender_choice,widget=forms.Select(attrs={"class": "form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", widget=forms.Select(attrs={"class": "form-control"}),choices=session_list)
    profile_pic = forms.FileField(label="Profile Pic", max_length=50,widget=forms.FileInput(attrs={"class": "form-control"}))



class EditStudentForm(forms.Form):
        email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
        first_name = forms.CharField(label="First Name", max_length=50,widget=TextInput(attrs={"class": "form-control"}))
        last_name = forms.CharField(label="Last Name", max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
        username = forms.CharField(label="Username", max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
        address = forms.CharField(label="Address", max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
        mobile_number = forms.CharField(
            label="Mobile Number",
            max_length=15,
            required=False,
            widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Mobile Number"})
        )
        courses_list = []
        try:
            courses = Courses.objects.all()
            for course in courses:
                small_course = (course.id, course.course_name)
                courses_list.append(small_course)
        except:
            courses_list=[]

        session_list = []
        # try:
        session = SessionYearModel.object.all()

        for ses in session:
                small_ses = (ses.id, str(ses.session_start_year) + "  TO  " +str(ses.session_end_year))
                session_list.append(small_ses)
        # except:
        #     session_list = []

        gender_choice = (
            ("Male", "Male"),
            ("Female", "Female")
        )

        course = forms.ChoiceField(label="Course", choices=courses_list,widget=forms.Select(attrs={"class": "form-control"}))
        sex = forms.ChoiceField(label="Sex", choices=gender_choice,widget=forms.Select(attrs={"class": "form-control"}))
        session_year_id = forms.ChoiceField(label="Session Year", widget=forms.Select(attrs={"class": "form-control"}),choices=session_list)
        profile_pic = forms.FileField(label="Profile Pic", max_length=50,widget=forms.FileInput(attrs={"class": "form-control"}),required=False)


