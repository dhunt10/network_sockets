from socket import AF_INET, SOCK_STREAM, socket

if __name__ == '__main__':
    HOST = input('Enter a host')
    PORT = input('Enter a Port')
    CONNECTION = (HOST, int(PORT))

    client_connect = socket(AF_INET, SOCK_STREAM)
    client_connect.connect(CONNECTION)

    HELLO_MESSAGE = "ece2540 HELLO 001691344"
    client_connect.send(HELLO_MESSAGE.encode())

    while True:
        server_resp = client_connect.recv(2048).decode("utf8");
        results = server_resp.split()

        try:
            CLASS = results[0]
            STATUS = results[1]
            FIRST_NUMBER = results[2]
            OP = results[3]
            SECOND_NUMBER = results[4]
            if OP == '-':
                NUMBER_MESSAGE = int(FIRST_NUMBER) - int(SECOND_NUMBER)
            elif OP == '+':
                NUMBER_MESSAGE = int(FIRST_NUMBER) + int(SECOND_NUMBER)
            elif OP == '/':
                NUMBER_MESSAGE = int(FIRST_NUMBER) / int(SECOND_NUMBER)
            else:
                NUMBER_MESSAGE = int(FIRST_NUMBER) * int(SECOND_NUMBER)

            client_connect.send(NUMBER_MESSAGE.encode())

        except IndexError:
            CLASS = results[0]
            STATUS = results[1]
            SECRET_FLAG = results[2]
            client_connect.close()
            break;

    print(SECRET_FLAG)
