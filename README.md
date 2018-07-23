**Requisitos**
-----------------
* Django
* Docker (opcional)
* Docker-compose (opcional)

**Instruções**

- Em caso de usar apenas o Django siga os seguintes passos (Caso use o docker pule tudo isso):

Instale as bibliotecas e dependências necessárias indicadas no requirements.txt

`pip install -r requirements.txt`

Após a instalação vá para SGEHookah/SGEHookah/SGEHookah/settings.py e altere as seguintes informações:

**Antes**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': 'db',
        'PORT': 5432,
    },
    'backup': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

**Depois**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Após alterar o settings.py rode o servidor de testes

*SGEHookah/SGEHookah/manage.py*

`python manage.py runserver`

O Django roda no port 8000, então para entrar no navegador :
**localhost:8000**

# Docker e Docker-compose

Primeiramente instale o Docker CE e o Docker-compose:
- [Docker CE](https://www.docker.com/community-edition#/download)
- [Docker-compose](https://docs.docker.com/compose/)

Após a instalação faça o clone do repositório (branch docker-dev), vá para a pasta do repositório e rode os seguintes comandos:

```
docker-compose build

docker-compose up
```
(Há um pequeno bug onde no primeiro docker-compose up o sistema gera um erro. Apenas cancele e rode novamente o docker-compose up)

Quando estiver tudo ok basta usar o sistema no **localhost** (o port utilizado é **80**)

# SGEHookah
Repositório de desenvolvimento do sistema SGE Hookah para o cliente Rafael Prada em parceria com a Faculdade Impacta

## Docker-Dev

Este branch foi feito especificamente para os desenvolvedores poderem baixar e acessar os arquivos necessários para fazer uso do
sistema.
