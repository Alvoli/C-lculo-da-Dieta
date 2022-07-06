import time
PROT = 0.15
CARB = 0.55
FAT = 0.3
A = int(input("Insira sua altura em centímetros:"))
I = int(input("Insira sua idade:"))
P = float(input("Insira o seu peso:"))
TMB=()
Gen =""
def DefineGenero():
    global Gen
    global TMB
    Gen =input("Insira seu gênero biológico(Homem ou Mulher):")
    if Gen == 'H' or Gen =='h' or Gen == "Homem" or Gen == "homem":
        TMB= (66+(13.7*P)+(5*A)-(6.8*I))
    elif Gen =='M' or Gen == 'm' or Gen == "Mulher" or Gen == "mulher":
        TMB=(655+(9.6*P)+(1.8*A)-(4.7*I))
    else:
        print("Insira uma resposta válida.")
        DefineGenero()
DefineGenero()
GCD= int(input("Insira seus gastos calóricos diários(Dentre cardio, musculação e jornada de trabalho):"))
GCD_F= GCD + TMB
Calc_Carb= GCD_F*CARB/4
Calc_Prot= GCD_F*PROT/4
Calc_Fat= GCD_F*FAT/9
Calc_Carb_Baixo= ((TMB-(TMB*0.2)+GCD)*0.55)/4
Calc_Carb_Alto= ((TMB+(TMB*0.2)+GCD)*0.55)/4
print(f"Seu Carboidrato diário base é de: {Calc_Carb:.2f} gramas.")
print(f"Sua Proteína diária é de: {Calc_Prot:.2f} gramas.")
print(f"Sua Gordura diária é de: {Calc_Fat:.2f} gramas.")
print(f"Seu Carboidrato diário alto é de: {Calc_Carb_Alto:.2f} gramas.")
print(f"Seu Carboidrato diário baixo é de: {Calc_Carb_Baixo:.2f} gramas.")
input()


'''
A cada 100g de arroz existem 28g de carbo
Para consumir 322g de carbo seria necessário...

28/100=322/x
      =
28x=32200
x=1150g
    ou
    1.15kg
xd
'''