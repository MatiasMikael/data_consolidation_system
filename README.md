# Data Consolidation System

## **Yleiskuvaus**
Data Consolidation System on Pythonilla toteutettu järjestelmä, joka yhdistää dataa kolmesta eri lähteestä: CSV-tiedostoista, JSON-tiedostoista ja PostgreSQL-tietokannasta. Järjestelmä seuraa PEP 8 -ohjeistusta ja sisältää siististi organisoidut skriptit, jotka noudattavat hyvää koodauskäytäntöä.

Projekti on suunniteltu käsittelemään ja yhdistämään erilaisia datalähteitä yhteen käyttökelpoiseen formaattiin jatkokäsittelyä varten, kuten analytiikkaan tai tallennukseen. Versionhallinta on toteutettu Gitin avulla, mikä mahdollistaa helpon kehityksen seurannan ja yhteistyön.

---

## **Käytetyt kirjastot ja työkalut**
### **Python-kirjastot:**
- **`pandas`**: Datan lataamiseen, yhdistämiseen ja tallentamiseen.
- **`sqlalchemy`**: PostgreSQL-tietokantayhteyden luomiseen ja hallintaan.
- **`dotenv`**: Ympäristömuuttujien hallintaan turvallisesti.
- **`os`**: Tiedostojen ja hakemistojen hallintaan.

### **Muut työkalut:**
- **PostgreSQL**: Relaatiotietokannan hallintaan.
- **Git**: Versionhallintaan ja projektin seurantaan.
- **ChatGPT**: Projektin suunnitteluun ja toteutukseen.

---

## **Skriptit ja niiden tehtävät**
### **1. `fetch_data.py`**
- Hakee dataa seuraavista lähteistä:
  - **CSV**: Lataa tiedoston `2_data/data1.csv`.
  - **JSON**: Lataa tiedoston `2_data/data2.json`.
  - **PostgreSQL**: Hakee tiedot taulusta `asiakas_taulu`.
- Tallentaa yhdistetyn datan tiedostoon `3_results/combined_data.csv`.
- Tallentaa kaikki tapahtumat ja virheet lokitiedostoon `5_logs/fetch_data.log`.

### **2. `combine_data.py`**
- Yhdistää CSV-, JSON- ja PostgreSQL-datat yhteiseen DataFrameen.
- Yhdistäminen tapahtuu `id`-sarakkeen perusteella.
- Tallentaa yhdistetyn datan tiedostoon `3_results/combined_data_cleaned.csv`.

### **3. `clean_data.py`**
- Siistii yhdistetyn datan:
  - Valitsee ja uudelleennimeää tarvittavat sarakkeet.
  - Poistaa mahdolliset duplikaatit.
- Tallentaa siistityn datan tiedostoon `3_results/combined_data_cleaned.csv`.
- Tallentaa tapahtumat lokitiedostoon `5_logs/clean_data.log`.

---

## **Lisenssi**
Tämä projekti on lisensoitu **MIT-lisenssillä**. Voit käyttää, muokata ja jakaa projektia vapaasti, kunhan mainitset alkuperäisen tekijän.
