import PySimpleGUI as sg


class Tela:
    def __init__(self):
        sg.theme('DarkAmber')
        # Layout
        layout = [
            [sg.Text("Insira o mapa de bits:"), sg.InputText(key="BitMap")],
            [sg.Radio('Hexa -> Bin', "conversor", default=True, key='Hexa'),
             sg.Radio('Bin -> Hexa', "conversor", key='Bin')],
            [sg.Text("", size=(64, 1), key='BinBitMap', justification='center')],
            [sg.Checkbox('Bit 1', key='Bit_1', ), sg.Checkbox('Bit 9', key='Bit_9'),
             sg.Checkbox('Bit 17', key='Bit_17'),
             sg.Checkbox('Bit 25', key='Bit_25'), sg.Checkbox('Bit 33', key='Bit_33'),
             sg.Checkbox('Bit 41', key='Bit_41'), sg.Checkbox('Bit 49', key='Bit_49'),
             sg.Checkbox('Bit 57', key='Bit_57')],
            [sg.Checkbox('Bit 2', key='Bit_2'), sg.Checkbox('Bit 10', key='Bit_10'),
             sg.Checkbox('Bit 18', key='Bit_18'), sg.Checkbox('Bit 26', key='Bit_26'),
             sg.Checkbox('Bit 34', key='Bit_34'), sg.Checkbox('Bit 42', key='Bit_42'),
             sg.Checkbox('Bit 50', key='Bit_50'), sg.Checkbox('Bit 58', key='Bit_58')],
            [sg.Checkbox('Bit 3', key='Bit_3'), sg.Checkbox('Bit 11', key='Bit_11'),
             sg.Checkbox('Bit 19', key='Bit_19'), sg.Checkbox('Bit 27', key='Bit_27'),
             sg.Checkbox('Bit 35', key='Bit_35'), sg.Checkbox('Bit 43', key='Bit_43'),
             sg.Checkbox('Bit 51', key='Bit_51'), sg.Checkbox('Bit 59', key='Bit_59')],
            [sg.Checkbox('Bit 4', key='Bit_4'), sg.Checkbox('Bit 12', key='Bit_12'),
             sg.Checkbox('Bit 20', key='Bit_20'), sg.Checkbox('Bit 28', key='Bit_28'),
             sg.Checkbox('Bit 36', key='Bit_36'), sg.Checkbox('Bit 44', key='Bit_44'),
             sg.Checkbox('Bit 52', key='Bit_52'), sg.Checkbox('Bit 60', key='Bit_60')],
            [sg.Checkbox('Bit 5', key='Bit_5'), sg.Checkbox('Bit 13', key='Bit_13'),
             sg.Checkbox('Bit 21', key='Bit_21'), sg.Checkbox('Bit 29', key='Bit_29'),
             sg.Checkbox('Bit 37', key='Bit_37'), sg.Checkbox('Bit 45', key='Bit_45'),
             sg.Checkbox('Bit 53', key='Bit_53'), sg.Checkbox('Bit 61', key='Bit_61')],
            [sg.Checkbox('Bit 6', key='Bit_6'), sg.Checkbox('Bit 14', key='Bit_14'),
             sg.Checkbox('Bit 22', key='Bit_22'), sg.Checkbox('Bit 30', key='Bit_30'),
             sg.Checkbox('Bit 38', key='Bit_38'), sg.Checkbox('Bit 46', key='Bit_46'),
             sg.Checkbox('Bit 54', key='Bit_54'), sg.Checkbox('Bit 62', key='Bit_62')],
            [sg.Checkbox('Bit 7', key='Bit_7'), sg.Checkbox('Bit 15', key='Bit_15'),
             sg.Checkbox('Bit 23', key='Bit_23'), sg.Checkbox('Bit 31', key='Bit_31'),
             sg.Checkbox('Bit 39', key='Bit_39'), sg.Checkbox('Bit 47', key='Bit_47'),
             sg.Checkbox('Bit 55', key='Bit_55'), sg.Checkbox('Bit 63', key='Bit_63')],
            [sg.Checkbox('Bit 8', key='Bit_8'), sg.Checkbox('Bit 16', key='Bit_16'),
             sg.Checkbox('Bit 24', key='Bit_24'), sg.Checkbox('Bit 32', key='Bit_32'),
             sg.Checkbox('Bit 40', key='Bit_40'), sg.Checkbox('Bit 48', key='Bit_48'),
             sg.Checkbox('Bit 56', key='Bit_56'), sg.Checkbox('Bit 64', key='Bit_64')],
            [sg.Text("")], #Somente para pular uma linha
            [sg.Button("Calcular", key='Calcular')]
        ]
        # Janela
        self.window = sg.Window("Mapa de Bits em Python", layout, element_justification='c')
