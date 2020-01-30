# The Architecture of Computer Hardware, Systems Software, and Networking 

## Chapter 1: Introduction: Computer and Systems 

User: capabilities, strengths, and limitations of computer system. Understanding of commands. 
Programmer: write better programs by using the characteristic of the machine for efficiency. 
System Architect/Analyst: design and implementation of systems that meet an organizations information technology (IT) needs. 
Networking Professional: design, maintenance, suppport, and management of networks connecting computer systems and interfaces. 
Web Services Designer: optimize web system configurations, page design, data formating, and scripting language to optimize customer accessibility to web services. 
System Administrator/Manager: maximize availability and efficiency of a system. 

Protocols: standard agreements for network interfaces and computer pairs to exchange information
Input-Process-Output (IPO):

- Input: Keyboard, Mouse, 
- Process: CPU
- Output: Printer, Display, Storage 

### Components of Computer System

#### Hardware 

Hardware Type:

- Input: Keyboard, Touchscreen, Mouse/Pointing Device
- Output: Display Screen, Printer
- Central Processing Unit (CPU): also known as cores. Performs calculations and other operations.
- Memory/Storage: holds programs and data while processing is taking place. Short term in Random Access Memory (RAM), Long term in SD cards 

Central Processing Unit (CPU): 

- Arithmetic/Logic Unit (ALU): arithmetic and Boolean logical calculations are performed. 
- Control Unit (CU): controls the processing of instructions and the movement of internal CPU data from one part of the CPU to another
- Interface Unit: moves the program instructions and data between the CPU and other hardware components through Input/Output (IO) module and can be used to combine multiple CPU cores together. 

- Bus: bundle of wires that carry signals and bpower between different components. 
- Channels: one or more separate processors (I/O modules) that connect the CPU. 

Random Access Memory (RAM): primary/working storage that holds programs and data for access by the CPU. 

- Primary Storage: large number of cells, each numbered and individual addressable. Each cell holds a binary number representing data value or part of the instruction. Smallest cell size is 8 bits.
- Byte: is 8 bits of memory. 4 bytes of memroy combine to form 32-bit word. Modern computers address memory 4 bytes (32-bit) or 8 bytes (64-bit) at a time. 

Stored Program Concept: John von Neumann. Program instructions and data are both stored in memory while being processed. 

#### Software 

Operating System: system software programs that manage the computer. Windows, Linux, Mac OSX, iOS, Android, Unix, Oracle Solaris, IBM z/OS. Traditionally stored on hard disk. Initial program load (IPL) or bootstrap is sorted in the ROM (read only memory). Provides tools to test the system and load the remainder of the operating system from the network.

- User Interface: allows user to execute programs, enter commands, manipulate files. Accepts input from a keyboard, mouse, touch scren and does output presentation on a display. Output display might be simple text or graphic user interface with a windowing system. 
- Application Programming Interface (API): interface for application programs and utilities to access the internal services provided by the operating system. File services, I/O services, data communication, user interface, program execution. 
- Kernel: module that contains the most important operating system processing functions. Kernel manages memory by locating and allocating space to programs that need it, schedules time for each application to execute, provides communication between programs, manages services and resources, and provides security. 
- File Management System: allocates and manages secondary storage space and translates file requests from their name-based form into specific I/O requests. 
- Network Module: controls interactions between computer system and the network.


Application Programs: programs that you write, that normally run to get work done. 

#### Communication

Communication Channel: provides connection between computers. Wire cable, fibre optic cable, telephone line, wireless technology (infared, cellular phone, radio based tech like Wifi or Bluetooth). 

- Modem or Network Interface Card (NIC) serve as interface between computer and network channel. Establishes connection, controls flow of data, directs the data to propert applications for use. 

#### Computer System

Distributed Computing: the ability to transfer data between different systems to improve processing efficiency. 
Open Computing: different types of computers working, sharing files, and communicating together. 

#### Protocols and Standards 

Standards: agreements among parties (manufacturers) to assure system components will work together interchangeably. Allows computers to be built using parts from different suppliers. Hardware, software, data, and communications. 

Protocols: specific agreed set of ground rules that allow communication between computer units (software and hardware). Protocol specification defines data representation, signaling characteristics, message format, meaning of messages, identification and authentication, and error detection. Protocols are usually standardized. 

TCP/IP: Transmission Control Protocol/Internet Protocol 

SATA: Storage device communication protocol. 

#### John von Neumann

Consultant on the ENIAC (Electronic Numerical Integrator and Computer). In 1945 he proposed improvements to the ENIAC design: 

1. Memory would hold both programs and data (Stored program concept). This would solve the ENIAC problem of having to rewire control panels for changing programs. 
2. Binary processing of data (for both instruction and data). Correlated to the use of the ON/OFF switches in the electronic design. 

von Neumann Architecture: CPU includes ALU, memory, and CU components. Control unit (CU) reads instructions from memory and executes it. Current standard for modern computers. 

#### Operating System

UNIX: started by Ken Thompson and Dennis Richie. Richie developed high-level language, C, to replace the assembly language UNIX was first written in. UNIX introduced hierarchial file system, shell concept, redirection, piping, and command operations. Spell and grammar checkers. UNIX also introduced graphic user interface (GUI). 

- C: language allows easy porting (convert for use by other computers). 

## Chapter 2: Introduction to System COncepts and SYstem Architecture

IT System: groups of computer hardware, various I/O devices, and application and system software, connected together by networks. 

- Allow organizations to process, access, and share information. Documents, information, improved business process and productivity, profits, strategic plans, and the like. 
- IPO: Input-Processing-Output model

System: a collection of components linked together and organized in such a way as to be recognizable as a single unit. 

Environment: anything outside the boundary that the system operates or presents itself within. 

Interface: the relationship between the system and its environment. If the interface is well defined, it is possible to replace the existing system with a different system. 

Subsystems: Components of a system that could be broken down into their own representable systems. 

Decomposition: the division of a system or subsystem into its components and linkages. Inherently hierarchical. 

Architecture: fundamental properties, and patterns of relationships, connections, constraints, and linkages among components and between the system and its environment. 

- Architecture is fundamental to the meaning and value of the system. 
- Organization is one of the possible many combinations of the components and linkages that meets the requirements of the architecture. 

Abstractions: representation of the system and its components by models or drawings. 

E-Business System: 

- Interface: Suppliers with Purchasing & Receiving 
- Components: Value Adding Processing, Marketing, Sales, Finance and Accounting
- Boundary: Competitors, Employees and Prospective Employees, Culture, Language, Government, Law, Financial Resources. 
- Environment

Top-Down Approach: Decomposition of a system into hierarchal components and concentration at appropriate levels of detail. Allows focus on specific areas of interest without distraction of irrelevant details.  

Application Architecture: Flow and processing of data within an organization or between organizations or between an organization and its environment. Primary concerned with the activities and processing of application programs and communications between them.  

Client-Server Computing Model: a program on client computer accepts services and resources from a complimentary program on a server computer. The services and resources include application programs, processing services, web services, file services, print services, directory services, e-mail, remote access services, computer start-up initial services. 

- "Cloud" link exists between the client and the server in the form of a network, intranet, or internet connection. Server might be a cluster of computers. 
- Does not require special computer hardware 
- Requests and responses take form of data messages between the client and the server. 
    - "Get" requests a web page and a response contains the HTML text for the page. 
- Shared Server: a number of clients sharing a number of servers with multiple services on the same network. 
- Multiple applications can run on a server but potential slowdowns may result from the load and traffic. 
- Server can have multiple clients, and a client can requests services from multiple servers. 
- Advantages: 
    - Central location makes the resources and services easy to locate for clients, but easy to protect, control, and manage resources. 
    - Ability to store, process, and manage a large amount of data.

Two Tier Architecture: two computers involved in a service. 

- Client computer running Web browser application, a server computer running web server application, a communication link between them, and a set of standard protocols (HTTP) for communication between them. 

Three Tier Architecture: Two-tier with an additional computer system for the database. 

- CGI: Common Gateway Interface: protocol for making communication between Web server and the database application possible. 

N-Tier Architecture: seperating different applications and processing resulting in better overall control. 

Middleware: resides between servers and clients. Resolves problems (incompatible message and data formats) between request and response messages from client and servers. 

### Web Based Computing: 

Intranet: organization's internal network. 

XML: eXtended Markup Language. Allows easy identification of relevant data within data streams between interconnected systems

Cloud Computing: many function of an organization data center can be moved to serviesc on the internet. Provides off-site storage facilities for an organization. Services can be used as a backup resource or recovery. 

Software as a Service (SaaS): provides software application that run on a server and delivers results to the display of a client. 

Platform as a Service (PaaS): extends cloud services to software facilities on a developers computer. 

- Web and programming development tools, web server, facilities, operating system application program interface (API). 
- Provides everything a developer would need to create and run application software on a cloud platform without hardware and software investment (no local support). 

Infastructure as a Service (IaaS): cloud-based hardware emulation in the form of virtual machines and networking. User/developer interacts with the virtual machine using a client application. 

Advantages of Cloud Computing: 

- Client data is simlplified and cost reduced. Not necessary to provide, support, update, and mantain individual copies of software for every user. No need to purchase hardware. 
- User collaboration. Multiple users can access same software, databases, tools, and data files from the cloud. 
- Access from wide varienty of equipment wherever internet is available. 
- Scalable. More memory, storage, virtual machines can be added to support. 
- Can continue to provide service and recovery during emergency. 
- Short computing needs without the overhead. 
- Allows developers to make risky changes to virtual machine wihtout threatening production equipment. 

Risks: 
- Security management. Data leak or theft can compromise. 
- Cloud server outage or loss of connectivity can cause problems. Dependency on internet connection. 
- Dependency on cloud service by client. 

### Peer to Peer Computing: 

Peer to Peer Architecture: treats computers in a network as equals - ability to share files and other resources between them.

- Synchronization is difficult because files can be stored at different versions on different computers. 
- Great to share a local printer or files between personal computers. 
- Removes the heavy loads and network traffic associated with a server. 
- Legal ramifications, illegal to share copywrited material on a server (not illegal Peer to Peer). 
- Viruses are easily spread and identity theft. 

<<<<<<< HEAD
# Chapter 3: Number Systems
=======
### Google: A System Architecture Example

Google IT System Requirements: 

- Must be able to respond to millions of requests around the world. Match results and advertising with language, geographic, and culture based on location of user. 
- Troll internet systematically to retrieve and organize data for response requests. Processing mechanism to establish ranking of results. 
- Request results must be near to 100 percent accurate. Individual hardware nad software component failures must not affect system performance. 
- System must be scalable to handle increasing users while being cost effective. 

Application Level System Requirements:

- System must accept search requests from users, identify and rank matches, create a web page, and serve it to the user. 
- System must collect data (crawling), indentifying search terms for every web page it encounters and create an index. 
- System must manage and serve advertisements based on user search requests.

Domain Name Services (DNS): used by web browser to identify the IP address of Web server

Shards: computer and databases divided among hard disks on many computers. 

## Chapter 3: Number Systems

Decimal: base 10 number system

Base: the number of digits, including zero, that exist in the number system. 

Binary: base 2 number system

Binary Arithmetic: calculations performed.

Binary Number: each digit, known as a bit, can have only a value of 0 or 1. 

Bits are stored in group sof 8 bits (byte), 16 bits (halfword), 32 bits (word), 64 bits (doubleword). 

Java:

- Short (16 bits)
- Int (32 bits)
- Long (64 bits)

Hexadecimal number: represents a 24-bit binary number. Base 16.
Octal: base 8 number system. 
>>>>>>> 335abdfdea7fc6e34d008d83513ef7851654e4fe
