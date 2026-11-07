# Day 3 – Computer Science: Computer Networks

**Date:** 5 November 2026  
**Week:** 1  
**Topics:** Network basics, Hosts, Packets, Routers and Switches.

---

# 1. What is a Computer Network?

A computer network is a group of computers and devices connected together to communicate and share information.

Examples:

- Computers connected in a college laboratory.
- Mobile phones connected through Wi-Fi.
- Computers communicating over the internet.
- Office computers sharing files and printers.

### Why do we need computer networks?

1. To share files.
2. To share printers and other devices.
3. To communicate with other computers.
4. To access websites and online services.
5. To transfer data between devices.

### Real-world example

In a college computer laboratory, multiple computers are connected through a network. Students can access shared resources and communicate with other systems.

---

# 2. Host

A host is a device connected to a network that can communicate using a network address.

Examples:

- Laptop
- Desktop computer
- Mobile phone
- Server

### Real-world example

When you open YouTube on your laptop, your laptop acts as a host communicating with YouTube's servers.

### Important points

- A host can send and receive data.
- Hosts communicate through network protocols.
- Hosts use network addresses to identify communication endpoints.

---

# 3. Packets

When data travels through a network, it is often divided into smaller units called packets.

For example, when you send a large image:

1. The image data is divided into packets.
2. Packets travel through the network.
3. The receiving device collects the data.
4. The original information is reconstructed.

### What does a packet contain?

A packet generally contains:

- Source information.
- Destination information.
- Data (payload).
- Other control information.

### Real-world example

When you send a WhatsApp message, networking protocols help transfer the data between devices.

### Important points

- Packets make data transmission manageable.
- Packets carry information across networks.
- Network protocols define how data is formatted and transmitted.

---

# 4. Router

A router is a networking device that connects different networks and forwards packets between them using IP addresses.

### Main responsibilities

1. Connect different networks.
2. Forward packets towards their destinations.
3. Select an appropriate route for packets.

### Real-world example

Your home Wi-Fi router connects your local home network to your Internet Service Provider's network.

### Important points

- Routers operate at the network layer (Layer 3) in the OSI model.
- Routers use IP addresses for routing.
- A router forwards packets between networks.

---

# 5. Switch

A switch is a networking device that connects multiple devices within a Local Area Network (LAN).

### Main responsibilities

1. Connect computers and other devices.
2. Forward Ethernet frames to the appropriate destination.
3. Use MAC addresses to identify devices on the local network.

### Real-world example

In a college computer laboratory, multiple computers can connect to one network switch.

### Important points

- A typical Ethernet switch operates at the data link layer (Layer 2).
- It uses MAC addresses to forward Ethernet frames.
- It helps devices communicate within a LAN.

---

# 6. Difference Between Router and Switch

| Router | Switch |
|---|---|
| Connects different networks | Connects devices within a LAN |
| Uses IP addresses for routing | Uses MAC addresses to forward Ethernet frames |
| Forwards packets between networks | Forwards frames within a LAN |
| Typically operates at Layer 3 | A typical Ethernet switch operates at Layer 2 |
| Example: Home Wi-Fi router | Example: College laboratory switch |

---

# 7. How Hosts, Packets, Routers and Switches Work Together

Imagine opening a website from your laptop.

### Step-by-step process

1. Your laptop sends a request to access a website.
2. Networking protocols prepare the data for transmission.
3. Data is carried in packets.
4. Your router forwards the traffic towards the internet.
5. Other network devices forward the packets towards the destination.
6. The website's server receives and processes the request.
7. The response travels back through the network.
8. Your laptop receives and displays the website.

### Example architecture

```text
       YOUR LAPTOP
           |
           |
       WIFI ROUTER
           |
           |
        INTERNET
           |
           |
      WEB SERVER
           |
           |
      WEBSITE DATA
```

A switch may also connect multiple devices within your local network.

---

# 8. Important Networking Terminology

| Term | Meaning |
|---|---|
| Network | Connected devices that communicate |
| Host | A device connected to a network |
| Packet | A formatted unit of data transmitted over a network |
| Router | Connects networks and forwards packets |
| Switch | Connects devices within a LAN |
| IP Address | A logical network address used to identify an interface |
| MAC Address | A link-layer hardware address used in local network communication |
| LAN | Local Area Network |
| WAN | Wide Area Network |
| Protocol | Rules that govern network communication |

---

# 9. Important Interview Questions

### Q1. What is a computer network?

A computer network is a group of connected devices that communicate and share resources.

### Q2. What is a host?

A host is a device connected to a network that can communicate using a network address.

### Q3. What is a packet?

A packet is a formatted unit of data transmitted over a network.

### Q4. What is a router?

A router connects different networks and forwards packets using IP addresses.

### Q5. What is a switch?

A switch connects devices in a LAN and forwards Ethernet frames using MAC addresses.

### Q6. What is the difference between a router and a switch?

A router connects different networks, whereas a switch connects devices within a LAN.

### Q7. What is an IP address?

An IP address is a logical address used to identify a network interface and help route data across networks.

### Q8. What is a MAC address?

A MAC address is a link-layer address used to identify a network interface on a local network.

### Q9. What is LAN?

LAN stands for Local Area Network. It connects devices within a limited geographical area, such as a home, office or college.

### Q10. What is WAN?

WAN stands for Wide Area Network. It connects networks across large geographical areas.

---

# 10. Quick Revision

| Topic | Remember |
|---|---|
| Computer Network | Connected devices communicating with each other |
| Host | Device connected to a network |
| Packet | Unit of transmitted data |
| Router | Connects different networks |
| Switch | Connects devices within a LAN |
| IP Address | Logical network address |
| MAC Address | Link-layer address |
| LAN | Local Area Network |
| WAN | Wide Area Network |

---

# 11. Practice Questions

### Multiple Choice Questions

1. Which device connects different networks?
   - A. Switch
   - B. Router
   - C. Keyboard
   - D. Monitor

2. Which address does a typical Ethernet switch use to forward frames?
   - A. IP address
   - B. MAC address
   - C. Email address
   - D. Website URL

3. What is a packet?
   - A. A physical computer
   - B. A unit of network data
   - C. A programming language
   - D. A storage device

4. What does LAN stand for?
   - A. Large Area Network
   - B. Local Area Network
   - C. Long Access Network
   - D. Logical Area Network

5. Which device commonly connects multiple computers in a college laboratory?
   - A. Switch
   - B. Keyboard
   - C. Printer
   - D. Monitor

### Answers

1. B – Router
2. B – MAC address
3. B – A unit of network data
4. B – Local Area Network
5. A – Switch

---

# 12. Day 3 CS Completion Checklist

- [ ] Understand computer networks.
- [ ] Understand hosts.
- [ ] Understand packets.
- [ ] Understand routers.
- [ ] Understand switches.
- [ ] Understand the difference between routers and switches.
- [ ] Understand IP addresses and MAC addresses.
- [ ] Prepare 2–3 interview questions.
- [ ] Explain network basics aloud in 60 seconds.


