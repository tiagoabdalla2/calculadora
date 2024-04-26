def exebir_mesagem():
    print("""bem vindo á calculadora insira um numero e pressione ENTER  , em seguida digite uma operaçao (+,-,*,/) e pressione ENTER
  por fim , insira ooutro numero e pressione ENTER mais uma vez . o resultado sera exbido em seguida .""")

def inciar():
    exebir_mesagem()
    n1 = float(input())
    operaçao = input()
    n2 = float(input())
    print(n1 , operaçao , n2 )

    
inciar()