# How to setup your own server

We need a public domain name. Which can be acquired from websites such as godaddy.com , dan, etc.
Now this public domain name needs to link to another DNS service provider, to which your IP would be linked.


## List all devices on the LAN

nmap -sV --allports -T4 192.168.1.0/24



## NGINX

### commands

Verify configurations :

```shell
nginx -T
```

Reload configurations :

```shell
nginx -s reload
```

## Performance considerations

### Edge server

Multi core system for handling high routing requirements.
Attempt to make use of High speed blade servers here if affordable.

This is because it needs to deal with high number of connections and extremely fast rerouting.

So the higher clock speed you have on the processors, the lesser cores you require.
GPUs are of no use, CPUs are required. This is to be used as the gateway server for the internal network.

A formula can be made up here, but tbh, it get's complicated due to the number of parallel services required to maintain a high efficiency system.

For example, in a generic system, you would want the following :

1. A firewall
2. A routing & load balancer service
3. A TTY service

## Security considerations

### Edge Server

Expose only port 80 on the edge server. Control sub domains extremely strictly.
If SSH is required for the edge server, make sure to use whitelisting strategy for it.

Whitelisting in SSH is done for SSHD in /etc/hosts.allow and /etc/hosts.deny

We deny ALL through ```sshd : ALL```.
Whitelisting in allow happens through ```sshd: IP(s)/subnet1```
