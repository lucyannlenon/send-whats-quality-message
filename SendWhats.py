from urllib.parse import quote
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os 

class SendWhats:
    def send(self, number):
        mensagem = f'Olá somente um teste'
        try:
            link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={number}&text={quote(mensagem)}'
            webbrowser.open(link_mensagem_whatsapp) 

            sleep(20)
            seta = pyautogui.locateCenterOnScreen('seta.png')
            sleep(5)
            pyautogui.click(seta[0],seta[1])
            sleep(2)
            return True
        except:
            print(f'Não foi possível enviar mensagem para {number}')
            with open('erros.csv','a+',newline='',encoding='utf-8') as arquivo:
                arquivo.write(f'{number}{os.linesep}')
            return False
        finally:
            pyautogui.hotkey('ctrl','w')
            sleep(2)

