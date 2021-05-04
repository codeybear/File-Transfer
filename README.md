
HTTP File Sender
=================

Command line utility to scan a folder and send files via HTTP to a server.

Requires Python 3.6 or above, only built in libraries are used so no need to install any packages.

To run the server:  
python server.py "{destinationfolderpath}"

Run the client:  
python client.py "{sourcefolderpath}"

Edit the config.py file to setup configuration of server HTTP address, port and buffer size which relates to the size of file chunks to transfer.

Both programs need to be cancelled with a keyboard interrupt i.e. CTRL+C on both Windows and Linux.

Note:  
If a file fails to send the program will retry it until it goes.  
If a file is modified a checksum change will unsure the file is resent.
