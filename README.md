# network_sockets
## Created by Darin Hunt, all credit should be given to him.
#### Not to be used by anyone else
- [x] created
- [x] tested

#### - This file is a client that connects to a server designed for a very specific purpose.
#### - The main function first assigns a port and host address to their respective variables.
#### - A function to connect to the server is first ran and once a connection is established.
#### - A string of the correct format is then sent to the server
#### - Once the initial message has been sent to the server we call a new function.
#### - In the new function a while loop runs and connects continuously receives messages from the server
#### - Once a message is received we extract two numbers and an operator inside of a try except
#### - Depending on the numbers and operator we get we then return a response to the server
#### - We continue to do this until the try except fails (ValueError) in which case we know we have found our BYE message
#### - Finally we extract the secret flag from the bye message and break the while loop and end the program
