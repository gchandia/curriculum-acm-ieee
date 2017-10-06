from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class Institution(models.Model):
    name = models.CharField(_("Nombre de la institución"), max_length=100)


class Campus(models.Model):
    name = models.CharField(_("Nombre del Campus"), max_length=100)
    institution = models.ForeignKey(Institution)


class Subject(models.Model):
    name = models.CharField(_("Nombre del curso"), max_length=100)
    yearly = models.BooleanField(_("Curso anual"))
    semester = models.PositiveIntegerField(_("Semestre al que corresponde"))
    fulltime_teacher = models.BooleanField(_("Profesor de jornada completa"))
    # Time distribution
    weekly_personal_hours = models.DurationField(_("Horas semanales de trabajo personal"))
    weekly_class_hours = models.DurationField(_("Horas semanales de clases"))
    weekly_lab_hours = models.DurationField(_("Horas semanales de laboratorios"))
    # Gender distribution
    men_qty = models.PositiveIntegerField(_("Cantidad de alumnos hombres"))
    women_qty = models.PositiveIntegerField(_("Cantidad de alumnas mujeres")) # TODO revisar
    # Evaluation distribution
    homework_percent = models.FloatField(_("Porcentaje de tareas personales"))
    test_percent = models.FloatField(_("Porcentaje de pruebas"))
    lab_percent = models.FloatField(_("Porcentaje de laboratorios"))
    #Evaluation Quantity
    homework_amount = models.PositiveIntegerField(_("Número de tareas personales"))
    test_amount = models.PositiveIntegerField(_("Número de pruebas"))
    lab_amount = models.PositiveIntegerField(_("Número de laboratorios"))
    # Teacher body distribution
    aux_amount = models.PositiveIntegerField(_("Número de auxiliares"))
    ayu_amount = models.PositiveIntegerField(_("Número de ayudantes"))
    tut_amount = models.PositiveIntegerField(_("Número de tutores"))


class Program(models.Model):
    name = models.CharField(_("Nombre de la Carrera"), max_length=100)
    campus = models.ForeignKey(Campus)
    subjects = models.ManyToManyField(Subject,
                                      verbose_name=_("Cursos obligatorios"),
                                      related_name="programs")
    electives = models.ManyToManyField(Subject,
                                       verbose_name=_("Cursos electivos"),
                                       related_name="elective_programs")
    core_curriculum = models.BooleanField(verbose_name=_("Plan común"))
    graduation_time = models.PositiveIntegerField(_("Tiempo estimado de graduación"))
    # Alumni quantity stats
    currentyear_alumni_qty = models.PositiveIntegerField(_("Cantidad de alumnos año actual"))
    lastyear_alumni_qty = models.PositiveIntegerField(_("Cantidad de alumnos año pasado"))
    b4lastyear_alumni_qty = models.PositiveIntegerField(_("Cantidad de alumnos año antepasado"))
    # Application stats
    currentyear_psu_max = models.PositiveIntegerField(_("Máximo puntaje PSU año actual"))
    currentyear_psu_min = models.PositiveIntegerField(_("Mínimo puntaje PSU año actual"))
    lastyear_psu_max = models.PositiveIntegerField(_("Máximo puntaje PSU año pasado"))
    lastyear_psu_min = models.PositiveIntegerField(_("Mínimo puntaje PSU año pasado"))
    b4lastyear_psu_max = models.PositiveIntegerField(_("Máximo puntaje PSU año antepasado"))
    b4lastyear_psu_min = models.PositiveIntegerField(_("Mínimo puntaje PSU año antepasado"))


class Teacher(models.Model):
    # User model includes username, email, first_name, last_name, password and other fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField(_("Email"))
    # fullname = models.CharField(_("Nombre completo"), max_length=100)
    phone = models.CharField(_("Teléfono"), max_length=100)
    institutions = models.ManyToManyField(Institution, verbose_name=_("Instituciones"))
    programs = models.ManyToManyField(Program, verbose_name=_("Carreras"))
