#!/usr/bin/python

'''
    SIPCheck is a tool that parse the file /var/log/asterisk/messages looking for error and 
    warnings messages from unauthorized access or trying calls from anonymous users and add 
    their ip to the firewall and warns to sinologic server to add for global list of banned 
    ip.
'''

'''
    Check if our database is available and get when was the last time we run this script

    Database has got this tables:
	- ipbanned : table with the list of the ip banned on Sinologic.
	- configure: table with the values of:
		+ last time we run this script
		+ datetime of the ipbanned table
		+ 
	- ipsuspect: table with the list of the ip suspected of attacks
	

    1. Get all values of the "configure" table.
    2. Check the datetime of the ipbanned table:
    2.1. If datetime is > 48 h, connect to Sinologic and download the new list of ip banned.
    3. Check /var/log/asterisk/messages and looking for 'Wrong password' or 'rejected' words
    3.1. For each line found, we parser the line and get the IP address suspected (IPAS).
    3.2. If IPAS exists in ipsuspect table, do nothing. Else, insert into the ipsuspect table.
    4. Once the parser has finished to analyze the log file, create a request to send like POST method all ipsuspect found.
    5. If it is required, add to the firewall new ip address suspected.

'''

