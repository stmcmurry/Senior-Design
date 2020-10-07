#include<SoftwareSerial.h>

/*
 * There are 15 channels between the Bluetooth advanced  remote controller and the APP, and each channel corresponds to a key, the remote controller will send different data to the app according to the buttons, Generally, the data format sent by the remote controller is as follows:
“M12BT:”  +  0xA4  +  30  +  DATA  +  SUM    
            “M12BT：” Package Header   
              0xA4              ID
             30         Data Length
  DATA       15 channels data
  SUM       BCC checksum
 
The 15channels data format as follows:
CH1_H + CH1_L + CH2_H + CH2_L + …… + CH11_H + CH11_L + CH12_H + CH12_L  + CH13_H + CH13_L + CH14_H + CH14_L+ CH15_H + CH15_L
              （High eight bits firs）

 */

#define TxD 10
#define RxD 9

SoftwareSerial bluetoothSerial(TxD, RxD);

char c;

void setup() {
  // put your setup code here, to run once:
  bluetoothSerial.begin(9600);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(bluetoothSerial.available()){
    c = bluetoothSerial.read();
    stringChecksum(c);
  }
}

byte stringChecksum(char s)
{
    byte c = 0;
    while(s != '\0')
        c ^= s++;
    return c;
}
