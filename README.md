# Network-Learning-Application-with-Packet-Sniffer

[![](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Introduction
This app let you translate data packet in network with natural language. It's using packet sniffer that i made with Python and Scapy to capture the data packet and translate it using couple parameters based on protocol that the data packet get. It will display the result as a table contain raw and translated result. 

## Instalation
To install this program you need to install Python and use Python IDE like Pycharm. 

```
https://www.jetbrains.com/pycharm/
```

Then i recommend you to use Python 3.6 as Project Intepreter. You can change it on the setting of your IDE. After that in terminal run this command to install some modules needed.

```
pip install psutil
pip install scapy
pip install mysql-connector
pip install PyQt5
```
Then install the database using MySql. Sql Dump locate in
- resource
  - Database
    - **db_app.sql**

Run the program in your IDE and Enjoy :)

## Usage

- This program is using Bahasa Indonesia as the language. There are four menu in the main menu. First is Show Network Traffic, Second is Quiz, Third is Glossary, and the last one is About Me. 

<img src="https://i.ibb.co/JRYNGLh/image.png" title="MainMenu" alt="Main Menu">



- In "Show Network Traffic" menu you can either choose to see result that has been stored in database or do the sniffing proccess itself in realtime. 

<img src="https://i.ibb.co/8BW59Vf/image.png" title="ShowNetworkTraffic" alt="Show Network Traffic">


- If you choose to see result that has been stored to database, you can see the table that show all of the name result, when it was taken, and packet itself. You can also find the name result by search it on the search bar that locate on top of the table. This will make your life easier. You can click "Detail Paket" at every stored row to see all the packet that being stored under that name.

<img src="https://i.ibb.co/bdbbhBQ/image.png" title="Stored Sniffing Result" alt="Stored Sniffing Result">



- When you click that button, you will see translation result with protocol name in the first word. Some parameter of the packet ex IP Address, port, and data size will be show. All of that parameter are being arrange in a sentece to make the packet more understandable. If user want to see raw packet, there is "Detail" button that can show all the information that packet carry. 

<img src="https://i.ibb.co/N7JGbgT/image.png" title="Translated Sniffing Result" alt="Translated Sniffing Result">




- Here you can see raw data that a packet has. Every parameter that being used in translated result before are get from here. User can see all the parameter that being contain in every single packet. Each packets will contain different parameter as it will be depend on what protocol they are using.

<img src="https://i.ibb.co/vhwf4YW/image.png" title="Raw Sniffing Result" alt="Translated Sniffing Result">

