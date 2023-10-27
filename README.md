# Tekle Negusa: IoT-Personräknaren 🧠👥🔢

## 🤝 Skapad av Marcus, Jimmy & Bam

### Inledning

Hej! Vi är Marcus, Jimmy och Bam. Välkommen till vårt projekt, **Tekle Negusa: IoT-Personräknaren**. Detta är en del av vår kurs "Datorkommunikation, Nätverk & Konnektivitet". Tekle Negusa är en personräknare byggd med 🔗[Arduino Rev 4 ](https://www.kjell.com/se/produkter/el-verktyg/elektronik/utvecklingskit/arduino/utvecklingskort/arduino-uno-rev4-wifi-utvecklingskort-p88079) utvecklad för att spåra antalet personer som passerar genom en specifik plats. Genom att använda IoT-teknik och sensorer har vi skapat en robust och pålitlig lösning för att samla in och analysera rörelsedata i realtid.



## 📋 Innehållsförteckning

1. **Systemkrav**
    - ***Sensor***
    - ***Databas***
    - ***Frontend***
2. **Rutiner***
3. **Tekniska Färdigheter**

---

## 🛠 Systemkrav

### Sensor 🎯

#### Hur och Varför

- **Typ**: PIR-rörelsensensor
- **Funktionsmetod**: Passiv Infraröd (PIR)
- **Funktion**: Detekterar rörelse baserat på förändringar i infrarött ljus.

🤓 **Vår Research**  
Efter att ha övervägt olika sensorer, bestämde vi oss för PIR som den mest lämpade för vår uppgift. Den erbjuder den precision vi behöver utan onödig teknologisk komplexitet.

#### Alternativ Utforskat

- **Lasersystem**: För komplicerat och svårt att implementera.
- **Distanssensor**: Inte optimalt för vår användning; för mycket bakomliggande komplexitet.

---

### Databas 🗃️

#### MongoDB

- **Typ**: Dokumentorienterat NoSQL
- **Datapunkter**: `id` och `timestamp`

🔗 **API**: [FASTAPI](https://fastapi.tiangolo.com/) används för att hämta data till frontend.

---

### Frontend 🌐

#### Verktyg

- **Initialt**: Grafana
- **Slutligt beslut**: Python Flask

💡 **Varför Flask?**  
Eftersom det är enklare och mer effektivt för vårt projekt.



## 🛠 Tekniska Färdigheter

- **Kommunikationsprotokoll**: Pub/Sub, Kafka, SQS, Pusher, MQTT
- **Databashantering**: MongoDB
- **IoT programvara**: Arduino Rev 4
- **Övergripande kunskap inom IoT**: Säkerhet, Roll-out, Uppstart, Patchning/Uppdatering

---

🙏 Tack för att du tog dig tid att läsa! Om du har några frågor, tveka inte att nå ut till oss!

**Marcus, Jimmy & Bam** 🌟