
HTTP Files Sender
=================

Command line utility to scan a folder and send files over an HTTP socket

Requires Python 3.6 or above, only built in libraries are used.

Run the client:  
python client.py "{folderpath}"

Run the server:  
python server.py "{folderpath}"

Edit the config.py file to setup configuration of HTTP address, PORT and buffer size which relates to the size of file chunks to transfer.
