Program Title: Remote Command -rcmd

Modules and their IOs for this program:

		Lab6_Client: keyboard input = Server IP Adress, Port Number, Time Delay (in seconds), Number of Executions, Command- ---------->Press enter and "UDP or TCP?" wil then appear,so type which one you want to use.
				   example = "127.0.0.1 5010 2 5 print"----------------------------------------------------->Press enter
			           UDP or TCP?: "UDP" ---------------------------------------------------------------------->Press enter
				   

		Lsb6_Server: keyboard input= TCP Port Number
				   example = "5010"--------------------------------------->Press enter
                                   UDP or TCP?: "UDP" ------------------------------------>Press enter

		*RUN SERVER THEN CLIENT*

What this program does:

	1. Sets up a socket between multiple (at least 5) clients and a server, where the server waits and listens for messages from the client.
	2. The client accepts the above defined inputs (server's IP address, time delay, number of executions, and command) from the keyboard and sends it to the server.
	3. The client recieves the result from the server, diplays it and terminates the connection.

	4. The server accepts the above defined inputs (the port number, UDP or TCP). 
	5. When the connection is made, the time, client ip, command and "connected" is printed at the server.
	6. The command is executed at the server the number of time requested, identifying the run time.
	7. When the connection is lost, the time, client ip, port and "disconnected" is printed at the server.