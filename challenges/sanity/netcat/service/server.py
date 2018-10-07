import socket
import threading

def send(conn):
    conn.sendall("GCTF{th3r3_ar3_m4ny_w4y5_t0_c0nn3c7_t0_4_serv1c3}".encode())
    conn.close()

if __name__ == '__main__':
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serversocket.bind(('', 5000))
        serversocket.listen(5)
        while 1:
            connection, address = serversocket.accept()
            threading.Thread(target=send, args=(connection,)).start()
    except KeyboardInterrupt:
        print("Shutting down server...")
    except socket.error:
        print("Socket error encountered...")
    except Exception:
        print("Unexcepted error encountered...")
    finally:
        serversocket.close()
