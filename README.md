# Rodando Python com Flask, MySQL e Tailwind 

### Requisitos

- Faça o download da versão mais recente do [Python](https://www.python.org/downloads/).

### Configuração do Ambiente

1. Crie um ambiente virtual para executar o servidor dentro desse ambiente:
    ```sh
    python -m venv venv
    ```

2. Ative o ambiente virtual:
    ```sh
    .\venv\Scripts\activate
    ```

3. Atualize o `pip` e instale o Flask no ambiente virtual:
    ```sh
    python.exe -m pip install --upgrade pip
    pip install flask
    ```

### Estrutura do Projeto

1. Crie o arquivo `__init__.py`.

2. Instale o pacote de variáveis de ambiente:
    ```sh
    pip install python-dotenv
    ```

3. Crie um arquivo `.env`.

### Executando o Servidor

Para testar em modo de **produção** o servidor, utilize os comandos:

```sh
flask run
```

ou para rodar em modo de **teste**:

```sh
flask --app main.py --debug run
```
### Integração com MySQL
Instale os pacotes necessários para trabalhar com **MySQL**:

```sh
pip install Flask-MySQL
pip install PyMySQL
pip install Flask-SQLAlchemy
```

### Verificação de Pacotes

Para ver a lista de pacotes instalados, utilize:

```sh
pip freeze
```

### Configuração do Tailwind CSS

1. Instale o Tailwind CSS:

```sh
npm install -D tailwindcss
```

2. Inicialize o Tailwind CSS:

```sh
npx tailwindcss init
```

3. Compile os estilos CSS:

```sh
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```

> Pronto! Agora você está configurado para desenvolver seu projeto Flask com suporte para Tailwind CSS.

### Extras
```sh
flask --app hello run --host 0.0.0.0
pip freeze > requirements.txt
pip install -r requirements.txt


```
