# Sistema de Scrappeo sobre el Boletín de la Provincia de Tucumán

Este sistema fue desarrollado en contexto de mi práctica supervisada de grado en UTN FRT. 

## Resumen

El sistema consta de dos módulos. 
* Módulo de Obtención de datos (presente proyecto): Consiste en la extracción automatica de los distintos avisos públicados diariamente en el [Boletín de la Provincia de Tucumán](https://boletin.tucuman.gov.ar). Dichos avisos son extraídos diariamente y almacenados. Se mantienen 2 opciones de almacenamiento: MySQL y MongoDB, los respectivos parametros de conexión deben ser proporcionados mediante un archivo llamado 'dev.env'.

* Módulo de Disposición de Datos (__aún no empezado__): Consiste en un sistema mediante el cual será posible la consulta de los datos almancedos vía un servicio de API Rest. Dicho servicio implementará el esquema HATEOAS para proporcionar navegavidad dentro del servicio. Adicionalmente funcionará por medio de un servicio de autenticación mediante JWT.



