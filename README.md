# Microservicio de Cálculo de Factorial

Este microservicio fue desarrollado en Flask y permite recibir un número entero por la URL para calcular su factorial y determinar si el número ingresado es par o impar.  
La respuesta se devuelve en formato JSON, lo que lo hace fácilmente integrable con otros sistemas o servicios.

---

# Análisis: Comunicación con otro servicio

Si este microservicio debiera comunicarse con otro encargado de almacenar el historial de cálculos en una base de datos externa, sería necesario modificar su arquitectura para incorporar un mecanismo de interacción entre servicios. La idea principal sería que, una vez realizado el cálculo del factorial y determinada la paridad del número, el microservicio actual enviara estos resultados al otro servicio mediante una solicitud HTTP, generalmente usando el método POST. Esto se podría implementar fácilmente con la librería requests de Python, enviando los datos en formato JSON.

Esta integración permitiría que el microservicio de cálculo se mantuviera ligero y especializado, ya que delegaría la gestión del almacenamiento a un servicio independiente. De esta forma, cada componente cumpliría una función específica: uno calcula y otro guarda los resultados. Esta separación de responsabilidades favorece el desacoplamiento, facilita el mantenimiento y permite escalar cada parte de manera independiente según la demanda o carga de trabajo.

En un escenario más complejo o de alta concurrencia, podría considerarse el uso de una cola de mensajería para manejar la comunicación de manera asíncrona. Esto evitaría que el servicio de cálculo dependa directamente de la disponibilidad del servicio de almacenamiento, mejorando la resiliencia, reduciendo la latencia percibida y permitiendo que el sistema crezca sin afectar su rendimiento general.
