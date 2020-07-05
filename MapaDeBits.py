from Tela import Tela
from Calculos import Calculos

tela = Tela()
calc = Calculos()
while True:
    # Extrai os dados da janela
    events, values = tela.window.Read()
    if events is None or events == 'Exit':
        break
    if events == 'Calcular':
        calc.calcular(tela, values)
