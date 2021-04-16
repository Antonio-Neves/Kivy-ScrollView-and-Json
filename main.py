# ----- Importações iniciais ----- #
#import kivy
#kivy.require('1.11.1')

import os
from kivy import Config

import platform

# ----- Soluciona problemas de OpenGL e placas graficas antigas em windows -- #
if platform.system() == 'Windows':

	os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
	Config.set('graphics', 'multisamples', '0')

# ----- Necessário para Video e Audio no Linux----- #
if platform.system() == 'Linux':

	os.environ['KIVY_VIDEO'] = 'ffpyplayer'

# ----- Configuração da janela ----- #
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'exit_on_escape', '0')
Config.set('graphics', 'width', 700)
Config.set('graphics', 'height', 500)

# ----- Importações ----- #
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
import json

# ----- Lista para guardar os dados do Json ----- #
lista_dados = []

# --- Lê arquivo Json e adiciona os dados na lista_dados --- #
with open('arquivojs.json', 'r') as data:
	lista_dados = json.load(data)


class Principal(BoxLayout):
	def __init__(self):
		super().__init__()

		self.modelo_resultados = ModeloResultados()  # instancia Wid de resultados

		self.io_resultado = 0  # controla se widget ModeloResultado já existe


	# ----- Adiciona um botão por cada dado no json ----- #
	def adiciona_botao(self):

		for item in lista_dados:
			self.ids.box_dados.add_widget(ModeloBotao(item[0]))


	# ----- Adiciona Widget do resultado ----- #
	def resultado(self, texto_botao):

		resultado = ''

		if self.io_resultado == 1:  # Se widget resultado já existe, apaga widget

			self.ids.box_resultados.clear_widgets()
			self.io_resultado = 0

		if self.io_resultado == 0:  # # Se widget resultado não existe, coloca widget

			self.ids.box_resultados.add_widget(self.modelo_resultados)

			for item in lista_dados:
				if item[0] == texto_botao:
					resultado = item[1]

			self.modelo_resultados.texto_resultado(resultado)
			self.io_resultado = 1


	# ----- Limpa os botoes do Scrolview ----- #
	def limpa_scrolview(self):

		self.ids.box_dados.clear_widgets()


	# ----- Limpa o Widget do resultado ----- #
	def limpa_box_resultados(self):

		self.ids.box_resultados.clear_widgets()


class ModeloBotao(Button):
	def __init__(self, texto):
		super().__init__()

		# --- texto do botão --- #
		self.text = texto


class ModeloResultados(FloatLayout):
	def __init__(self):
		super().__init__()

	def texto_resultado(self, texto_botao):

		self.ids.resultado.text = texto_botao


class Main(App):
	def build(self):
		return Principal()


if __name__ == '__main__':
	Main().run()
