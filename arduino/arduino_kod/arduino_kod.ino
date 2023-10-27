#include <WiFiNINA.h>

char ssid[] = "Wi-Fi";
char pass[] = "Lösenord";

char server[] = char server[] = "192.168.1.129";  


WiFiClient client;

int lastState = LOW;
int currentState = LOW;
const int PIRPin = 2; 
const int ledPin = 13;

void setup() {
  
  pinMode(PIRPin, INPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  Serial.begin(9600)

  // Anslut till WiFi
  while (WiFi.status() != WL_CONNECTED) {
    WiFi.begin(ssid, pass);
    delay(5000);
  }
}

void loop() {
  currentState = digitalRead(PIRPin);

  if(currentState == HIGH && lastState == LOW) {
    digitalWrite(ledPin, HIGH);
    sendPersonDetected();

    Serial.println("Rörelse detekterad! En person har detekterats.");

    delay(1000);
    digitalWrite(ledPin, LOW);
  }

  lastState = currentState;
  delay(1000);
}

void sendPersonDetected() {
  if (client.connect(server, 80)) {
    client.println("POST /personDetected HTTP/1.1");
    client.println("Host: DIN_SERVER_ADRESS");
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.println("Connection: close");
    client.println();
  }
}
