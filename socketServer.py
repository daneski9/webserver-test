#Dane Coleman
#Using local host to create a web server, and a socket to handle the clients requests.
#import socket module
from socket import *
serverPort = 443
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #extract address of client and put into addr, assigns connection socket the request
    try:
        message = connectionSocket.recv(1024)
        print (message)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read()
        print (outputdata)
        responseMsg = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(responseMsg.encode()) #Send one HTTP header line into socket
        for i in range(0, len(outputdata)): #Send the content of the requested file to the client
           connectionSocket.send(outputdata[i].encode())
           
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        print(filename, "Was successfully delivered")
    except IOError:
        responseMsg = "HTTP/1.1 404 Not Found\r\n\r\n"
        errorMsgHtml = "404 Not Found"
        connectionSocket.send(responseMsg.encode())
        connectionSocket.send(errorMsgHtml.encode())
        connectionSocket.close()
        serverSocket.close()
