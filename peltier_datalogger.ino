#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors(&oneWire);

#include <SD.h>

const int chipSelect = 10;
File myFile;
int p=0;
#include <Arduino.h>
#include <U8g2lib.h>
U8G2_SSD1306_128X64_NONAME_2_SW_I2C u8g2 (U8G2_R0, A5, A4);
unsigned long t;
void setup(void)
{

  Serial.begin(9600);
  
  

   pinMode(A4, OUTPUT);
  digitalWrite(A4, 0);
  u8g2.begin();
  u8g2.setPowerSave(0);
    SD.begin(chipSelect);
    pinMode(5, INPUT);

}
void loop() {
   int btn = digitalRead(5);
     if (btn==1){
      SD.remove("test.txt");
      Serial.println("file removed");
     }
     else{
  sensors.requestTemperatures(); 
    
    float temp = sensors.getTempCByIndex(0);
    t = millis();
    int s = (t/1000)%60;
    int m = (t/1000)/60;
   
    String T= "Temp:"+String(temp);
    String Time = "Time: "+String(m);
  String s_ = ":"+String(s);
    Serial.print("Temp:");
    Serial.println(temp);
    myFile = SD.open("/test.txt", FILE_WRITE);
    if(myFile){
      myFile.print(temp);
      myFile.print("      ");
      myFile.print(m+s_);
      myFile.println("");
      myFile.close();}
    else{Serial.println("error");}      
    u8g2.firstPage();
     do {
      u8g2.setFont(u8g2_font_ncenB14_tr);
  u8g2.setCursor(0, 15);
      u8g2.print(T);
      
      u8g2.setCursor(0, 55);
      u8g2.println(Time+s_);
     
     }
     while(u8g2.nextPage());
   
     }
  }


