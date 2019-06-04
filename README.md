# Minicurso de Django

Repositório para divulgar os arquivos desenvolvidos durante o minicurso na disciplina de Linguagem de Programação III.

## Instalação do Python

Faça o download do [Python](https://www.python.org/downloads/ "Python")

Ao fazer a instalação do Python, assegure-se de marcar as seguintes caixas de seleção: 

![alt text](https://i.ibb.co/1XY0gZF/Capture.png "Install Python 1")

Clique em "Customize Installation e deixe marcado pip.

![alt text](https://i.ibb.co/qpdhJKx/Capture.png "Install Python 2")

## Instalação do Ambiente Virtual

No seu terminal, instale o virtual environment com o seguinte comando:

`pip install virtualenv`

Na área de trabalho crie uma pasta de um nome qualquer e acesse essa pasta via terminal utilizando os comandos de mudança de diretório (cd ou semelhantes). Ao acessá-la, digite o seguinte comando (onde nomeEnv seja um nome qualquer): 

`python -m venv nomeEnv` 

Criado o seu ambiente virtual, ative ele com os seguintes comandos: 

`nomeEnv/Scripts/activate` para Windows e `source nomeEnv/bin/activate` para Mac/Linux

Com o ambiente virtual ativado, teremos algo parecido com isso no terminal:

![alt text](https://i.ibb.co/V36WdSg/Capture.png "Install venv 1")

Teremos algo como o escrito em verde (teste) ao lado do caminho do seu projeto. Só vá para o próximo passo se estiver tudo conforme o tutorial até o momento.

Com o seu ambiente virtual ativado, digite a seguinte linha de comando no seu terminal:

`python –m pip install Django`

Para desativar o ambiente virtual após o uso é bem simples, apenas digite no seu terminal o comando:

`deactivate`

Após tudo funcionando, é só seguir os passos do slide disponibilizado.

## Autor

Douglas Frota Brandão - [douglasbrandao](https://github.com/douglasbrandao "Douglas Brandão")
