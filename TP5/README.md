# Redes de Computadoras

## Trabajo Practico N°5

### Grupo: Frame Moggers

### Integrantes

* **Bejarano, Kevin**
* **Bustos, Hugo Gabriel**
* **Gonzalez, Macarena**
* **Nieto, Marcos**

### Consignas
1) Reconocimiento de arquitectura.

Firewall: Bloquea requests maliciosos.
Load Balancer: Distribuye trabajo entre unidades de cómputo disponibles usando round robin.
Compute: Hace el procesamiento de los requests. Decide donde enviar el paquete. Ej: READ a la DB.
Database:
Storage: Guarda datos. Maneja tráfico UPLOAD/STATIC sin ser una carga para Compute. Si no está, no se pueden guardar datos.
Memory Cache: Guarda respuestas en RAM. Da servicio a READs repetidos sin tocar la base de datos. Alrededor de 40% de los READs pueden ser leídos de la Cache. De no estar presente, la DB se ve sobreexigida.
Message Queues: Introduce un búfer para manejar los picos de tráfico, para que Compute pueda procesarlos a su tiempo. Previene los request drop durante estos picos de tráfico.
