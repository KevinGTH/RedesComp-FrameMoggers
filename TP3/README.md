
# Redes de Computadoras

## Trabajo Practico N°2

### Grupo: Frame Moggers

### Integrantes

* **Bejarano, Kevin**
* **Bustos, Hugo Gabriel**
* **Gonzalez, Macarena**
* **Nieto, Marcos**

### Desarrollo

#### 1) Investigación conceptual.

1. SSH es un protocolo de red criptográfico. Proporciona servicios de autenticación y cifrado de mensajes. Soluciona el problema de cómo mantener una conexión segura en una red no confiable. Se diferencia en ésto de telnet, donde los datos se transfieren en texto plano.

2. Autenticación refiere al proceso de verificar la identidad de cada una de las partes involucradas en la comunicación. Encriptación es el proceso por el cual los mensajes enviados por la red son cifrados a propósito de mantener su confidencialidad.

3. Son los elementos claves de la criptografía asimétrica. Permiten cifrar datos y verificar identidades. Un usuario crea un par de llaves relacionadas, una pública, la otra privada. 
    **Criptografía:** Si Anabel quiere comunicarse de forma segura con Bartolomeo, encripta el mensaje a enviar con la clave pública de éste último. Bartolomeo usa entonces su clave privada para descifrar el mensaje.  
    **Autentificación:** Si Bartolomeo quiere demostrar que es el remitente de un mensaje, lo firma con su clave privada. Cualquiera puede entonces verificar la firma usando la clave pública de Bartolomeo.

4. En adición a poder descifrar cualquier mensaje seguro del que seamos destinatarios, un agente malicioso puede usar nuestra clave privada para mandar mensajes como si fueramos su remitente.

5. Las claves SSH son prácticamente imposibles de forzar, comparadas con las contraseñas generadas por humanos. Eliminan riesgos como la intercepción de contraseñas, ya que la clave privada nunca se envía al servidor. Ganan en conveniencia también, permitiendo log-ins sin contraseña y el uso de scripts para aplicaciones como interacciones automáticas con servidores, etc.
