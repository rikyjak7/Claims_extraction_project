# Progetto di Estrazione di Claims da Tabelle HTML Relazionali

Questo progetto ha come obiettivo l'estrazione automatica di claims (dati scientifici) da tabelle HTML relazionali. Le tabelle contengono metodi e metriche, e il nostro codice estrae in modo strutturato i risultati, associando ogni metodo alle metriche corrispondenti, includendo anche valori come le deviazioni standard (quando presenti).

## Funzionalità Principali

- **Estrazione dei dati da tabelle HTML**: Il codice estrae i dati da una tabella HTML, identificando le metriche e i metodi.
- **Formattazione dei claims**: I dati vengono strutturati in un formato facilmente leggibile e interpretabile.
- **Supporto per tabelle generiche**: Il codice è stato progettato per essere flessibile e adattarsi a tabelle con qualsiasi numero di metodi e metriche.
- **Gestione delle deviazioni standard**: Quando una metrica include una deviazione standard nel formato "valore ± deviazione", il codice gestisce correttamente questa informazione.

## Tecnologie Utilizzate

- **Python 3.x**: Linguaggio di programmazione utilizzato per lo sviluppo del progetto.
- **BeautifulSoup**: Libreria Python per il parsing di HTML.
- **Regular Expressions (regex)**: Per estrarre e manipolare i dati numerici (inclusi valori e deviazioni).

## Come Funziona

1. **Parsing della Tabella HTML**: Il codice esamina il contenuto della tabella HTML e ne estrae la struttura. Vengono identificati i metodi (nella prima colonna) e le metriche (nelle intestazioni delle colonne).
   
2. **Estrazione dei Dati**: Una volta ottenuti i metodi e le metriche, il codice raccoglie i valori associati a ciascun metodo e li formatta in un claim.

3. **Formato dei Claims**: Il risultato finale è una lista di claims nel formato:


4. **Flessibilità**: Il codice può gestire tabelle con qualsiasi numero di righe (metodi) e colonne (metriche).

## Come Eseguire il Codice

### Requisiti

- Python 3.x
- BeautifulSoup4: Puoi installarlo utilizzando pip:

```bash
pip install beautifulsoup4

   
