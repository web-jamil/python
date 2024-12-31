Networking commands in Unix-like systems (such as Linux and macOS) are essential for managing network configurations, monitoring network status, and troubleshooting network issues. These commands allow system administrators and users to inspect network interfaces, test connectivity, and manage various network services.

### **1. Common Networking Commands**

Here’s a detailed overview of some of the most common networking commands used in Linux and Unix systems:

---

### **2. `ifconfig` (Interface Configuration)**

The `ifconfig` command is used to configure and display information about network interfaces on a machine. It is considered deprecated on many newer systems, where `ip` (from the `iproute2` package) is preferred, but `ifconfig` is still widely used.

#### **Usage**:

```bash
ifconfig
```

This will display the network configuration of all active network interfaces, including IP addresses, netmasks, and MAC addresses.

- **Show specific interface**:

  ```bash
  ifconfig eth0
  ```

  Shows information about the interface `eth0`.

- **Bring an interface up**:

  ```bash
  sudo ifconfig eth0 up
  ```

- **Bring an interface down**:

  ```bash
  sudo ifconfig eth0 down
  ```

- **Assign an IP address to an interface**:
  ```bash
  sudo ifconfig eth0 192.168.1.100
  ```

---

### **3. `ip` (New Networking Command)**

The `ip` command is part of the `iproute2` package and is the modern alternative to `ifconfig`. It provides more detailed and versatile network management capabilities.

#### **Usage**:

```bash
ip addr show
```

Displays IP address information for all interfaces.

- **Show all network interfaces**:

  ```bash
  ip link show
  ```

- **Assign IP address to an interface**:

  ```bash
  sudo ip addr add 192.168.1.100/24 dev eth0
  ```

- **Bring an interface up**:

  ```bash
  sudo ip link set eth0 up
  ```

- **Bring an interface down**:

  ```bash
  sudo ip link set eth0 down
  ```

- **Delete an IP address**:
  ```bash
  sudo ip addr del 192.168.1.100/24 dev eth0
  ```

---

### **4. `ping` (Packet Internet Groper)**

`ping` is one of the most commonly used commands to test network connectivity between two devices. It sends ICMP Echo Request packets to a target host and waits for a response.

#### **Usage**:

```bash
ping google.com
```

Pings `google.com` to check network connectivity.

- **Ping a specific IP address**:

  ```bash
  ping 192.168.1.1
  ```

- **Send a specific number of pings**:

  ```bash
  ping -c 5 google.com
  ```

- **Change packet size**:

  ```bash
  ping -s 100 google.com
  ```

- **Flood ping** (used for testing network throughput):
  ```bash
  ping -f google.com
  ```

---

### **5. `traceroute`**

`traceroute` is used to trace the path that packets take to reach a destination. It shows the intermediate hops along the network path.

#### **Usage**:

```bash
traceroute google.com
```

- **Specify a maximum number of hops**:

  ```bash
  traceroute -m 10 google.com
  ```

- **Change packet size**:

  ```bash
  traceroute -s 100 google.com
  ```

- **Use a specific port**:
  ```bash
  traceroute -p 80 google.com
  ```

---

### **6. `netstat` (Network Statistics)**

`netstat` is a tool for displaying network connections, routing tables, interface statistics, and more. It is useful for monitoring active network connections and network interface statuses.

#### **Usage**:

```bash
netstat
```

- **Show active connections**:

  ```bash
  netstat -tuln
  ```

  Displays active TCP (`t`) and UDP (`u`) listening ports (`l`), and shows numeric addresses (`n`).

- **Show routing table**:

  ```bash
  netstat -r
  ```

- **Show interface statistics**:
  ```bash
  netstat -i
  ```

---

### **7. `ss` (Socket Stat)**

`ss` is a utility for investigating sockets. It is a faster, more modern alternative to `netstat`.

#### **Usage**:

```bash
ss
```

- **Show listening ports**:

  ```bash
  ss -tuln
  ```

- **Show established connections**:

  ```bash
  ss -t
  ```

- **Show connections for a specific process**:

  ```bash
  ss -p
  ```

- **Display detailed socket stats**:
  ```bash
  ss -s
  ```

---

### **8. `nslookup` (Name Server Lookup)**

`nslookup` is used to query DNS (Domain Name System) to obtain domain name or IP address information.

#### **Usage**:

```bash
nslookup google.com
```

Resolves the domain `google.com` to its associated IP address.

- **Query a specific DNS server**:

  ```bash
  nslookup google.com 8.8.8.8
  ```

- **Find the reverse IP address for a domain**:
  ```bash
  nslookup 8.8.8.8
  ```

---

### **9. `dig` (Domain Information Groper)**

`dig` is a powerful tool for querying DNS information. It is often preferred over `nslookup` due to its detailed output and flexibility.

#### **Usage**:

```bash
dig google.com
```

- **Query a specific record type (e.g., MX for mail)**:

  ```bash
  dig google.com MX
  ```

- **Show all DNS records**:

  ```bash
  dig google.com ANY
  ```

- **Query using a specific DNS server**:
  ```bash
  dig @8.8.8.8 google.com
  ```

---

### **10. `route` (Routing Table)**

`route` is used to display or modify the IP routing table.

#### **Usage**:

```bash
route
```

- **Display the current routing table**:

  ```bash
  route -n
  ```

- **Add a route to the routing table**:

  ```bash
  sudo route add -net 192.168.1.0/24 gw 192.168.1.1
  ```

- **Delete a route**:
  ```bash
  sudo route del -net 192.168.1.0/24
  ```

---

### **11. `hostname` (Set or Show System's Hostname)**

The `hostname` command is used to show or set the system's hostname, which is the name that identifies the computer on a network.

#### **Usage**:

```bash
hostname
```

- **Show the system's current hostname**:

  ```bash
  hostname
  ```

- **Set the system's hostname**:

  ```bash
  sudo hostname newhostname
  ```

- **Show the fully qualified domain name (FQDN)**:
  ```bash
  hostname -f
  ```

---

### **12. `curl` (Client URL)**

`curl` is a versatile tool used to transfer data to or from a server using various protocols like HTTP, HTTPS, FTP, and more.

#### **Usage**:

```bash
curl http://example.com
```

- **Download a file**:

  ```bash
  curl -O http://example.com/file.zip
  ```

- **Send a POST request**:

  ```bash
  curl -X POST -d "name=John&age=30" http://example.com/api
  ```

- **Display response headers**:
  ```bash
  curl -I http://example.com
  ```

---

### **13. `scp` (Secure Copy Protocol)**

`scp` is used to securely transfer files between local and remote hosts over SSH.

#### **Usage**:

```bash
scp file.txt user@remotehost:/path/to/destination
```

- **Copy a file to a remote server**:

  ```bash
  scp file.txt user@192.168.1.100:/home/user/
  ```

- **Copy a file from a remote server**:
  ```bash
  scp user@192.168.1.100:/home/user/file.txt /local/path/
  ```

---

### **14. `netcat` (nc)**

`netcat` (often abbreviated as `nc`) is a networking tool used for reading from and writing to network connections using the TCP/IP protocol. It is often referred to as the "Swiss army knife" of networking.

#### **Usage**:

```bash
nc -zv 192.168.1.1 1-1024
```

Checks which ports between 1 and 1024 are open on the remote host `192.168.1.1`.

- **Start a listening server**:

  ```bash
  nc -l 12345
  ```

- **Connect to a remote server**:
  ```bash
  nc 192.168.1.1 12345
  ```

---

### **Conclusion**

Networking commands are essential for network administration, configuration, and troubleshooting. Understanding how to use tools like `ping`, `traceroute`, `netstat`, `ip`, `ss`, and `nslookup` can help diagnose connectivity issues, monitor network traffic, and manage network interfaces. For deeper network management, commands like `curl`, `scp`, and `netcat` provide essential functionality for data transfer and remote communication.

Networking commands in Unix-like operating systems (Linux, macOS, etc.) are essential for managing network configurations, troubleshooting, and monitoring network activity. These commands allow users to interact with the network interface, monitor connections, test communication between machines, and configure network settings.

Here’s a comprehensive guide to some of the most common networking commands and their usage:

---

### **1. `ifconfig` (Interface Configuration)**

The `ifconfig` command is used to configure or display network interface settings on a system. It can show information about active network interfaces, IP addresses, and more.

#### **Usage**:

- **Show all active interfaces**:
  ```bash
  ifconfig
  ```
- **Show information about a specific interface**:
  ```bash
  ifconfig eth0
  ```
- **Assign an IP address to an interface**:
  ```bash
  sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0 up
  ```
- **Bring down an interface**:
  ```bash
  sudo ifconfig eth0 down
  ```

Note: `ifconfig` is deprecated in favor of `ip` command in modern Linux distributions.

---

### **2. `ip` (IP Routing and Network Interface Management)**

The `ip` command is a more modern replacement for `ifconfig` and is used to configure network interfaces, manage routing, and show network information.

#### **Usage**:

- **Show all network interfaces**:
  ```bash
  ip addr
  ```
- **Show information about a specific interface**:
  ```bash
  ip addr show eth0
  ```
- **Assign an IP address to an interface**:
  ```bash
  sudo ip addr add 192.168.1.10/24 dev eth0
  ```
- **Bring up an interface**:
  ```bash
  sudo ip link set eth0 up
  ```
- **Add a default gateway**:
  ```bash
  sudo ip route add default via 192.168.1.1
  ```
- **Delete an IP address from an interface**:
  ```bash
  sudo ip addr del 192.168.1.10/24 dev eth0
  ```

---

### **3. `ping` (Test Connectivity)**

The `ping` command is used to test the network connectivity between the local machine and a remote host. It sends ICMP echo request packets to a specified IP address and waits for a response.

#### **Usage**:

- **Ping a host (e.g., google.com)**:
  ```bash
  ping google.com
  ```
- **Ping a specific IP address**:
  ```bash
  ping 192.168.1.1
  ```
- **Set the number of packets to send**:
  ```bash
  ping -c 5 google.com
  ```
- **Ping a host with a specific packet size**:
  ```bash
  ping -s 1000 google.com
  ```

---

### **4. `netstat` (Network Statistics)**

The `netstat` command shows network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

#### **Usage**:

- **Display all active connections**:
  ```bash
  netstat -a
  ```
- **Display routing table**:
  ```bash
  netstat -r
  ```
- **Display network statistics**:
  ```bash
  netstat -i
  ```
- **Show listening ports**:
  ```bash
  netstat -l
  ```
- **Show network connections with associated program names**:
  ```bash
  netstat -tulnp
  ```

Note: `netstat` is being replaced by `ss` in many modern Linux distributions.

---

### **5. `ss` (Socket Statistics)**

The `ss` command is used to investigate sockets, including active connections and listening ports. It is a modern alternative to `netstat`.

#### **Usage**:

- **Display all active connections**:
  ```bash
  ss -a
  ```
- **Show listening ports**:
  ```bash
  ss -tuln
  ```
- **Show detailed information about a specific port (e.g., port 80)**:
  ```bash
  ss -tuln | grep ':80'
  ```

---

### **6. `traceroute` (Trace Network Path)**

The `traceroute` command traces the path that packets take from the source machine to a destination host, showing each router (hop) along the way.

#### **Usage**:

- **Trace the path to a domain (e.g., google.com)**:
  ```bash
  traceroute google.com
  ```
- **Set the maximum number of hops**:
  ```bash
  traceroute -m 10 google.com
  ```
- **Specify the packet size**:
  ```bash
  traceroute -s 56 google.com
  ```

---

### **7. `dig` (DNS Lookup)**

The `dig` command is a DNS lookup tool that allows you to query DNS servers for information about a domain (such as IP address, mail servers, etc.).

#### **Usage**:

- **Get the A record (IPv4 address) of a domain**:
  ```bash
  dig google.com
  ```
- **Get a specific DNS record type (e.g., MX for mail servers)**:
  ```bash
  dig google.com MX
  ```
- **Query a specific DNS server**:
  ```bash
  dig @8.8.8.8 google.com
  ```

---

### **8. `nslookup` (DNS Query)**

`nslookup` is another DNS query tool that allows you to query DNS servers for domain information, similar to `dig`.

#### **Usage**:

- **Query the DNS for a domain**:
  ```bash
  nslookup google.com
  ```
- **Set a specific DNS server for the query**:
  ```bash
  nslookup google.com 8.8.8.8
  ```
- **Query a specific type of DNS record**:
  ```bash
  nslookup -type=MX google.com
  ```

---

### **9. `route` (Routing Table Management)**

The `route` command is used to view or modify the IP routing table.

#### **Usage**:

- **Display the routing table**:
  ```bash
  route -n
  ```
- **Add a new route**:
  ```bash
  sudo route add -net 192.168.1.0/24 gw 192.168.1.1
  ```
- **Delete a route**:
  ```bash
  sudo route del -net 192.168.1.0/24
  ```

---

### **10. `hostname` (Show or Set Hostname)**

The `hostname` command is used to show or set the system's hostname (the name of the machine on the network).

#### **Usage**:

- **Display the current hostname**:
  ```bash
  hostname
  ```
- **Set a new hostname**:
  ```bash
  sudo hostname newhostname
  ```

---

### **11. `curl` (Transfer Data from a URL)**

The `curl` command is used to interact with URLs and transfer data (e.g., downloading files, making HTTP requests, etc.).

#### **Usage**:

- **Download a file**:
  ```bash
  curl -O https://example.com/file.zip
  ```
- **Make an HTTP request**:
  ```bash
  curl http://google.com
  ```
- **Show the response headers of a request**:
  ```bash
  curl -I http://google.com
  ```

---

### **12. `wget` (Non-Interactive Download Tool)**

`wget` is another utility for downloading files from the internet, particularly useful for non-interactive downloads.

#### **Usage**:

- **Download a file**:
  ```bash
  wget https://example.com/file.zip
  ```
- **Download a file in the background**:
  ```bash
  wget -b https://example.com/file.zip
  ```

---

### **13. `iptables` (Firewall Configuration)**

The `iptables` command is used for configuring the system's firewall, controlling inbound and outbound network traffic.

#### **Usage**:

- **View current rules**:
  ```bash
  sudo iptables -L
  ```
- **Allow incoming traffic on a specific port (e.g., port 80)**:
  ```bash
  sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
  ```
- **Block incoming traffic from a specific IP**:
  ```bash
  sudo iptables -A INPUT -s 192.168.1.100 -j DROP
  ```

---

### **14. `nmcli` (NetworkManager Command-Line Interface)**

The `nmcli` command is a command-line client for NetworkManager, allowing you to manage network connections, interfaces, and settings.

#### **Usage**:

- **Show the status of all network devices**:
  ```bash
  nmcli device status
  ```
- **Connect to a Wi-Fi network**:
  ```bash
  nmcli device wifi connect "SSID" password "password"
  ```

---

### **Conclusion**

Networking commands are vital for managing and troubleshooting network interfaces, monitoring network traffic, and ensuring proper communication between machines. Commands like `ifconfig`, `ip`, `ping`, `netstat`, `ss`, `traceroute`, `curl`, and others are commonly used by network administrators and developers for everyday tasks related to network configuration and monitoring. Understanding these commands will help you diagnose network issues, configure devices, and optimize performance in your network environment.

Networking commands are essential for managing and troubleshooting network connectivity on Unix-like systems (like Linux and macOS). They allow users to configure network interfaces, check network status, troubleshoot connectivity issues, and test network connections.

Here’s a comprehensive guide to common **networking commands**:

---

### **1. Basic Networking Commands**

#### **1.1 `ifconfig` (Interface Configuration)**

The `ifconfig` command is used to configure and display network interfaces in Unix-like systems. Although it is being replaced by `ip` in some distributions, it is still widely used.

- **View current network interfaces and their configurations**:

  ```bash
  ifconfig
  ```

- **Display specific interface details**:

  ```bash
  ifconfig eth0
  ```

- **Enable an interface**:

  ```bash
  sudo ifconfig eth0 up
  ```

- **Disable an interface**:

  ```bash
  sudo ifconfig eth0 down
  ```

- **Assign an IP address to an interface**:
  ```bash
  sudo ifconfig eth0 192.168.1.100
  ```

---

#### **1.2 `ip` (Network Configuration)**

The `ip` command is more modern and powerful, gradually replacing `ifconfig` for configuring network interfaces, routing, and managing network namespaces.

- **Show all network interfaces**:

  ```bash
  ip addr
  ```

- **Display IP addresses assigned to interfaces**:

  ```bash
  ip addr show
  ```

- **Bring an interface up**:

  ```bash
  sudo ip link set eth0 up
  ```

- **Bring an interface down**:

  ```bash
  sudo ip link set eth0 down
  ```

- **Assign an IP address to an interface**:

  ```bash
  sudo ip addr add 192.168.1.100/24 dev eth0
  ```

- **Show routing table**:

  ```bash
  ip route show
  ```

- **Delete an IP address**:
  ```bash
  sudo ip addr del 192.168.1.100/24 dev eth0
  ```

---

#### **1.3 `ping` (Test Network Connectivity)**

The `ping` command is used to test network connectivity between two hosts by sending ICMP Echo Request packets and waiting for an Echo Reply.

- **Ping an IP address**:

  ```bash
  ping 192.168.1.1
  ```

- **Ping a domain name**:

  ```bash
  ping www.google.com
  ```

- **Ping with a specific number of packets**:

  ```bash
  ping -c 4 192.168.1.1
  ```

- **Ping with a specific interval**:
  ```bash
  ping -i 2 192.168.1.1
  ```

---

#### **1.4 `traceroute` (Trace Route)**

The `traceroute` command shows the route packets take to reach a network host. It displays each hop along the path, helping identify where the network delays or failures occur.

- **Basic traceroute**:

  ```bash
  traceroute www.google.com
  ```

- **Use a specific number of queries per hop**:

  ```bash
  traceroute -q 5 www.google.com
  ```

- **Traceroute with a maximum number of hops**:
  ```bash
  traceroute -m 15 www.google.com
  ```

---

#### **1.5 `netstat` (Network Statistics)**

The `netstat` command provides various network-related information, such as active connections, listening ports, routing tables, and more. It's often used for troubleshooting and monitoring network activity.

- **Display all active network connections**:

  ```bash
  netstat -a
  ```

- **Show listening ports**:

  ```bash
  netstat -l
  ```

- **Display active connections with process IDs**:

  ```bash
  netstat -tulnp
  ```

- **Show routing table**:

  ```bash
  netstat -r
  ```

- **Show network statistics**:
  ```bash
  netstat -s
  ```

---

#### **1.6 `ss` (Socket Statictics)**

The `ss` command is an alternative to `netstat` for displaying network socket statistics. It is faster and more powerful than `netstat`.

- **Display all open sockets**:

  ```bash
  ss -a
  ```

- **Show TCP sockets**:

  ```bash
  ss -t
  ```

- **Show UDP sockets**:

  ```bash
  ss -u
  ```

- **Display socket information for a specific process**:
  ```bash
  ss -p
  ```

---

#### **1.7 `route` (Routing Table)**

The `route` command is used to view and manipulate the IP routing table.

- **Display the routing table**:

  ```bash
  route -n
  ```

- **Add a route**:

  ```bash
  sudo route add -net 192.168.1.0/24 gw 192.168.1.1
  ```

- **Delete a route**:
  ```bash
  sudo route del -net 192.168.1.0/24
  ```

---

### **2. Network Interface and Configuration Management**

#### **2.1 `hostname` (System Hostname)**

The `hostname` command is used to display or set the system's hostname, which is the name assigned to the machine in a network.

- **Display the current hostname**:

  ```bash
  hostname
  ```

- **Set the hostname**:

  ```bash
  sudo hostname newhostname
  ```

- **Set the fully qualified domain name (FQDN)**:
  ```bash
  sudo hostnamectl set-hostname newhostname.domain.com
  ```

---

#### **2.2 `nmcli` (NetworkManager CLI)**

`nmcli` is the command-line interface for NetworkManager, a tool that manages network connections in Linux. It allows users to configure, enable, disable, and monitor network connections.

- **Display network status**:

  ```bash
  nmcli device status
  ```

- **Connect to a Wi-Fi network**:

  ```bash
  nmcli dev wifi connect SSID password 'your_password'
  ```

- **Show available Wi-Fi networks**:

  ```bash
  nmcli dev wifi list
  ```

- **Disable a network interface**:
  ```bash
  nmcli device disconnect eth0
  ```

---

### **3. DNS Commands**

#### **3.1 `dig` (Domain Information Groper)**

`dig` is a DNS lookup tool for querying DNS servers to retrieve DNS records.

- **Basic DNS lookup**:

  ```bash
  dig example.com
  ```

- **Query a specific DNS record (e.g., A, MX, TXT)**:

  ```bash
  dig example.com A
  dig example.com MX
  dig example.com TXT
  ```

- **Perform a reverse DNS lookup**:
  ```bash
  dig -x 8.8.8.8
  ```

---

#### **3.2 `nslookup` (Name Server Lookup)**

`nslookup` is another DNS querying tool, similar to `dig`.

- **Query DNS for a domain**:

  ```bash
  nslookup example.com
  ```

- **Set the DNS server to query**:
  ```bash
  nslookup example.com 8.8.8.8
  ```

---

### **4. Network Troubleshooting Commands**

#### **4.1 `mtr` (My Traceroute)**

`mtr` is a network diagnostic tool combining the functionality of `ping` and `traceroute` to give an overview of network performance and identify packet loss or delays.

- **Basic mtr command**:

  ```bash
  mtr example.com
  ```

- **Display results in report mode**:
  ```bash
  mtr --report example.com
  ```

---

#### **4.2 `tcpdump` (Network Packet Analyzer)**

`tcpdump` is a command-line packet analyzer used to capture and display network traffic.

- **Capture all packets on a network interface**:

  ```bash
  sudo tcpdump -i eth0
  ```

- **Capture packets and save them to a file**:

  ```bash
  sudo tcpdump -i eth0 -w capture.pcap
  ```

- **Capture only packets from a specific host**:
  ```bash
  sudo tcpdump -i eth0 host 192.168.1.1
  ```

---

#### **4.3 `nmap` (Network Mapper)**

`nmap` is a powerful network scanning tool used for discovering hosts and services on a computer network.

- **Scan a single host**:

  ```bash
  nmap 192.168.1.1
  ```

- **Scan a range of IPs**:

  ```bash
  nmap 192.168.1.1-100
  ```

- **Scan a specific port**:

  ```bash
  nmap -p 80 192.168.1.1
  ```

- **Perform a service version detection scan**:
  ```bash
  nmap -sV 192.168.1.1
  ```

---

### **5. File Transfer Commands**

#### **5.1 `scp` (Secure Copy Protocol)**

`scp` is used to securely transfer files between computers over SSH.

- **Copy a file to a remote host**:

  ```bash
  scp file.txt user@remotehost:/path/to/destination
  ```

- **Copy a file from a remote host**:

  ```bash
  scp user@remotehost:/path/to/file.txt /local/destination
  ```

- **Copy a directory recursively**:
  ```bash
  scp -r dir user@remotehost:/path/to/destination
  ```

---

#### **5.2 `rsync` (Remote Sync)**

`rsync` is a command-line utility for syncing files and directories locally or remotely over SSH.

- **Sync files from local to remote**:

  ```bash
  rsync -av file.txt user@remotehost:/path/to/destination
  ```

- **Sync files from remote to local**:
  ```bash
  rsync -av user@remotehost:/path/to/file.txt /local/destination
  ```

---

### **Conclusion**

Networking commands provide essential tools for configuring, managing, and troubleshooting network connections. Commands like `ping`, `traceroute`, `ip`, `netstat`, and `tcpdump` help users monitor network health, identify issues, and manage networking configurations efficiently. Advanced tools like `nmap`, `scp`, and `rsync` enhance network exploration and file transfer capabilities.

Networking commands in Unix-like systems (Linux, macOS, etc.) are essential tools for managing and troubleshooting network connections. These commands allow you to monitor network interfaces, configure network settings, test connectivity, and debug network issues.

Here is a comprehensive overview of common **networking commands**:

---

### **1. `ifconfig` (Interface Configuration)**

The `ifconfig` command is used to configure and display network interface parameters. It is commonly used to view and manage network interfaces like Ethernet and Wi-Fi.

#### **Common Usage**:

- **Display all network interfaces**:
  ```bash
  ifconfig
  ```
- **Display a specific interface (e.g., eth0)**:
  ```bash
  ifconfig eth0
  ```
- **Enable a network interface**:
  ```bash
  sudo ifconfig eth0 up
  ```
- **Disable a network interface**:
  ```bash
  sudo ifconfig eth0 down
  ```
- **Assign an IP address to an interface**:
  ```bash
  sudo ifconfig eth0 192.168.1.100
  ```

> **Note**: `ifconfig` is deprecated in some distributions and replaced by `ip`.

---

### **2. `ip` Command (IP Route, Link, Address)**

The `ip` command is a more modern and versatile tool used for managing network interfaces, IP addresses, routes, and other networking features.

#### **Common Usage**:

- **Display all network interfaces**:
  ```bash
  ip a
  ```
- **Show routing table**:
  ```bash
  ip route
  ```
- **Bring an interface up**:
  ```bash
  sudo ip link set eth0 up
  ```
- **Bring an interface down**:
  ```bash
  sudo ip link set eth0 down
  ```
- **Assign an IP address to an interface**:
  ```bash
  sudo ip addr add 192.168.1.100/24 dev eth0
  ```
- **Delete an IP address**:
  ```bash
  sudo ip addr del 192.168.1.100/24 dev eth0
  ```

---

### **3. `ping`**

The `ping` command is used to test the connectivity between two devices over a network. It sends Internet Control Message Protocol (ICMP) echo requests to the target machine and listens for replies.

#### **Common Usage**:

- **Ping a specific IP address or hostname**:
  ```bash
  ping 8.8.8.8
  ping google.com
  ```
- **Set the number of packets to send**:
  ```bash
  ping -c 4 google.com
  ```
- **Set packet size**:
  ```bash
  ping -s 1024 google.com
  ```
- **Set interval between requests**:
  ```bash
  ping -i 2 google.com
  ```

---

### **4. `traceroute`**

The `traceroute` command is used to trace the route that packets take to reach a destination IP address or hostname. It helps identify the path and any issues along the route.

#### **Common Usage**:

- **Traceroute to a destination**:
  ```bash
  traceroute google.com
  ```
- **Use a different port**:
  ```bash
  traceroute -p 80 google.com
  ```

> **Note**: On some systems, `traceroute` might be replaced by `tracepath` or `mtr`.

---

### **5. `netstat` (Network Statistics)**

The `netstat` command is used to display active network connections, routing tables, interface statistics, and other network-related information.

#### **Common Usage**:

- **Display all active network connections**:
  ```bash
  netstat
  ```
- **Display all active TCP connections**:
  ```bash
  netstat -t
  ```
- **Display all listening ports**:
  ```bash
  netstat -l
  ```
- **Display routing table**:
  ```bash
  netstat -r
  ```
- **Display network interface statistics**:
  ```bash
  netstat -i
  ```

> **Note**: `netstat` is deprecated on some systems and replaced by `ss`.

---

### **6. `ss` (Socket Stat)**

The `ss` command is used to display socket statistics and is considered a faster and more modern replacement for `netstat`.

#### **Common Usage**:

- **Display all active connections**:
  ```bash
  ss
  ```
- **Display all active TCP connections**:
  ```bash
  ss -t
  ```
- **Display all listening ports**:
  ```bash
  ss -l
  ```
- **Display detailed information about TCP connections**:
  ```bash
  ss -t -a
  ```

---

### **7. `route`**

The `route` command is used to view and manipulate the IP routing table.

#### **Common Usage**:

- **Display the routing table**:
  ```bash
  route
  ```
- **Add a new route**:
  ```bash
  sudo route add default gw 192.168.1.1
  ```
- **Delete a route**:
  ```bash
  sudo route del default gw 192.168.1.1
  ```

> **Note**: On some systems, `route` has been replaced by `ip route`.

---

### **8. `hostname`**

The `hostname` command is used to display or set the system’s hostname (the name of the computer on the network).

#### **Common Usage**:

- **Display the current hostname**:
  ```bash
  hostname
  ```
- **Set a new hostname**:
  ```bash
  sudo hostname newhostname
  ```

---

### **9. `nslookup` (Name Server Lookup)**

The `nslookup` command is used to query Domain Name System (DNS) records, including the mapping of domain names to IP addresses.

#### **Common Usage**:

- **Lookup an IP address for a domain**:
  ```bash
  nslookup google.com
  ```
- **Lookup a specific DNS record (e.g., MX)**:
  ```bash
  nslookup -query=MX google.com
  ```

---

### **10. `dig` (Domain Information Groper)**

`dig` is another powerful DNS lookup tool, providing more detailed information than `nslookup`. It can be used to query DNS records and troubleshoot DNS-related issues.

#### **Common Usage**:

- **Lookup an IP address for a domain**:
  ```bash
  dig google.com
  ```
- **Query a specific DNS record type (e.g., A, MX)**:
  ```bash
  dig google.com A
  dig google.com MX
  ```

---

### **11. `wget`**

The `wget` command is used to download files from the web over HTTP, HTTPS, and FTP protocols.

#### **Common Usage**:

- **Download a file**:
  ```bash
  wget http://example.com/file.tar.gz
  ```
- **Download a file in the background**:
  ```bash
  wget -b http://example.com/file.tar.gz
  ```
- **Download a file and save it with a different name**:
  ```bash
  wget -O newname.tar.gz http://example.com/file.tar.gz
  ```

---

### **12. `curl`**

The `curl` command is used to transfer data to or from a server using various protocols (HTTP, FTP, etc.).

#### **Common Usage**:

- **Fetch a web page**:
  ```bash
  curl http://example.com
  ```
- **Download a file**:
  ```bash
  curl -O http://example.com/file.tar.gz
  ```
- **Send data via POST request**:
  ```bash
  curl -X POST -d "name=John&age=30" http://example.com/submit
  ```

---

### **13. `ip addr` (Show IP Address)**

The `ip addr` command shows IP addresses assigned to network interfaces.

#### **Common Usage**:

- **Display all IP addresses**:
  ```bash
  ip addr
  ```
- **Display IP address for a specific interface**:
  ```bash
  ip addr show eth0
  ```

---

### **14. `arp` (Address Resolution Protocol)**

The `arp` command is used to view and manipulate the ARP cache, which stores the mappings of IP addresses to MAC addresses.

#### **Common Usage**:

- **Display ARP cache**:
  ```bash
  arp -a
  ```
- **Add a static ARP entry**:
  ```bash
  sudo arp -s 192.168.1.1 00:11:22:33:44:55
  ```

---

### **15. `ufw` (Uncomplicated Firewall)**

The `ufw` command is used to manage a firewall on Linux-based systems, typically with a focus on ease of use.

#### **Common Usage**:

- **Enable the firewall**:
  ```bash
  sudo ufw enable
  ```
- **Allow traffic on a specific port**:
  ```bash
  sudo ufw allow 80
  ```
- **Check the firewall status**:
  ```bash
  sudo ufw status
  ```

---

### **16. `tcpdump`**

The `tcpdump` command is a network packet analyzer. It allows users to capture and display the data traveling through the network.

#### **Common Usage**:

- **Capture packets on a specific interface**:
  ```bash
  sudo tcpdump -i eth0
  ```
- **Capture packets and save to a file**:
  ```bash
  sudo tcpdump -i eth0 -w capture.pcap
  ```

---

### **Conclusion**

These networking commands are essential for managing, troubleshooting, and configuring network connections on a Linux/Unix system. They provide powerful functionality for controlling network interfaces, testing connectivity, monitoring network traffic, and interacting with DNS and routing tables. Mastering these commands will help you maintain and troubleshoot network configurations effectively.
