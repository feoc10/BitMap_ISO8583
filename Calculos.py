from typing import Any

from PySimpleGUI import PySimpleGUI


class Calculos:
    def calcular(self, janela: PySimpleGUI, valores) -> Any:
        if janela.window['Bin'].get():
            self.binToHexa(janela, valores)
        elif janela.window['Hexa'].get():
            self.hexaToBin(janela, valores)

    def hexaToBin(self, janela: PySimpleGUI, valores) -> Any:
        """Transforma o Hexa do campo de input em binario e preenche os checkboxes da janela ativa"""
        ini_string = valores['BitMap']
        ini_string = ini_string.replace(" ", "")
        if len(ini_string) < 16:
            janela.window['BinBitMap'].update("Mapa de bits menor que o tamanho minímo")
            janela.window['BinBitMap'].update(text_color="red")
        else:
            # Converte hexa para binario
            result = "{0:064b}".format(int(ini_string, 16))
            janela.window['BinBitMap'].update(result)
            janela.window['BinBitMap'].update(text_color="yellow")

            i = 1
            for b in result:
                bit = f"Bit_{i}"
                if int(b) == 1:
                    janela.window[bit].update(value=True)

                else:
                    janela.window[bit].update(value=False)

                i += 1

    def binToHexa(self, janela: PySimpleGUI, valores):
        """Transforma os checkboxes preenchidos em hexa no campo de input"""
        janela.window['BinBitMap'].update("Bin To Hexa")
        janela.window['BinBitMap'].update(text_color="red")
        checkboxesList = []
        aux_bin = ""
        for check in range(1, 65):
            checkbox = f"Bit_{check}"
            if janela.window[checkbox].get():
                aux_bin += '1'
            else:
                aux_bin += '0'

        aux_hex = hex(int(aux_bin, 2))
        aux_hex = aux_hex[2:].upper()
        janela.window['BitMap'].update(aux_hex)
