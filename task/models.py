from django.db import models
from django.contrib.auth import get_user_model

'''
class Employee(models.Model): #Lista de Funcionários

    emp_name = models.CharField(max_length=255, verbose_name='NOME DO COLABORADOR')
    emp_office = models.CharField(max_length=255, verbose_name='FUNÇÃO')
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True, verbose_name='FOTO')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='USUÁRIO')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name


class ProjControl(models.Model): #Tabela = Lista de Documentos LD
    
    proj_name = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='PROJETO')
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='DISCIPLINA')
    doc_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='NOME DO DOCUMENTO')
    doc_number = models.ForeignKey(DocType, on_delete=models.CASCADE, verbose_name='NÚMERO DO DOCUMENTO')
    responsible = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='resp', verbose_name='RESPONSÁVEL')
    elab = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='elab', verbose_name='ELABORADOR')
    verif = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='verif', verbose_name='VERIFICADOR')
    aprov = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='aprov', verbose_name='APROVADOR')
    emiss = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, related_name='emiss', verbose_name='EMISSOR')
    status = models.ForeignKey(StatusDoc, on_delete=models.CASCADE, blank=True, null=True, verbose_name='STATUS')
    action = models.ForeignKey(Action, on_delete=models.CASCADE, blank=True, null=True, verbose_name='AÇÃO')
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    comments = models.TextField()
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.proj_name)

        
class Upload(models.Model): #Upload de arquivos
    arq = models.FileField(upload_to='uploads/', help_text='localizar Arquivo')
    update_arq = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.arq)
'''