from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=20)
    number_of_student = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.school_name} - {self.number_of_student}'

    class Meta:
        db_table = 'school'
        verbose_name_plural = 'School'
    
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, Student ID = {self.student_id}'

    class Meta:
        db_table = 'student'
        verbose_name_plural = 'Students'




