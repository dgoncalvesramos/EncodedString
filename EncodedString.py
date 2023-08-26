import socket
import base64
import sys 
import re

#Extrait la chaine de caractère encodée à l'aide d'une regex puis renvoie sa valeur décodée

def extract_encoded_string(texte):
	match = re.search("my string is '([^']+)'", texte)
	if match:
		encoded_string = match.group(1)
		decoded_bytes = base64.b64decode(encoded_string)
		decoded_string = decoded_bytes.decode('utf-8')  # convertir les bytes en string
	else:
		sys.exit("First number wasn't found !")
	return decoded_string
	
	
# Paramètres
HOST = 'challenge01.root-me.org'  # Hostname
PORT = 52023        			  # Port du serveur

# Créer le socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Reception de la réponse
response = s.recv(1000).decode()
print(response)

decoded_string = extract_encoded_string(response)

#Envoie du message
message = decoded_string + '\n'
s.send(message.encode())

#Réception du flag
response = s.recv(1000).decode()
print(response)
