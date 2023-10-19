# API de gerenciamento de tarefas serveless

Esse projeto tem como objetivo exemplificar o desenvolvimento de uma API de gerenciamento de tarefas em ambiente serveless onde suas rotas serão disponibilizadas através de uma função lambda e persistida em um banco Mysql na RDS.

ATENÇÃO: Esse projeto não contempla um sistema mais restrito de segurança, onde o usuário deverá apresentar chave de autenticação para "bater" nas rotas via HTTP.

## Tecnologias Utilizadas

- Linguagem Python 3.7.9
- Framework Chalice
- Lambda da AWS
- Banco Mysql - RDS AWS
- API Gateway AWS
- AWS CLI

# Conhecendo Serveless

Serverless é um modelo de desenvolvimento nativo em nuvem para criação e execução de aplicações sem o gerenciamento de servidores.

Os servidores ainda são usados nesse modelo, mas eles são abstraídos do desenvolvimento de aplicações. O provedor de nuvem fica responsável pelas tarefas rotineiras de provisionamento, manutenção e escala da infraestrutura do servidor. Os desenvolvedores só precisam empacotar o código em containers para fazer a implantação.

Depois da implantação, as aplicações serverless atendem à demanda e aumentam ou diminuem a escala automaticamente de acordo com as necessidades. As soluções serverless dos provedores de nuvem pública costumam ser oferecidas sob demanda por meio de um modelo de execução orientado a eventos. Por isso, não há cobrança pelas funções serverless não utilizadas.

# O que são Lambdas?

O AWS Lambda é um serviço de computação que permite executar código sem o provisionamento ou gerenciamento de servidores.

O Lambda executa seu código em uma infraestrutura de computação de alta disponibilidade e executa toda a administração dos recursos computacionais, incluindo manutenção do servidor e do sistema operacional, provisionamento e escalabilidade automática da capacidade e registro em log do código. Com o Lambda, tudo o que você precisa fazer é fornecer seu código em uma dos runtimes de linguagens compatíveis com o Lambda.

Você organiza seu código em Funções do Lambda. O serviço do Lambda executa a função somente quando necessário e escala automaticamente. Você paga apenas pelo tempo de computação consumido. Não haverá cobranças quando o código não estiver em execução.

# Requisitos para executar o projeto

Para que o projeto seja executado corretamente serão necessários executar os seguintes passos:

- Criar uma conta root na plataforma de serviço em nuvem AWS.
- Criar uma conta de administrador na plataforma AWS através da conta root.
- Criar politicas e regras de acesso aos serviços Lambda e RDS Mysql.
- Adicionar um novo "security group" através do serviço EC2 - Atenção nos ips que serão liberados.
- Instanciar um novo banco Mysql através do serviço RDS da AWS - Pode ser o modelo Free Tier
- Ter uma IDE instalada - Aconselho VSCode ou Pycharm
- Ter o Git instalado
- Ter o Python 3.7.9 instalado
- Ter o Chalice instalado

# Instalando Python

A versão utilizada no projeto é a 3.7.9 que pode ser baixada através do link:
https://www.python.org/downloads/
Dúvidas de como instalar o Python e outro assuntos relacionados clique no link abaixo:
https://devguide.python.org/getting-started/setup-building/

# Instalando AWS CLI

A AWS Command Line Interface (AWS CLI) é uma ferramenta unificada para o gerenciamento de seus produtos da AWS. Com apenas uma ferramenta para baixar e configurar, você poderá controlar vários produtos da AWS pela linha de comando e automatizá-los usando scripts.

Para instalar o AWS CLI siga as instruções do link abaixo:
https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html

Após a instalação do AWS ClI, através do prompt de comando (com nível administrador) digite:

```sh
$ aws configure
```

Insira as informações solicitadas:

- AWS Access Key ID - (Fornecidas na criação do usuário adm)
- AWS Secret Acess Key - (Fornecidas na criação do usuário adm)
- Default region name - Atenção para a região na qual você selecionou no sistema (ex.: sa-east-1)
- Deafult output format - json

Pronto, AWS CLI estará configurado!

# Executando o programa

1. Crie um ambiente virtual na sua maquina para Python 3.7.9
2. Com ambiente virtual ativado, digite:

```sh
$ git clone repositorio
```

3. Agora instale as dependencias no seu ambiente virtual que estão dentro de requirements.txt digitando:

```sh
$ pip install -r requirements.txt
```

4. Insira as credenciais do seu banco de dados no arquivo "**_ init _**.py" localizado dentro da pasta "chalicelib"
5. No terminal da IDE ou através de um prompt, dentro da pasta principal digite:

```sh
$ phyton db_create.py
```

Será criado uma tabela no seu banco de dados com as seguintes entidades: id/descricao/status/dataCricao 5. Agora com a tabela criada com suas entidades é hora de executar o servidor como local para testes, acesse a pasta "apitodo" e digite no terminal ou prompt:

```sh
$ chalice local
```

Será executado um servidor local, clique sobre o link disponibilizado para acessar via seu browser ou programa de requisições como Postman/Insominia através das rotas da API. Mais informações das rotas no tópico "Rotas disponibilizadas". 6. Após efetuar o teste local e verificar que a API está funcionando perfeitamente, está na hora de efetuarmos o deploys da aplicação para AWS, para tal através do terminal ou prompt digite:

```sh
$ chalice deploy
```

O Chalice irá executar várias ações na AWS através das credenciais configuradas na AWS CLI, dentre as ações são configurações de regras e politicas de acesso, criação da lambda e configurar uma rota pública através do API Gateway.

# Documentação - Rotas disponibilizadas

Link da documentação
Vocë pode utilizar qualquer aplicativo de consulta de rotas como Postman ou Insominia para efetuar as requisição

Observações Importantes:

- Essa API foi desenvolvida de forma simples não levando em conta restrições de acesso ou autenticações através de regras configuradas dentro da AWS.
- A criação dessa API teve como base a criação de um ambiente virtual como manda as boas práticas de desenvolvimento.
