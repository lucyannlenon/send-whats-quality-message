from PnoneNumberBr import PnoneNumberBr
from PositionFile import PositionFile
from googleData import getGoogleData
from googleData import writeGoogleSheets
from SendWhats import SendWhats
import os 


def main():
    
    file = PositionFile()
    read = file.load() 
    send = SendWhats()
    okInfo = ["OK"]
    while True:

        items = getGoogleData(f'D{read}:G{read}') ; 

        if(items is None):
            print(f'Não encontrei nada in line D{read}:G{read}')
            break


        for item in items:
            for number in item:
                try:    
                    phone = PnoneNumberBr(number)
                    if(send.send(phone.getNumber())):
                        writeGoogleSheets(f'H{read}',okInfo)
                        break ; 
                except ValueError as err:
                    with open('erros.csv','a+',newline='',encoding='utf-8') as arquivo:
                        arquivo.write(f'{number}  -> {err}{os.linesep}')
        #increment        
        read=read +1 
    #wirte current position in fil 
    file.write(str(read))


    # telefone_objeto = PnoneNumberBr(telefone)
    # print(telefone_objeto.getNumber())

main()