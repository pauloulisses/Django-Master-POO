# input - entrada  / output - saída
# Algoritmo - Escrever o passo a paaso de uma tarefa que precisa ser executada

# 1. Um passo a passo

1. ir dormi

2. porta do quarto ta fechada?

3. se sim: abrir a porta

4. se não entrar no quarto

5. a luz está acesa?

6. se sim - desligar a luz

7. se não - ir para a cama

8. fim dormi

# Oque é Django
# Framework web
# para python feito em python
# Código aberto (open source)
# Arquitetura MVT
# Full Stack

# Oque ele faz 
# sites, blogs, redes sociais
# sistemas web completos
# ERPs - sistemas de gestão para uma empresa
# CRMs - controle de atendimentos, sistemas para vendedores
# PDVs - ponto de vendas sistemas de mercados
# APIs(DRF) - apisRest

# sistemas Desktop vs Sistemas Web

Sistemas Desktop:
São programas instalados no computador do usuário.
Funcionam localmente (mesmo sem internet, na maioria dos casos).



Sistemas Web:
São acessados pelo navegador (Chrome, Edge, Firefox).
Rodam na internet ou rede interna.
Não precisam ser instalados no PC.
Exemplos: WhatsApp Web, Gmail, sistemas de banco, sites em geral.

Resumo rápido:
Desktop = instalado no computador
Web = acessado pelo navegador


# protocolo HTTP

# Protocolo HTTP (HyperText Transfer Protocol)


HTTP é o protocolo usado para comunicação entre navegador (cliente) e servidor na web.

Em resumo:
O navegador faz uma requisição (request)
O servidor responde com dados (response)

É assim que sites, APIs e sistemas web funcionam.

Exemplo simples:
Cliente pede uma página → Servidor envia a página
Cliente pede dados → Servidor envia JSON

Principais métodos HTTP:
GET    → buscar dados
POST   → enviar dados
PUT    → atualizar dados
DELETE → apagar dados

HTTP é sem estado (stateless):
Cada requisição é independente da outra.

Hoje em dia usamos muito o HTTPS (HTTP + segurança com criptografia).



# Ambiente Virtual (Virtual Environment)

Ambiente virtual é um espaço isolado para projetos Python.
Ele permite que cada projeto tenha suas próprias bibliotecas e versões,
sem afetar o Python instalado no sistema.

Isso evita conflitos entre dependências.

------------------------------------------------
PASSO A PASSO PARA CRIAR E USAR UM AMBIENTE VIRTUAL
------------------------------------------------

1) Abra o terminal dentro da pasta do seu projeto

2) Crie o ambiente virtual com o comando:

   python -m venv venv

   (isso cria uma pasta chamada "venv")

3) Ative o ambiente virtual:

   No Windows (CMD):
   venv\Scripts\activate

   No Windows (PowerShell):
   venv\Scripts\Activate.ps1

4) Quando ativar, aparecerá no terminal:

   (venv)

   Isso significa que o ambiente está funcionando.

5) Agora instale pacotes normalmente:

   pip install nome_do_pacote

6) Para sair do ambiente virtual:

   deactivate

------------------------------------------------
Resumo:
Cada projeto deve ter seu próprio ambiente virtual Python.
------------------------------------------------

