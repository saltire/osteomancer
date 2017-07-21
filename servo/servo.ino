#include <Servo.h>

int servoPin = 9;
Servo servo;

int angle = 0;
int target = angle;

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);

    Serial.begin(9600);

    servo.attach(servoPin);
}

void loop() {
    if (Serial.available()) {
        target = Serial.read();
        if (target > 180) {
            target = 180;
        }
    }

    int angle = servo.read();

    if (target != angle) {
        digitalWrite(LED_BUILTIN, HIGH);

        if (target > angle) {
            angle += 1;
        }
        else if (target < angle) {
            angle -= 1;
        }

        servo.write(angle);
        delay(15);
    }
    else {
        digitalWrite(LED_BUILTIN, LOW);
    }
}
