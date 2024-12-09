from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),


# student urls

    path("student/dashboard/", student_dashboard, name="student_dashboard"),
    
    path("student/profile/", profile, name="student-profile"),
    

    path("student/study_material/", study_material, name="study_material"),
    
    path("student/doubt_session/", doubt_session, name="doubt_session"),
    
    path("student/register_complaint/", register_complaint, name="register_complaint"),
    
    path("student/feedbacks/", feedbacks, name="feedbacks"),
    path("student/assesments/", assesments, name="assesments"),
    path("student/lectures/", lectures, name="lectures"),
    path("student/update_profile", update_profile, name="update_profile"),


# teacher urls
path("teacher/dashboard/", teacher_dashboard, name="teacher_dashboard"),


# admin urls
path("admin_u/dashboard/", admin_dashboard, name="admin_dashboard"),

path("admin_u/manage_user/", manage_user, name="manage_user"),
path("admin_u/edit_user/<int:id>/", edit_user, name="edit_user"),
path("admin_u/manage_student/", manage_student, name="manage_student"),
path("admin_u/manage_teacher/", manage_teacher, name="manage_teacher"),
path("admin_u/manage_admin/", manage_admin, name="manage_admin"),
path("admin_u/upload_studymaterial/",upload_studymaterial, name="upload_studymaterial"),
path("admin_u/upload_lectures/",upload_lectures, name="upload_lectures"),
path("admin_u/upload_assesments/",upload_assesments, name="upload_assesments"),
path("admin_u/view_feedback/",view_feedback, name="view_feedback"),
path("admin_u/view_complaint/",view_complaint, name="view_complaint"),
path("admin_u/view_enquries/",view_enquries, name="view_enquries"),
path("admin_u/view_feedback/",view_feedback, name="view_feedback"),
path("admin_u/add_notification/",add_notification, name="add_notification"),



]
    