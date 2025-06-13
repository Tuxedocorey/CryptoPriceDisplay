int UP = 13;
int DOWN = 12;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);  // Increased timeout
  pinMode(UP, OUTPUT);
  pinMode(DOWN, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String message = Serial.readString();
    message.trim();  // Removes newline and extra whitespace

    

    if (message == "up") {
      digitalWrite(UP, HIGH);
      digitalWrite(DOWN, LOW);
    }
    else{
      digitalWrite(DOWN, HIGH);
      digitalWrite(UP,LOW);
    }
  }
}
