import processing.serial.*;

import hypermedia.net.*;

UDP udp; //define the UDP object

void setup() {

udp = new UDP (this, 6000); //create new datagram connection on port 6000
udp.log(true); //print out the connection activity (optional)
udp.listen(true); //wait for incoming message
}

void draw() {
}

void keyPressed() {
  int buffer = 24;
  String ip = "192.168.16.100"; //remote IP address to send string to
  int port = 8888; //destination port
 
  udp.send("24", ip, port); //the message to send
}

void receive( byte[] data ) { //default handler
//void receive( byte[] data, String ip, int port ) { // extended handler
  for(int i=0; i < data.length; i++)
  print(char(data[i]));
  println();
}
