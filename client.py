import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.56.102', 8080))

print("Welcome!")
temperature_in_fahrenheit = input("Enter the temperature in Fahrenheit: ")
client_socket.send(temperature_in_fahrenheit.encode())
temperature_in_celsius = client_socket.recv(1024)
temperature_in_celsius = float(temperature_in_celsius.decode())
print("The temperature in Celsius is:", temperature_in_celsius)

client_socket.close()