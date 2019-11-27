from django.db import models
from teachers.models import Teacher


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    head = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    establish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class AcademicSession(models.Model):
    year = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return '{} - {}'.format(self.year, self.year + 1)


class Semester(models.Model):
    number = models.PositiveIntegerField(unique=True)
    guide = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        if self.number == 1:
            return '1st'
        if self.number == 2:
            return '2nd'
        if self.number == 3:
            return '3rd'
        if 3 < self.number <= 12:
            return '%sth' % self.number


class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    roll = models.CharField(max_length=6, unique=True)
    registration_number = models.CharField(max_length=6, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default='1st')
    ac_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    guardian_mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    last_gpa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '{} ({}) semester {} dept.'.format(
            self.name, self.semester, self.department
        )


