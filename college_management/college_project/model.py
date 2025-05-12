from django.db import models

# =============================
# Admin-Managed Models
# =============================

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    organized_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class PlacementCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    package = models.DecimalField(max_digits=10, decimal_places=2)
    drive_date = models.DateField()
    eligibility_criteria = models.TextField()

    def __str__(self):
        return self.name

# =============================
# Faculty-Managed Models
# =============================

class Marks(models.Model):
    mark_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks_obtained = models.IntegerField()
    max_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=30,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
            ('Conducting Event', 'Conducting Event'),
            ('Organising Seminar/Workshop', 'Organising Seminar/Workshop')
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"


class FacultyProfessionalDetail(models.Model):
    faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE)
    experience_years = models.IntegerField()
    specialization = models.CharField(max_length=100)
    publications = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.faculty.name} - {self.specialization}"


class StudentInternship(models.Model):
    internship_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.student.name} - {self.company_name}"


class PlacementManagement(models.Model):
    placement_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(PlacementCompany, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30,
        choices=[
            ('Applied', 'Applied'),
            ('Interviewed', 'Interviewed'),
            ('Selected', 'Selected'),
            ('Rejected', 'Rejected')
        ]
    )
    applied_on = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.company.name} - {self.status}"

