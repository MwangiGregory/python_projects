# TCP CHAT

This is a simple command line based chat application. It utilzes sockets to open a persistent bidirectional communication channel between a server and many hosts. 

I have utilized the sockets module which comes inbuilt with python.

## Usage

1. Ensure you have python 3.8+ installed
2. Download the scripts on a computer and note their locations.
3. Locate the server script and run this command:
```
py server.py
```
4. Open a new terminal window in the same location as the client.py script and run the following command
```
py client.py
```
5. A communication channel is now open between the two scripts. Type anything into either of the terminals and press enter. The text should appear in the corresponding script.
6. To close, press CTRL + C on the client script first, then the client script.

