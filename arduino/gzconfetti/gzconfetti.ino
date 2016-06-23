/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/

struct buf64 {
    char str[64];
    int nextChar;
};
buf64 cmdBuf;


void exeCmds(char str[64]){  //Take a command string (whitespace stripped) and execute it.

    if (str[0] == '1'){
        digitalWrite(8, HIGH);
    }
    else if (str[0] == '0'){
        digitalWrite(8, LOW);
    }
    else if (str[0] == 'M'){
        digitalWrite(7, LOW);
    }
    else if (str[0] == 'N'){
        digitalWrite(7, HIGH);
    }
}


void sendReport(String report){

    Serial.println(report);
}


void serialEvent(){  //Upon receiving new serial data, read it in (ignoring spaces) and execute the command if a newline character is detected
    
    unsigned char ch;

    while (Serial.available() > 0){

        ch = Serial.read();

        //Serial.print("I just read the character ");
        //Serial.println(ch);
        
        if (ch != '\n' && ch != ' '){
            //Serial.println("ch wasn't a newline or space");
            cmdBuf.str[cmdBuf.nextChar] = ch;
            cmdBuf.nextChar++;
        }
        else if (ch == '\n'){
            //Serial.print("ch was a newline, so I need to execute this string: ");
            //Serial.println(cmdBuf.str);
            cmdBuf.str[cmdBuf.nextChar] = ch;
            cmdBuf.nextChar = 0;
            exeCmds(cmdBuf.str);
            cmdBuf.str[0] = '\0';
            //Serial.print("I have reset the string to: ");
            //Serial.println(cmdBuf.str);
        }
    }
}


void setup() {
    Serial.begin(9600);
    pinMode(4, OUTPUT);
    digitalWrite(4, HIGH);
    pinMode(7, OUTPUT);
    digitalWrite(7, HIGH);
    pinMode(8, OUTPUT);
}

void loop() {
    ;  //Should prob put something here to save power, so as not to churn away doing nothing
}

