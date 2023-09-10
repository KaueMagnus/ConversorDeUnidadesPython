'''Calculadora de conversão de unidades'''

import os               
def limpar_tela():      #definindo a instrução que irá limpar a tela em cada iteração.
    sistema = os.name
    if sistema == "posix":  # Linux ou macOS
        os.system("clear")
    elif sistema == "nt":  # Windows
        os.system("cls")
        
from tabulate import tabulate      #Importando biblioteca tabulate que nos fornece uma possibilidade de saída de tabelas.

reset = int(1)  # Variavel para guardar meu reset inicial do programa

while reset == 1:  # Enquanto reset é igual a 1 ele irá executar as intruções de conversão.
    
    limpar_tela()
    
    print("=========TABELA DE MEDIDAS=========")

    print("Selecione o tipo de medida:")
    print("1 - Temperatura (Celsius, Fahr, Kelvin).")
    print("2 - Comprimento (Metros, Kilometros, Pés, Jardas).")
    print("3 - Peso (KG, Libras, Gramas, Miligramas).")
    print("4 - Sair.")
    print("===================================")
    # Usuario digita o numero correspondente da medida.
    operacao = int(input("Digite o numero da opção: "))

    match operacao:
        case 1:  # Executado se o usuário escolher a opção 1.
            limpar_tela()
            print("=========TEMPERATURA=========")
            valor = float(input("Insira o valor da medida: "))
            celsiusFahr = float((valor * 9/5) + 32)
            celsiusK = float(valor + 273.15)
            fahrC = float((valor - 32) / 1.8000)
            fahrK = float((valor + 459.67) * 5/9)
            kelvinC = float(valor - 273.15)
            kelvinFahr = float((valor * 9/5) - 459.67)

            temperatura = [  # Estrutura da tabela para exibir os resultados de temperatura.
                ["De", "Para", "Resultado"],
                ["Celsius", "Fahrnheit", f"{valor} °C = {celsiusFahr:.1f} °F"],
                ["Celsius", "Kelvin", f"{valor} °C = {celsiusK:.1f} °K"],
                ["Fahrnheit", "Celsius", f"{valor} °F = {fahrC:.1f} °C"],
                ["Fahrnheit", "Kelvin", f"{valor} °F = {fahrK:.1f} °K"],
                ["Kelvin", "Celsius", f"{valor} °K = {kelvinC:.1f} °C"],
                ["Kelvin", "Fahrnheit", f"{valor} °K = {kelvinFahr:.1f} °F"]
            ]
            # Instrução para exibir a tabela estruturada.
            print(tabulate(temperatura, headers="firstrow", tablefmt="heavy_grid"))

        case 2:  # Executado se o usuário escolher a opção 2.
            limpar_tela()
            print("=========COMPRIMENTO=========")
            valor = float(input("Insira o valor da medida: "))
            metroKm = float(valor / 1000)
            metroPes = float(valor * 3.281)
            metroJardas = float(valor * 1.094)
            kmMetro = float(valor * 1000)
            kmPes = float(valor * 3281)
            kmJarda = float(valor * 1094)
            pesMetro = float(valor / 3.281)
            pesKm = float(valor / 3281)
            pesJarda = float(valor / 3)
            jardaMetro = float(valor / 1.094)
            jardaKm = float(valor / 1094)
            jardaPes = float(valor * 3)

            comprimento = [  # Estrutura da tabela para exibir os resultados de comprimento.
                ["De", "Para", "Resultado"],
                ["Metros", "Kilometros", f"{valor} m = {metroKm:.2f} km"],
                ["Metros", "Pés", f"{valor} m = {metroPes:.2f} pés"],
                ["Metros", "Jardas", f"{valor} m = {metroJardas:.2f} jardas"],
                ["Kilometros", "Metros", f"{valor} km = {kmMetro:.2f} metros"],
                ["Kilometros", "Pés", f"{valor} km = {kmPes:.2f} pés"],
                ["Kilometros", "Jardas", f"{valor} km = {kmJarda:.2f} jardas"],
                ["Pés", "Metros", f"{valor} pés = {pesMetro:.2f} metros"],
                ["Pés", "Kilometros", f"{valor} pés = {pesKm:.2f} km"],
                ["Pés", "Jardas", f"{valor} pés = {pesJarda:.2f} jardas"],
                ["Jardas", "Metros", f"{valor} jardas = {jardaMetro:.2f} metros"],
                ["Jardas", "Kilometros", f"{valor} jardas = {jardaKm:.2f} km"],
                ["Jardas", "Pés", f"{valor} jardas = {jardaPes:.2f} pés"]
            ]
            # Instrução para exibir a tabela estruturada.
            print(tabulate(comprimento, headers="firstrow", tablefmt="heavy_grid"))

        case 3:  # Executado se o usuário escolher a opção 3.
            limpar_tela()
            print("=========PESO=========")
            valor = float(input("Insira o valor da medida: "))
            mgGrama = float(valor / 1000)
            mgKg = float(valor / 1000000)
            mgLibras = float(valor / 453600)
            gramaMg = float(valor * 1000)
            gramaKg = float(valor / 1000)
            gramaLibras = float(valor / 453.6)
            kgMg = float(valor * 1000000)
            kgGrama = float(valor * 1000)
            kgLibras = float(valor * 2.205)
            librasMg = float(valor * 453600)
            librasGramas = float(valor * 453.6)
            librasKg = float(valor / 2.205)

            peso = [  # Estrutura da tabela para exibir os resultados de peso.
                ["De", "Para", "Resultado"],
                ["Miligrama", "Grama", f"{valor} mg = {mgGrama:.2f} g"],
                ["Miligrama", "Kilograma", f"{valor} mg = {mgKg:.2f} kg"],
                ["Miligrama", "Libra", f"{valor} mg = {mgLibras:.2f} lb"],
                ["Grama", "Miligrama", f"{valor} g = {gramaMg:.2f} mg"],
                ["Grama", "Kilograma", f"{valor} g = {gramaKg:.2f} kg"],
                ["Grama", "Libra", f"{valor} g = {gramaLibras:.2f} lb"],
                ["Quilograma", "Miligrama", f"{valor} kg = {kgMg:.2f} mg"],
                ["Quilograma", "Grama", f"{valor} kg = {kgGrama:.2f} g"],
                ["Quilograma", "Libra", f"{valor} kg = {kgLibras:.2f} lb"],
                ["Libra", "Miligrama", f"{valor} lb = {librasMg:.2f} mg"],
                ["Libra", "Grama", f"{valor} lb = {librasGramas:.2f} g"],
                ["Libra", "Kilograma", f"{valor} lb = {librasKg:.2f} kg"]
            ]
            # Instrução para exibir a tabela estruturada.
            print(tabulate(peso, headers="firstrow", tablefmt="heavy_grid"))

        case 4:  # Executado se o usuário escolher a opção 4, fazendo com que o programa encerre.
            break

        case other:  # Executado se o usuário escolher uma opção diferente de 1, 2, 3 e 4.
            print("Opção Inválida!")

    # Opção do usuário reiniciar o programa, a instrução
    reset = int(input("Deseja reiniciar? 1 - Sim || 2 - Não\n"))
    # ...é feita em conjunto com o while reset == 1 do inicio.
    if reset == 2:
        limpar_tela()
# É encerrado o programa quando a condição do while reset == 1 é dada como False.
limpar_tela()
print("Encerrando programa...")
