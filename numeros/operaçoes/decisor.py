"""
Seleciona qual arit de sera realizada conforme o input do usario

"""
from operaçoes import arit  

def chama_calculadora(n1 , n2 , arit ):
    match arit :
        case "+ ":
            return arit.soma(n1, n2)
        case "-" :
            return arit.subtracao(n1, n2)
        case "*" :
            return arit.multiplicacao(n1, n2)
        case "/" : 
            return arit.divisao(n1, n2)
        case 
        case _:
            return "erro! operação invalida"
