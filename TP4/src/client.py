import socket
import json
import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

def encrypt_and_encode(public_key, plaintext: str) -> str:
    payload_bytes = plaintext.encode('utf-8')
    ciphertext = public_key.encrypt(
        payload_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(ciphertext).decode('utf-8')

def main():
    puerto = int(input("> Ingrese puerto remoto: "))
    ip_dir = input("> Ingrese dirección IPv4: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((ip_dir, puerto))
        print("Conexión TCP establecida exitosamente.")

        public_key_bytes = client.recv(2048)
        public_key = serialization.load_pem_public_key(public_key_bytes)

        current_group = input("> Defina el identificador de grupo inicial: ")

        while True:
            entrada = input("\n> Ingrese payload (o '/grupo' para modificar el grupo, 'salir' para abortar): ")
            
            if entrada.lower() == "salir":
                break
            
            if entrada.lower() == "/grupo":
                current_group = input("> Ingrese el nuevo identificador de grupo: ")
                continue
            
            if not entrada.strip():
                continue

            encoded_payload = encrypt_and_encode(public_key, entrada)
            
            trama_json = {
                "group": current_group,
                "payload": encoded_payload
            }
            
            client.sendall(json.dumps(trama_json).encode("utf-8"))
            print(" Trama JSON encriptada y enviada al buffer de transmisión.")

    finally:
        client.close()
        print(" Descriptor de socket liberado.")

if __name__ == "__main__":
    main()