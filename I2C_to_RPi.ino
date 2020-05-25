const int LED = A5;

void setup()
{
    Wire.begin(0x8);
    Wire.onReceive(receiveEvent);

    pinMode(LED, OUTPUT);
    digitalWrite(LED, LOW);
    digitalWrite(LED, HIGH);
    delay(1000);
    digitalWrite(LED, LOW);
}

void receiveEvent(int howMany)
{
    while (Wire.available())
    {
        char c = Wire.read();
        digitalWrite(LED, c);
    }
}

void loop()
{
    delay(100);
}
