import re


class PnoneNumberBr:
    def __init__(self, phoneNumber):
        if self.isValid(phoneNumber):
            self.number = phoneNumber
        else:
            raise ValueError(f"Invalid Number {self.number}")

    def __str__(self):
        return self.numFormat()

    def getNumber(self):
        number = re.sub(r'\D','',self.number)
        lenNumero = len(number);
        brCode="55" 
        if(lenNumero==10 and number.startswith(brCode)):
            raise ValueError(f"Invalid Number {self.number}")
        if(lenNumero==10):
            if(int(number[2])<=5):
                return f'{brCode}{number}'
            else:
                return f'{brCode}{number[:2]}9{number[2:]}'
        if(lenNumero==11):
            return f'{brCode}{number}'
        if(lenNumero==12 and number.startswith(brCode)):
            if(int(number[4])<=5):
                return number ; 
            else:
                return f'{number[:4]}9{number[4:]}'
        return number

    def isValid(self, telefone):
        lenNumero = len(re.sub(r'\D','',telefone));
    
        return lenNumero>=10 and lenNumero <=13            

    def numFormat(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"  # "?" indica que aquele grupo não é obrigatorio
        resposta = re.search(padrao, self.number)
        numero_formatado = "+{}({}){}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
        return numero_formatado