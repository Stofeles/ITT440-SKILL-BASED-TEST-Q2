import socket

#convert fahrenheit to celcius function
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

#create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind to host and port
server_socket.bind(('192.168.56.102', 8080))

#listen for connection
server_socket.listen(1)
print("Hello!")
print("Gathering info from client...")

while True:
    #establishing connection
    connection, address = server_socket.accept()
    print("CONNECTED TO CLIENT!")

    temperature_in_fahrenheit = connection.recv(1024).decode()
    temperature_in_fahrenheit = float(temperature_in_fahrenheit)
    temperature_in_celsius = fahrenheit_to_celsius(temperature_in_fahrenheit)
    connection.send(str(temperature_in_celsius).encode())

    connection.close()