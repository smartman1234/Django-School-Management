from rolepermissions.roles import AbstractUserRole

class Subscriber(AbstractUserRole):
    available_permissions = {
        'visit_website': True,
    }

class Student(AbstractUserRole):
    available_permissions = {
        'visit_website': True,
        'update_profile': True,
        'view_result': True,
        'create_article': True,
        'add_testimonial': True,
    }


class Teacher(AbstractUserRole):
    available_permissions = {
        'visit_website': True,
        'update_profile': True,
        'view_result': True,
        'create_article': True,
        'add_testimonial': True,
        'add_result': True,
        'update_result': True,
        'add_testimonial': True,
    }


class Editor(AbstractUserRole):
    available_permissions = {
        'visit_website': True,
        'update_profile': True,
        'view_result': True,
        'create_article': True,
        'add_testimonial': True,
        'add_result': True,
        'update_result': True,
        'crud_teacher_application': True,
        'crud_student_application': True,
        'crud_subject': True,
        'crud_academic_session': True,
        'crud_designation': True,
        'crud_result': True,
    }


class AcademicOficer(AbstractUserRole):
    available_permissions = {
        'visit_website': True,
        'update_profile': True,
        'create_article': True,
        'add_testimonial': True,
        'crud_academic_session': True,
        'crud_counsel': True,
    }


class Admin(AbstractUserRole):
    available_permissions = {
        'create_article': True,
        'can_change_article': True,
        'can_delete_article': True,
        'can_view_article': True,
        'can_add_like': True,
        'can_view_like': True,
    }

