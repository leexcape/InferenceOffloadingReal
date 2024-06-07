import socket

def start_client(host='127.0.0.1', port=65432, message='Hello, World!'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f'Connected to {host}:{port}')
        s.sendall(message.encode())
        print(f'Sent data: {message}')

if __name__ == '__main__':
    start_client()
