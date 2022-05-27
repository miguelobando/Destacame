from enum import unique
from pyexpat import model
from django.db import models
from django.core.validators import EmailValidator, RegexValidator, MaxValueValidator, MinValueValidator


validadorNombre = RegexValidator(r'^[a-zA-Z ]+$', 'Solo letras y espacios permitidos')
validadorEmail = EmailValidator()
validadorPlaca = RegexValidator(r'^[A-Za-z0-9]+$', 'Solo letras y numeros')

class Usuario(models.Model):
    # id = models.AutoField(primary_key= True)
    email = models.CharField( primary_key=True ,validators=[validadorEmail],max_length=200)
    nombre = models.CharField(max_length=200, validators=[validadorNombre])
    apellido = models.CharField(max_length=200, validators=[validadorNombre])
    esChofer = models.BooleanField(default=False)
    # class Meta:
    #     unique_together = ['id', 'email']

class Bus(models.Model):
    placa = models.CharField(primary_key=True, validators=[validadorPlaca], max_length=200)
    chofer = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True, related_name="chofer")

class Asiento(models.Model):
    id = models.AutoField(primary_key= True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=False, related_name="bus")
    numeroAsiento = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    terminal = models.CharField(max_length=200, validators=[validadorNombre])
    ciudad = models.CharField(max_length=200, validators=[validadorNombre])

    class Meta:
        unique_together = ['terminal', 'ciudad']

class Trayecto(models.Model):
    id = models.AutoField(primary_key = True)
    inicio = models.ForeignKey(Ruta,on_delete=models.CASCADE,null=False, related_name="rutaDeInicio")
    fin = models.ForeignKey(Ruta,on_delete=models.CASCADE,null=False, related_name="rutaDeFin")
    class Meta:
        unique_together = ['inicio','fin']

class HorarioXTrayecto(models.Model):
    id = models.AutoField(primary_key=True)
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE, null=False, related_name="trayecto") 
    horario = models.DateTimeField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=False, default=1 ,related_name='busAsignado')
    class Meta:
        unique_together = ['trayecto','horario','bus']

class Boleto(models.Model):
    id = models.AutoField(primary_key= True)
    asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE, null=False, related_name="asientoAsignado")
    pasajero = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False,related_name="pasajeroAsignado")
    trayecto = models.ForeignKey(Trayecto,on_delete=models.CASCADE, null=False, related_name="trayectoAsignado")
    horario = models.ForeignKey(HorarioXTrayecto,on_delete=models.CASCADE, related_name="horarioAsignado")




