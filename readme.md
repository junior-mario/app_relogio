# Automação Relógio de Ponto

Este micro projeto foi criado para facilitar a coleta dos arquivos de registro de ponto dos relógios.

&nbsp;
## 🔥 Introdução

Tem por finalidade facilitar o download dos arquivos de registro de pontos utilizando automação do navegador 
Google Chrome utilizando Selenium.
A verssão 1.0 possibilita a coleta de todos os relógios de uma vez baseado na data informada.

&nbsp;
## ⚙️ Pré-requisitos

Para realizar a instalaÃ§Ã£o dos requisitos basta instala-los utilizando o comando abaixo.
Obs: o projeto foi feito para ser utilizado em maquinas com Windows 10.

**Instalação de todas as bibliotecas utilizadas no projeto**
```
pip install -r requirements. txt
```

* Ter acesso de administrador na pasta C:\temp
* Ter o navegador Google Chrome instalado



&nbsp;
## 🔨 Deploy Aplicação

Para criação do executavel para rodar em sistema Windows foi utilizado o Pyinstaller. 

![Static Badge](https://img.shields.io/badge/Pyinstaller-blue?link=https://pyinstaller.org/en/stable/)

&nbsp;

**Criar o executável com o icone padrão do Pyinstaller**
```
Pyinstaller --onefile  app_relogio.py 
```

**Criar o executável com o icone personalizavel**
```
Pyinstaller --onefile --icon=coffee.ico app_relogio.py
```

&nbsp;
## 🛠️ Executando

Para executar pode-se utilizar o seguinte comando após instalar os pré-requisitos.

```
python app_relogio.py
```

*Arquivos de ponto gerados pelo relógios serão armazenados em c:\temp* 

*Arquivos finalizados pelo programa serão armazenados em c:\temp\arquivos*

*É recomendado apagar os arquivos gerados em c:\temp\arquivos para evitar possiveis duplicações*


&nbsp;
## 📦 Tecnologias Utilizadas:


 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Static Badge](https://img.shields.io/badge/Pyinstaller-blue?link=https://pyinstaller.org/en/stable/)


&nbsp;
## 👷 Autores

* **Mario** - *desenvolvimento* - [Mario](https://github.com/junior-mario)

&nbsp;
## 📄 Licença

Esse projeto está sob a licença MIT - acesse os detalhes [LICENSE.md](https://github.com/junior-mario/calibracao/blob/main/LICENSE).


&nbsp;
## 💭 FAQ - Perguntas frequentes

#### Q: Está apresentando erro após gerar o arquivo do relógio

***A: Verifique se existe arquivos na pasta c:\temp\arquivos***