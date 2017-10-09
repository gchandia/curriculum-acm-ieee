from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    women_qty = models.PositiveIntegerField(_("Cantidad de alumnas mujeres"))  # TODO revisar
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
    topics = models.ManyToManyField('KnowTopic', through='TeachingDetails')


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


# class Profile(models.Model):
#
#     # User model includes username, email ,first_name, last_name, password and other fields
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(_("Teléfono"), max_length=30)
#     #institutions = models.ManyToManyField(Institution, verbose_name=_("Instituciones"))
#     #programs = models.ManyToManyField(Program, verbose_name=_("Carreras"))
#
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()


class Poll(models.Model):
    # User contains email/username, first_name, last_name, password
    user = models.ForeignKey(User)
    institution = models.ForeignKey(Institution)
    program = models.ForeignKey(Program)
    subject = models.OneToOneField(Subject)
    city = models.CharField(_("Ciudad de Universidad"), max_length=100)
    accepted = models.BooleanField(_("Aceptada"))
    was_request = models.BooleanField(_("Es solicitud"))
    hash_id_program = models.CharField(_("Link a encuesta Datos Generales"), max_length=200)
    hash_id_subject = models.CharField(_("Link a encuesta Curso"), max_length=200)

class Request(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    institution = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class KnowArea(models.Model):
    name = models.CharField(max_length=100)


class KnowUnit(models.Model):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(KnowArea)


class KnowTopic(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    unit = models.ForeignKey(KnowUnit)


class TeachingDetails(models.Model):
    METHODOLOGIES = (
        ('P', _("Práctica")),
        ('T', _("Teórica")),
        ('TP', _("Teórico Práctica"))
    )

    topic = models.ForeignKey(KnowTopic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    hours = models.PositiveIntegerField(_("Horas dedicadas al tópico"))
    method = models.CharField(
        max_length=2,
        choices=METHODOLOGIES
    )
