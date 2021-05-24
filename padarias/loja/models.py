from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
	usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Produto(models.Model):
	nome = models.CharField(max_length=200)
	preco = models.FloatField()
	fresco = models.BooleanField(default=False,null=True, blank=True)

	def __str__(self):
		return self.name

class Pedido(models.Model):
	consumidor = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
	data_pedido = models.DateTimeField(auto_now_add=True)
	completado = models.BooleanField(default=False)
	transacao_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class ItemPedido(models.Model):
	produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
	pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
	quantidade = models.IntegerField(default=0, null=True, blank=True)
	data_adicionado = models.DateTimeField(auto_now_add=True)

class EnderecoEntrega(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
	endereco = models.CharField(max_length=200, null=False)
	cidade = models.CharField(max_length=200, null=False)
	estado = models.CharField(max_length=200, null=False)
	CEP = models.CharField(max_length=200, null=False)
	data_adicionado = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
