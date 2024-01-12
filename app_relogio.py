from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import socket
import shutil

# Funções

def coleta_data():
    print('Insira a data no seguinte formato  DD/MM/YYY: ')
    data = input(' ►►► ').split('/')
    return data


def nome_ultimo_arquivo(caminho):
    lista_arquivos = os.listdir(caminho)
    lista_datas = []
    for arquivo in lista_arquivos:
        data = os.path.getmtime(f"{caminho}/{arquivo}")
        lista_datas.append((data, arquivo))

    lista_datas.sort(reverse=True)
    ultimo_arquivo = lista_datas[0]
    

    if "AFD" not in ultimo_arquivo[1]:
        time.sleep(3)
        print("ARQUIVO AFD NÃO É O ULTIMO DA LISTA")
            # Chama recursivamente a função para tentar novamente
        return nome_ultimo_arquivo(caminho) 

    for iten in lista_datas:
        print(iten)
    return ultimo_arquivo[1]




def lista_arquivos_gerados(caminho_destino):
    lista_arquivos = os.listdir(caminho_destino)
    lista_arquivos_finalizados = []
    for arquivo in lista_arquivos:
        #data = os.path.getmtime(f"{caminho_destino}/{arquivo}")
        lista_arquivos_finalizados.append(arquivo)

        print('\n\n\n')
        print('----------------------------------------------------------------')
        print("|                Arquivos gerados.                              |")

    for iten in lista_arquivos_finalizados:

        print(f"                {iten}                   ")


    print('----------------------------------------------------------------')
    print('\n')
                

def imprimi_lista(lista, titulo):

    print('\n\n\n')
    print('----------------------------------------------------------------')
    print(f"|                {titulo}                   |")

    for iten in lista:

        print(f"                {iten}                   ")

    print('----------------------------------------------------------------')
    print('\n')




# def xxxx():
#     contador = 0
#     while contador == 0:
#         if "AFD" not in ultimo_arquivo[1]:
#             time.sleep(3)
#             print("ARQUIVO AFD NÃO É O ULTIMO DA LISTA")
#              # Chama recursivamente a função para tentar novamente
#             return nome_ultimo_arquivo(caminho)
#         else:
#                 contador = 1    




def verifica_relogios():
    servers = [ 
            "192.168.1.130:443:SRQB", 
            "192.168.1.134:443:Portaria_2", 
            "192.168.2.18:443:Portaria_1", 
            "192.168.1.131:443:Clube_Hipico",
            "192.168.1.133:443:Vila_Hipica",
            "192.168.1.132:443:Clube_Mata",
            "192.168.2.20:443:Sede_Golfe",
            "192.168.2.21:443:Manut_Golfe",
            "192.168.2.19:443:Golfe_CHQB",
            "192.168.2.17:443:Hipico_SRQB",
            "192.168.2.22:443:Bombeiros", 
            "10.0.128.74:443:Reserva" 
            ]

    for server in servers:
        try:
            host, port, empresa = server.split(":")
            port = int(port)
            socket.create_connection((host, port), 3)
            print(server, "OK")
            #print(server)
            dispositivos_up = (host, empresa)
            lista_up.append(dispositivos_up)
        except:
            print(server, "FAIL")
            dispositivos_down = (host, empresa)
            lista_down.append(dispositivos_down)


    #print("UP")
    #print(lista_up)
    #print("------")

    #print("DOWN")
    #print(lista_down)
    #print("------")
    return lista_up, lista_down

#lista_up, lista_down = verifica_relogios()



# Cria os arquivos baseados na lista_up que mostra os relogios que estao online
# Criar um dicionario contendo os nomes dos arquivos que foram criado
# utilizando o nome do setor para consultar arquivo criado para poder adiconar o conteudo do arquivo obtido do relogio

def cria_arquivos_com_cabecalho(data_atual, lista_up, cabecalho):
    lista_nome_arquivos = {}
    print("ENTROU NA FUNÇÃO CRIAR ARQUIVO")
    for setor in lista_up:
        nome_arquivo = setor[1]+ "_" + data_atual +".txt" # cria o nome do arquivo
        nome_arquivo_completo = os.path.join(caminho,nome_arquivo) # Cria o caminho absoluto do arquivo
        print(f" NOME DO ARQUIVO: {nome_arquivo}")
        setor =  setor[1]
        #print(key)
        #print(nome)
        
        lista_nome_arquivos[setor] = nome_arquivo_completo
        f2 = open(nome_arquivo_completo, "x") # cria um arquivo vazio
        f2.write(cabecalho[setor]) # adiciona o cabeçalho no arquivo criado
        f2.close() # fecha o arquivo
        #print(dict)
    return lista_nome_arquivos



# Variaveis

cabecalho = {
    "SRQB":"0000000001103885489000114000000000000SOCIEDADE RESIDENCIAL QUINTA DA BARONEZA                                                                                                              0001400375003430301012001170720181707201809033c3d",
    "Portaria_2":"0000000001103885489000114000000000000SOCIEDADE RESIDENCIAL QUINTA DA BARONEZA                                                                                                              00014003750036218010120012307201823072018101726d9",
    "Portaria_1":"0000000001103885489000114000000000000SOCIEDADE RESIDENCIAL QUINTA DA BARONEZA                                                                                                              000140037500235230101200123072018230720181030e6be",
    "Clube_Hipico":"0000000001103885501000190000000000000CLUBE HIPICO QUINTA DA BARONEZA                                                                                                              000140037500234980101200123072018230720181016bd95",
    "Vila_Hipica":"0000000001103885501000190000000000000CLUBE HIPICO QUINTA DA BARONEZA                                                                                                              00014003750036804010120012307201823072018101670d7",
    "Clube_Mata":"0000000001103885501000190000000000000CLUBE HIPICO QUINTA DA BARONEZA                                                                                                              000140037500343810101200122072018230720181017f416",
    "Sede_Golfe":"0000000001105089568000144000000000000QUINTA DA BARONEZA GOLFE CLUBE                                                                                                              0001400375002392501012001230720182307201810184abf",
    "Manut_Golfe":"0000000001105089568000144000000000000QUINTA DA BARONEZA GOLFE CLUBE                                                                                                              000140037500342850101200123072018230720181018b0c0",
    "Golfe_CHQB":"0000000001103885501000190000000000000CLUBE HIPICO QUINTA DA BARONEZA                                                                                                              0001400375003000301012001220720182307201810184b8f",
    "Hipico_SRQB":"0000000001100885489000114000000000000SOCIEDADE RESIDENCIAL QUINTA DA BARONEZA                                                                                                              000140037500234390101200123072018230720181019ba0e",
    "Bombeiros":"0000000001103885489000114000000000000SOCIEDADE RESIDENCIAL QUINTA DA BARONEZA                                                                                                              0001400375015056401012001180820211808202111098e0c",
    "Reserva":"0000000001123192716000133000000000000CONDOMINIO RESERVA DOS IPES                                                                                                              000140037501055430101200118082021180820211106f030"
    
        }

lista_up = []
lista_down = []
data_atual = time.strftime("%d-%m-%Y")
data = coleta_data()
caminho = r"C:\temp"
user = "admin"
pass01 = "121314"
pass02 = "admin" 



# Caminho da pasta de destino
caminho_destino = r'C:\temp\arquivos'

# Verifica dispositivos on
lista_up, lista_down = verifica_relogios()

# Cria os arquivos TXT dos relogios que estão UP
lista_nome_arquivos = cria_arquivos_com_cabecalho(data_atual, lista_up, cabecalho) 


# Inicializando instancia google

# Classe service é usada para iniciar uma instancia do webdrive
service = Service()

# webdriver.ChromeOptions é usada para definir a preferencia para o navegador chrome
options = webdriver.ChromeOptions()
#options = webdriver.FirefoxOptions()
# executa o navegador em segundo plano
#options.add_argument("--headless") 
# ignora erro de certificado
options.add_argument('--ignore-certificate-errors')

options.add_experimental_option("prefs", {
  "download.default_directory": caminho
})

# inicia-se a instancia do chrome
driver = webdriver.Chrome(service=service, options=options)
#driver = webdriver.Firefox(service=service, options=options)


# Realizando o acesso ao site
cont = 0
for relogio in lista_up:
    ip, empresa = relogio
    url="https://" + ip + "/"
    #print(url)
    #driver.get(url)
    if ip == "10.0.128.74" or ip == "192.168.1.131" or ip == "192.168.2.22" or ip == "192.168.2.19":
            print("senha é admin")
            password = "admin"
    else:
            print("senha padrão")
            password = "121314"
    

    driver.get(url)
     
# Econtrando os elementos para realziar o login
                
    # encontra o campo de usuario
    elemento = driver.find_element(By.XPATH, '//*[@id="input_user"]').send_keys('admin')

    # encontra o campo de senha
    elemento = driver.find_element(By.XPATH, '//*[@id="input_password"]').send_keys(password)

    elemento = driver.find_element(By.XPATH, '//*[@id="logar"]').click()   

    time.sleep(2)
    driver.maximize_window()
    elemento = driver.find_element(By.XPATH, '//*[@id="MasterPage_menu"]/div/ul/li[4]/a').click()
    #driver.find_element(By.XPATH, '//*[@id="MasterConteudo"]/div[3]/div/div[3]/button[1]').text

    # codigo para poder abrir o popup
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MasterPage_menu"]/div/ul/li[4]/ul/li[3]/a'))).click()

# Inserindo data e fazendo o download
    time.sleep(3)

    # Clica na caixa de data
    elemento = driver.find_element(By.XPATH, '//*[@id="initial_date"]').click()
    elemento = driver.find_element(By.XPATH, '//*[@id="initial_date"]').clear()
    elemento = driver.find_element(By.XPATH, '//*[@id="initial_date"]').send_keys(data)

    elemento = driver.find_element(By.XPATH, '//*[@id="MasterConteudo"]/div[3]/div/div[3]/button[2]').click()
    time.sleep(4)

# Alterando o nome do arquivo mais recente
    ultimo_arquivo = nome_ultimo_arquivo(caminho) # arquivo mais recente contido na pasta


    ultimo_arquivo =  os.path.join(caminho,ultimo_arquivo) # Cria o caminho absoluto do arquivo
    print(f" ULTIMO ARQUIVO LOCALIZADO: {ultimo_arquivo}") 
    #print(f" IMPRIMINDO LISTA UP {lista_up[cont]}")
    dispositivo, nome_empresa = lista_up[cont] # ip do dispositivo e qual empresa ele pertence

    #print(dispositivo)
   

    
    arquivo_criado = lista_nome_arquivos[nome_empresa] # pega o nome do arquivo gerado contendo o cabeçalho
    print(f"ARQUIVO CRIADO COM CABEÇALHO: {arquivo_criado}")




    f_download  = open(ultimo_arquivo) # Abre o arquivo que exportado do relogio
    texto = f_download.read()# le o conteudo do arquivo exportado
    f_download.close()
    #print(texto)


    f_criado  = open(arquivo_criado,"a") # abre o arquivo existente
    f_criado.write("\n") # adiciona uma quebra de linha
    f_criado.writelines(texto) # grava o conteudo do arquivo baixado no arquivo criado
    f_criado.close()




    # Garante que a pasta de destino existe, caso contrário, a cria
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)

    # Move o arquivo para a pasta de destino
    shutil.move(arquivo_criado, caminho_destino)
    print(f"Arquivo movido para {caminho_destino}")

    cont = cont + 1


os.system('cls')

lista_arquivos_gerados(caminho_destino)
titulo = "Relógios sem acesso a rede."
imprimi_lista(lista_down, titulo)
driver.quit()
time.sleep(30)