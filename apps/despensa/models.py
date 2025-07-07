from django.db import models

class Producto(models.Model):
  nombre = models.Charfield(max_length=100)
  descripcion = models.Charfield(Max_length=100)
  precio = models.float()
  stock = models.Integerfield()
  categoria = models.Charfield(max_length=100)
  def __str__(self):
    return f"{self.nombre}.{self.descripcion}"

#models producto


class Categoria(models.Model):
  nombre = models.Charfield(max_length=100)
  descripcion = models.Charfield(max_length=100)
  producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
  def __str__(self):
    return f"{self.nombre}.{self.descripcion}"

