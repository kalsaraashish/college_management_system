from django.conf import settings

from college_management_app.models import Students, Staffs

def profile_pic_context(request):
    profile_pic = None
    if request.user.is_authenticated:
        try:
            # Check if user is a student
            if hasattr(request.user, 'students'):
                student_obj = Students.objects.get(admin=request.user)
                if student_obj.profile_pic:
                    profile_pic = f"{settings.MEDIA_URL}{student_obj.profile_pic}"
            # Check if user is a staff
            elif hasattr(request.user, 'staffs'):
                staff_obj = Staffs.objects.get(admin=request.user)
                if staff_obj.profile_pic:
                    profile_pic = f"{settings.MEDIA_URL}{staff_obj.profile_pic}"
        except (Students.DoesNotExist, Staffs.DoesNotExist):
            pass  # If no profile found, profile_pic remains None

    return {"profile_pic": profile_pic}
