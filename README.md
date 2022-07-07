# ec_msaddtolayaway

## Descripción

microservicio capaz de permitir agregar a una colección de MongoDB, uno o más cómics ligados a un usuario, se deberá de
cumplir con los siguientes criterios:

- CA1: Solo a los usuarios previamente registrados se les permitirá agregar comics a su registro
- CA2: Solo se podrán agregar comics existentes en el registro de Marvel
- CA3: En caso de no cumplir con los requisitos previos se deberá de notificar cuál es el problema existente
- CA4: Con el objetivo de cumplir con los primeros dos criterios, será necesario utilizar los microservicios de la parte
  1 y 2

## Requerimientos

- [python 3.9 o mayor](https://www.python.org/)
- [ms_comics](https://github.com/RicardoPizano/ec_comics)
- [ms_users](https://github.com/RicardoPizano/ec_users)

## Instalación

### Local

#### virtualenv (Opcional)

instalar virtualenv

``` bash 
$ pip3 install virtualenv 
``` 

crear virtualenv

``` bash 
$ virtualenv venv 
``` 

activar virtualenv

- linux

``` bash 
$ ./venv/bin/activate
``` 

- windows

``` bash 
$ ./venv/Scripts/activate
``` 

#### Dependencias

instalacion de dependencias

``` bash 
$ pip3 install -r requirements.tx
``` 

#### Ejecutar

``` bash 
$ python3 main.py
``` 

### Docker

#### Descargar imagen

``` bash
$ docker pull ec_maddtolayaway:latest
```

#### Crear contenedor

``` bash
$ docker run -d -p ${puerto}:80 --name container_ec_maddtolayaway ec_maddtolayaway 
```

## Edpoints

## /addToLayaway

#### POST
``` json
auth:
 En el header de la peticion mandar el token del usuario en formato Bearer
  Authorization : Bearer {user_token}
 
body request (opcional):
{
    "comic_id": int
}
body response:
{
    "user_id": "string",
    "user_name": "string",
    "comic": {
        "id": int,
        "title": "string",
        "image": "string",
        "onsaleDate": "string"
    }
}
```

##### Para mayor información una vez ejecutando el proyecto entrar a la url: `{base_url}/docs`
