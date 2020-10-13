#include <Ethernet.h>

//DEFINITIONS-----------------------------------------

byte mac[] = { 0x34, 0xF3, 0x9A, 0x1E, 0x90, 0x24 }; //mac adress
IPAddress ip(192,168,16,100); //ip address

unsigned int localPort = 8888; //udp port to listen for packets on

char packetBuffer[UDP_TX_PACKET_MAX_SIZE];

EthernetUDP Udp; //creates Udp instance

char f1 = 10; //char to compare packetBuffer to
char f2 = 24; //char to compare packetBuffer to


void setup() {
 
  Ethernet.init(10); //sets CS pin for ethernet shield

  Ethernet.begin(mac, ip); //initializes ethernet with mac and ip addresses

  Serial.begin(9600); //initializes serial connection. Waits for serial to be available (native usb only).
  while (!Serial) {
    ;
  }

  //Checks for presence of Ethernet shield. Halts if no ethernet hardware present.
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found. Sorry, can't run without hardware. :(");
    while (true) {
      delay(1);
    }
  }
  //Checks for presence of etherner link.Halts if no link present.
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }
  Udp.begin(localPort); //begins udp on port specified above.
}



void loop() {
 
  int packetSize = Udp.parsePacket();
  if (packetSize) {                     //if data available, prints following;

    Serial.println("----------------------------------------------");
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    for (int i = 0; i < 4; i++) {
      Serial.print(remote[i], DEC);
      if (i < 3) {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(Udp.remotePort());

    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.print("packetBuffer = ");
    Serial.println(packetBuffer);
    if (packetBuffer[0] == f1) {
      Serial.println("Contents:");
      Serial.println("10 received via UDP!");
    } else if (packetBuffer[0] == f2) {
      Serial.println("Contents");
      Serial.println("24 received via UDP!");
    } else {
      Serial.println("SOMETHING WENT WRONG");
    }
    Serial.println("----------------------------------------------");

    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.write("acknowledged", 13);
    Udp.endPacket();
  }
 
}
