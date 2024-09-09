import socket
import pickle

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(hostname, ',', IPAddr)

with open('secret.pickle', 'wb') as writer:
    pickle.dump(IPAddr, writer)
