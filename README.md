# Aprendendo Python com flask 

Faça o download da versão mais recente do Python

Criar um ambiente virtual para execultar o servidor dentro desse ambiente

python -m venv venv

Execultar o script do servidor pra ativar ele

.\venv\Scripts\activate

Instalar o Flask no ambiente virtual

python.exe -m pip install --upgrade pip
pip install flask

Criar o arquivo __init__.py 

Instalar um pacote de váriavel
pip install python-dotenv

Criar um arquivo .flaskenv

Para testar:
flask run
flask --app main.py --debug run

MYSQL

pip install Flask-MySQL
pip install PyMySQL
pip install Flask-SQLAlchemy


Ver pacotes:
pip freeze


npm install -D tailwindcss

npx tailwindcss init

npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch