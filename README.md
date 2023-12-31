# Extraer data de patiotuerca Ecuador

Indice
- Funcionalidad buscada
- Problemas encontrados
- Url API encontrada
- Capturas del programa funcionando
- Web service con Menu multimarcas para realizar consultas directas


## Funcionalidad buscada

  Con este codigo se pretende realizar la extración de información de una pagina de venta de autos con fines educativos en la cual se ha realizado el metodo de inspeción de código directamente en la pagina al realizar una busqueda para identificar su API la cual es [link](https://ecuador.patiotuerca.com/ptx/api/v2/nitros?type=autos&brand=kia&model=sportage%20r&subtype=&count=2&_=1695961279559) y con la cual mediante el código logramos extraer los datos requeridos lo cuales son (anio, ciudad, marca, modelo, precio), una vez obtenida la información se realizó la creación de un Webservice con el cual se puede presentar la información extraida mediante la siguiente direccion de red local mediante flask el cual nos permite colocando la direcciñon <http://127.0.0.1:3000/api/multiple/?marcas=kia,chevrolet,ford,hyundai,renault> crear consultas multiples de varias marcas o consultas individuales mediante el siguiente link <http://127.0.0.1:3000/api/renault>, una vez realizado este proceso se procedio a guardar en MongosDB dichas consulta utilizando la herramienta POSTMAN colocando en el metodo POST la url <http://127.0.0.1:3000/api/renault> y remplazando la palabra renault por varias marcas de autos como ford, hyundai, chevrolet y con esto completamos el objetivo planteado.

## Problemas encontrados.

  Problema1.- Encontrar una API valida para la extracción de datos, al momento de buscar en varias paginas de compras de autos muchas tenian APIs con data que no podia ser ordenada por lo cual no me servian para las pruebas que queria realizar.
  
  Problema2.- Realizar el proceso POST con la url multiple no logre enviar la información a la base de datos, solo puedo agregar información una marca a la vez.

## Url API encontrada

<https://ecuador.patiotuerca.com/ptx/api/v2/nitros?type=autos&brand=kia&model=sportage%20r&subtype=&count=2&_=1695961279559>

## Web service con Menu multimarcas para realizar consultas directas

Se preparo un menu en HTML el cual nos presenta una pantalla principal donde podemos elegir varias marcas o una en especifico para la extraccion de información.

**Webservice con multiples opciones de marcas**
![Pagina principal WEB service](imagenes/webservice_con_opciones_marcas.jpeg) 


## Capturas del programa funcionando

**Extracción de datos**
![Extracción de datos](imagenes/extract_datos.jpeg)

**Inicio de Web Service**
![Inicio de Web Service](imagenes/inicio_webservice.jpeg)

**Web service multiples marcas**

![Web service multiples marcas](imagenes/webservice_multiple.jpeg)

**Pinged a Mongosbd**
![Ping a Mongosbd](imagenes/pinged_mongos.jpeg)

**POSTMAN**
![POSTMAN](imagenes/post.jpeg)

**Registros guarados en MongosDB**
![Registros guarados en MongosDB](imagenes/registros_mongosdb.jpeg)   

**Webservice con multiples opciones de marcas**
![Pagina principal WEB service](imagenes/webservice_con_opciones_marcas.jpeg) 
