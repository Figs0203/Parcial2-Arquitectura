# Microservicio de Cálculo de Factorial

Este microservicio fue desarrollado en Flask y permite recibir un número entero por la URL para calcular su factorial y determinar si el número ingresado es par o impar.  
La respuesta se devuelve en formato JSON, lo que lo hace fácilmente integrable con otros sistemas o servicios.

---

# Análisis: Comunicación con otro servicio

Si este microservicio necesitara comunicarse con otro encargado de almacenar el historial de cálculos en una base de datos externa, el diseño se modificaría para incluir una llamada HTTP a ese servicio.
Por ejemplo, después de calcular el factorial, se podría enviar una solicitud POST con los datos del número, su factorial y la etiqueta (par o impar) al otro microservicio mediante la librería requests.

Este enfoque permite mantener una arquitectura desacoplada, en la que cada servicio cumple una responsabilidad específica: uno calcula y otro almacena. Además, esta separación mejora la escalabilidad y facilita el mantenimiento.
En escenarios de alta concurrencia, también se podría implementar comunicación asíncrona usando una cola de mensajes (como RabbitMQ o Kafka) para evitar bloqueos y manejar mejor la carga.
