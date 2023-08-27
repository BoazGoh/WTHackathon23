#include <Stepper.h>
#include <Servo.h>

#define FULLSTEP 4

int start = 0;
int pos1 = 0;
int pos2 = 0;
unsigned long currentTime;
unsigned long newTime = 0;
const int stepsPerRevolution = 2048; 

Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
Servo myservo;
Servo myservo2;

void setup() {
  // put your setup code here, to run once:
  pinMode(2,INPUT); //homing
  pinMode(4,OUTPUT); //output
  pinMode(6,INPUT); //a
  pinMode(7,INPUT); //b
  Serial.begin(9600);
  myservo.attach(3); 
  myservo2.attach(5); 
  myStepper.setSpeed(1000);
  newTime = millis();
}

void loop() {
  // put your main code here, to run repeatedly:
  currentTime = millis();
  if((currentTime - newTime) >= 30000)
  {
    newTime = currentTime;
    int A,B;
    turn(60);
    for (int j = 0; j < 2; j++)
    {
      turn1(70);
      turn1(-70);
      delay(500);
      /*
      digitalWrite(4,HIGH);
      delay(100);
      digitalWrite(4,LOW);
      A = digitalRead(6);
      B = digitalRead(7);

      while (A == B)
      {
        A = digitalRead(6);
        B = digitalRead(7);
      }

      if (!(A != 1 && B == 1))
      {
        Serial.println("error!");
      }
      */
      turn2(90);
      turn2(-90);
    }

    delay(1000);
    
    turn(60);
    turn1(70);
    turn1(-70);
    delay(500);
    /*
    digitalWrite(4,HIGH);
    delay(100);
    digitalWrite(4,LOW);
    A = digitalRead(6);
    B = digitalRead(7);

    while (A == B)
    {
      A = digitalRead(6);
      B = digitalRead(7);
    }

    if (!(A != 1 && B == 1))
    {
      Serial.println("error!");
    }
    */
    turn2(90);
    turn2(-90);
  }
}

void turn(int angle)
{
  int steps;
  steps = stepsPerRevolution/360*angle;
  myStepper.setSpeed(10);
  myStepper.step(steps);
}

void turn1(int angle)
{
  if (angle > 0)
  {
    for (pos1 = 0; pos1 <= angle; pos1 += 1) 
    { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos1);
      delay(6);
    }
  }

  else
  {
    for (pos1 = -angle; pos1 >= 0; pos1 -= 1) 
    { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo.write(pos1); 
      delay(6);             // tell servo to go to position in variable 'pos'
    }
  }
}

void turn2(int angle)
{
  if (angle > 0)
  {
    for (pos2 = 0; pos2 <= angle; pos2 += 1) 
    { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo2.write(pos2);              // tell servo to go to position in variable 'pos'
      delay(6);                       // waits 15 ms for the servo to reach the position
    }
  }

  else
  {
    for (pos2 = -angle; pos2 >= 0; pos2 -= 1) 
    { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      myservo2.write(pos2);              // tell servo to go to position in variable 'pos'
      delay(6);                       // waits 15 ms for the servo to reach the position
    }
  }
}