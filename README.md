# vulcano-weather

API desarrollada con el framework FastAPI (Lang: Python 3.8)
con el fin de brindar al usuario vulcaniano
la posibilidad de conocer el clima de su planeta en ciertos periodos de tiempo

La documentacion Swagger de los servicios expuestos puede ser 
revisada en el navegador con la url: /docs (el host puede variar, si se ejecuta de manera local):

Swagger UI: [Link text Here](https://vulcano-weather-z2exu4tjca-uc.a.run.app/docs)


## Supocisiones

- El planeta ferengi tendrá un año solar de 360 dia (mayor facilidad para transformar luego a coordenadas rectangulares) 
por lo que los 10 años se calcularán sobre este supuesto. 

- En un inicio la posicion por defecto de los planetas será alineados en el eje x positivo
con respecto al sol 

- El perimetro maximo del triangulo se calculó como la distancia maxima
de la recta entre los dos planetas con mayor radio.

- Un dia o mas con cierto clima se considerara un periodo 

  
## Servidor en la nube (GCP)

* postgres DB -> Instancia de GPC CloudSQL (configuracion horizontal y vertical minima para el proyecto)
* Servidor con 2 instancias (configuracion horizontal minima) escalable a maximo 3 -> GCP Cloud Run


- **URL del Servicio:** [Link text Here](https://vulcano-weather-z2exu4tjca-uc.a.run.app/)
- **URL con la documentacion de los servicios REST expuestos:** [Link text Here](https://vulcano-weather-z2exu4tjca-uc.a.run.app/docs)
- **URL con las respuestas del ejercicio:** [Link text Here](https://vulcano-weather-z2exu4tjca-uc.a.run.app/weather/periods/count)


## Ejecucion Local
### Requerimientos 
* Python3.6+
* PostgresSQL 10+
* Tener instalado PIP
* Posicionarse en la carpeta del proyecto
* pip install -r requirements.txt
* ejecutar el comando por consola:

```
DB_NAME="db_name" DB_HOST="db_host" DB_PORT="db_port" DB_USER="db_user" DB_PASSWORD="db_password" uvicorn main:app --host localhost --port 8082
```

Nota: Cambiar lo que está entre comillas por la configuracion local/remota definida
en su base de datos

### TESTS: Ejecutar de manera local

Para ejecutar los test de manera local se debe asignar las variables de entorno
seguido del comando pytest

```
DB_NAME="db_name" DB_HOST="db_host" DB_PORT="db_port" DB_USER="db_user" DB_PASSWORD="db_password" pytest
```
