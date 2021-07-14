
# Creación de apis y microservicios con framework serverless-python

## Installation
Prerequisito configurar aws cli - https://tinyurl.com/3v8ccr84

Ejecutar el siguiente comando para instalar serverless 

```bash
$ npm install -g serverless
```

## Establecer las credenciales en el archivo serverless.yml
```bash
USER
PASSWORD
HOST
PORT
DATABASE
```

Creación de entorno virutal para desarrollar los microservicios.
Referencia: https://tinyurl.com/w7fa6yy8

```bash
$ cd py-test
$ pip install virtualenv
$ python -m virtualenv venv
$ .\venv\Scripts\activate
(venv) $
```

Instalar las librerias que se requieran ejemplo.

```bash
$ pip install mysqlclient
```

Realizar prueba de microservicio ejemplo.

```bash
(venv) $ python like.py
```

Desactivar el ambiente virutal.

```bash
$ deactivate
```
## Instalar plugin serverless-python-requirements

```bash
$ sls plugin install -n serverless-python-requirements
```

## Serverless Offline
Para realizar pruebas de los microservicios localmente.

```bash
$ npm install serverless-offline --save-dev
```

En el directorio del proyecto ejecutar comando. 

```bash
$ serverless offline
```
Se mostraran los endpoints locales para consumirlos 

## Deploy project 

Para realizar la creación y actualización de los endpoints(apigateway) junto con los microservicios(lambda function) y configuraciones como roles políticas etc. 

```bash
$ serverless deploy
```

Esto se crea con el servicio de forma interna de cloudformation. 

