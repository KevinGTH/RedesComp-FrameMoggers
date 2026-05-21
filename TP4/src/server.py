import socket
import threading
import json
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

HOST = "127.0.0.1"
PORT = 5050
BUFFER_SIZE = 1024

# Generar claves
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Preparamos la clave pública en formato de bytes (PEM) para enviarla
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


def handle_client(client_socket, client_address):
    ip_address = client_address[0]
    print(f"Hello {ip_address} welcome to the server!")

    # Enviar clave al cliente, despues de una conexion
    try:
        client_socket.sendall(public_key_bytes)
    except Exception as e:
        print(f"Error enviando clave: {e}")
        return

    try:
        while True:
            data = client_socket.recv(BUFFER_SIZE)

            if not data:
                break

            try:
                message = json.loads(data.decode("utf-8"))

                if (
                        isinstance(message, dict)
                        and "group" in message
                        and "payload" in message
                        and isinstance(message["group"], str)
                        and isinstance(message["payload"], str)
                ):
                    # Leer el payload
                    encrypted_payload = base64.b64decode(message["payload"])
                    decrypted_payload = private_key.decrypt(
                        encrypted_payload,
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None
                        )
                    )

                    print(f"{message['group']}: {decrypted_payload.decode('utf-8')}")
                else:
                    print(f"{ip_address} wants to send an ill formatted message.")

            except Exception as e:
                print(f"{ip_address} error procesando el mensaje: {e}")

    except ConnectionResetError:
        pass

    finally:
        print(f"Bye {ip_address}!")
        client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.start()

    except KeyboardInterrupt:
        print("\nServer stopped.")

    finally:
        server_socket.close()


if __name__ == "__main__":
    main()