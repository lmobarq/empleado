from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    
)

# from empleado.applications.departamento.models import Departamento
# models
from .models import Empleado
#forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """vista que carga la pagina de inicio"""
    template_name = 'inicio.html'


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class  ListByAreaEmpleado(ListView):
    """lista de empleados de un area"""
    template_name = 'persona/list_by_area.html'
    # queryset = Empleado.objects.filter(
    #     departamento__shor_name = 'Administración'
    # )
    context_object_name = 'empleados'

    def get_queryset(self):
        #el codigo que yo quiero#  
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    
class ListEmpleadosByKword(ListView):
    """Lista de empleados por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('********************')
        palabra_clave = self.request.GET.get("kword",'')
        # print('=======',palabra_clave)
        # return []

        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        # print('lista_resultado:',lista)
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()
        # print(empleado.habilidades.all())
        # return []


class ListEmpleadosByTrabajo(ListView):
    template_name = 'persona/list_by_trabajo.html'

    def get_queryset(self):
        #el codigo que yo quiero#  
        lmtrabajo = self.kwargs['lmjob']
        lista = Empleado.objects.filter(
        job = lmtrabajo
        )
        return lista    



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #todo un proceso    
        context['titulo'] = 'Empleado del mes'
        return context
    



class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    # fields = ('__all__')

    # fields = [
    #     'first_name',
    #     'last_name',
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'avatar',
    # ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        #logica del proceso
        # print(empleado) #esto deberai estar despues de empleado = form.save() en 1ra version
        # empleado = form.save()
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form) 

        

class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('***************METODO POST***********************')
        print('============================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

        

    def form_valid(self, form):
        #logica del proceso
        return super(EmpleadoUpdateView, self).form_valid(form) 



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')



    # success_url = '/success'
    # success_url = '.'



    # fields = ['first_name', 'last_name', 'job']





# class  ListByAreaEmpleado(ListView):
#     """lista de empleados de un area"""
#     template_name = 'persona/list_by_area.html'
#     # queryset = Empleado.objects.filter(
#     #     departamento__shor_name = 'Administración'
#     # )

#     def get_queryset(self):
#         #el codigo que yo quiero#  
#         area = self.kwargs['shorname']
#         lista = Empleado.objects.filter(
#         departamento__shor_name = area
#         )
#         return lista




#lista-empleado-trabajo
















# listar todos los empleados de la empresa
# listar todos los empleados que pertenecen a un area de la empresa

# listar los empleados por palabra clave
# listar habilidades de un empleado
# listar empleados por trabajo

