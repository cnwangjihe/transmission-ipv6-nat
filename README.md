### A Not Elegant Solution for Transmission IPv6 NAT
This patch is for [Transmission 3.00](https://github.com/transmission/transmission/tree/3.00), and adds support for IPv6 NAT.  
I write this patch because I use Transmission in docker with bridge, which will get a NAT IPv6 from the interface. In such a situation, Transmission will refuse to work with IPv6, including not sending IPv6 to the tracker, and disabling IPv6 extension in DHT.  

Network:  

`PUBLIC_ADDR:PUBLIC_PORT -> DOCKER_ULA:LOCAL_PORT`

This solution is very violent as the title says, we need a machine with a static IPv6 address running an IP-echo server, others can connect to it and get their public IP.  
You need to change `2001::1234` and `12345` in ipv6-nat.patch to your server's IP and port.  
And this patch force transmission to use the public address instead of the interface address, and bind to "::".  
We also require `PUBLIC_PORT` == `LOCAL_PORT`, so that we will announce the correct ip:port to the tracker.  
