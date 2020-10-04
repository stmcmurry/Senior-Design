//Dummy Motor Pins
//https://www.kevinhughes.ca/blog/arduino-bluetooth-xbox-360-controller-fun.html
int M1 = 1;
int E1 = 2;
int O1 = 3;
int W1 = 4;

void setup() {
  // put your setup code here, to run once:
  
  //set pin modes
  pinMode(M1, OUTPUT);
  pinMode(E1, OUTPUT);
  pinMode(O1, OUTPUT);
  pinMode(W1, OUTPUT);

  // init
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  int command;
  

}

void turnRight(){
  
}

void turnLeft(){
  
}

void speedUp(){
  
}

void stop(){
  
}
