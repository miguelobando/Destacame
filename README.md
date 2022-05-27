# frontend-destacame

## Desiciones técnicas

Se utilizó nuxt.js para mostrar la capacidad de adaptación del desarrollador con frameworks basados en vue.js, adicionalmente se utilizó bulma css como framework css y django con django api rest framework para el backend

## Instalación y despliegue de frontend

Abrir una consola y ejecutar los siguientes comandos

```bash
$ cd Frontend
$ npm install
$ npm run dev
```

## Instalación y despliegue de backend

Abrir otra console y ejecutar los siguientes comandos

```bash
$ cd Backend
$ pip install virtualenv
$ python -m virtualenv env
$ source env/Scripts/activate
$ pip install -r requirements.txt
$ py manage.py makemigrations
$ py manage.py migrate
$ py manage.py runserver
```

La prueba estará desplegada en localhost:3000 :)
