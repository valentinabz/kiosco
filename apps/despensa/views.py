from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto
from .models import Categoria

class CursoListView(ListView):
 model = Producto
template_name = 'Prducto/list.html'
context_object_name = 'Producto' 

class CursoCreateView(CreateView):
 model = Producto
fields = '__all__'
template_name = 'Producto/create.html'
success_url = reverse_lazy('Producto:producto_list')

class CursoUpdateView(UpdateView):
 model = Producto
fields = '__all__'
template_name = 'Producto/update.html'
success_url = reverse_lazy('Producto:Producto_list')
class CursoDeleteView(DeleteView):
 model = Producto
template_name = 'Producto/delete.html'
success_url = reverse_lazy('Prpducto:Producto_list')

class CursoListView(ListView):
 model = Categoria
template_name = 'Categoria/list.html'
context_object_name = 'Categoria' 

class CursoCreateView(CreateView):
 model = Categoria
fields = '__all__'
template_name = 'Categoria/create.html'
success_url = reverse_lazy('Categoria:Categoria_list')



class CursoUpdateView(UpdateView):
 model = Categoria
fields = '__all__'
template_name = 'Categoria/update.html'
success_url = reverse_lazy('Categoria:Categoria_list')
class CursoDeleteView(DeleteView):
 model = Producto
template_name = 'Categoria/delete.html'
success_url = reverse_lazy('Categoria:Categoria_list')

