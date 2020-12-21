# Sistema de Scrappeo sobre el Boletín de la Provincia de Tucumán

Este sistema fue desarrollado en contexto de mi práctica supervisada de grado en UTN FRT. 

## Resumen

El sistema consta de dos módulos. 
* Módulo de Obtención de datos: Consiste en la extracción automatica de los distintos avisos públicados diariamente en el [Boletín de la Provincia de Tucumán](https://boletin.tucuman.gov.ar). Dichos avisos son extraídos diariamente y almacenados. Se mantienen 2 opciones de almacenamiento: MySQL y MongoDB, los respectivos parametros de conexión deben ser proporcionados mediante un archivo llamado 'dev.env'.

* Módulo de Disposición de Datos: Consiste en la disposición de la información registrada vía API Rest. También incluse la posibilidad de actualizar avisos. [Ver Proyecto](https://github.com/IgnacioNicolasAlvarez/API_Boletin_Oficial_Tuc)



