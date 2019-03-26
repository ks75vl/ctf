

void setup() {
	
	Serial.begin(115200);
	pinMode(10, OUTPUT);
	pinMode(11, INPUT);
	pinMode(12, OUTPUT);
}

int value = 0;
int input = 0;

void loop() {

	if (Serial.available() > 0) {
		input = Serial.read();
	}
	
	value = digitalRead(11);
	Serial.print("Pin11 = ");
	Serial.println(value);
	digitalWrite(10, value);

	value = analogRead(A0);
	Serial.print("PinA0 = ");
	Serial.println(value);
	analogWrite(12, value);

	delay(100);
}
