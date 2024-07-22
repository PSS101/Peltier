/*
  SD card read/write

  This example shows how to read and write data to and from an SD card file
  The circuit. Pin numbers reflect the default
  SPI pins for Uno and Nano models:
   SD card attached to SPI bus as follows:
 ** SDO - pin 11
 ** SDI - pin 12
 ** CLK - pin 13
 ** CS - pin 4 (For For Uno, Nano: pin 10. For MKR Zero SD: SDCARD_SS_PIN)

  created   Nov 2010
  by David A. Mellis
  modified  24 July 2020
  by Tom Igoe

  This example code is in the public domain.

*/
#include <SD.h>

const int chipSelect = 10;
File myFile;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  // wait for Serial Monitor to connect. Needed for native USB port boards only:


  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
SD.begin(10);

  delay(2000);
  myFile = SD.open("/test.txt");
  if (myFile) {
    

    // read from the file until there's nothing else in it:
    while (myFile.available()) {
      Serial.write(myFile.read());
      
    }
    // close the file:
    myFile.close();
  } else {
    
    
  }
}

void loop() {
  // nothing happens after setup
}
