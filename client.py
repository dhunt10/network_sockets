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

        print(results)
        try:
            CLASS = results[0]
            STATUS = results[1]
            FIRST_NUMBER = int(results[2])
            OP = results[3]
            SECOND_NUMBER = int(results[4])
            if OP == '-':
                NUMBER_MESSAGE = FIRST_NUMBER - SECOND_NUMBER
            elif OP == '+':
                NUMBER_MESSAGE = FIRST_NUMBER + SECOND_NUMBER
            elif OP == '/':
                NUMBER_MESSAGE = FIRST_NUMBER / SECOND_NUMBER
            else:
                NUMBER_MESSAGE = FIRST_NUMBER * SECOND_NUMBER

            client_connect.send((str(NUMBER_MESSAGE).encode()))

        except ValueError:
            CLASS = results[0]
            STATUS = results[1]
            SECRET_FLAG = results[2]
            client_connect.close()
            break;

    print(SECRET_FLAG)
