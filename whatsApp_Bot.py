# Author: Ivanoel Rodrigo
# WhatsApp Robô
# 08/06/2020

from selenium import webdriver
import time

class WhatsappRobo:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Olá, tudo bem? Responderei assim que possível."

        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Grupo da família"]

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            # Abra whats Web no navegador e aperte f12 para vê qual é elemento que egloba o texto
            # da mensagem toda e só cópia.
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappRobo()
bot.EnviarMensagens()
