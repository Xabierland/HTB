# Devvortex - Easy

IP = 10.10.11.242

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