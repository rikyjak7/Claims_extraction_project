def prompt_function(lista, caption, paragraphs):

    prompt = """
    Ti fornirò:

    -Una lista di celle, organizzate riga per riga, che rappresentano una tabella HTML. Ogni cella è composta da una coppia {nome, valore}.
    -Una caption della tabella che descrive brevemente il suo contenuto.
    -Alcuni paragraphs come contesto aggiuntivo che possono fornire chiarimenti o spiegazioni sui dati riportati.

    Il tuo compito è:

    -Identificare e separare le informazioni in specifiche (Specifications) e metriche di output (Measures).
    -Trattare ogni riga della tabella come una riga di risultato, dove:
    Le specifiche descrivono i dettagli dell'esperimento o del modello (come dimensione, configurazioni o altre proprietà).
    Le metriche di output descrivono esclusivamente i risultati di valutazione o performance.
    -Crea un output per ogni riga della tabella nel seguente formato:
    |{|Specification|, |Specification|, …}, Measure, Outcome|

    Dove:

    Specification: una coppia {nome, valore},dove il nome corretto della specifica (come ad esempio i nomi di colonne) deve essere cercato sia nella table,
    nella caption o nei paragraphs (ad esempio, un modello, un dataset, una configurazione, un dominio ...), 
    mentre il corrispettivo valore dovrà essere cercato nella table. 
    Measure: una metrica utilizzata per valutare l'esperimento o il modello, da ricercare su tutti 
    e 3 gli input forniti:lista,caption,paragprah (esempi di metriche sono "Accuracy", "EER (%)", "F1-measure" ...).
    Outcome: il valore corrispondente alla misura di output (ad esempio, "0.89", "13.39%" ...).

    Regole:
    -Analizza attentamente i paragraphs e la caption per interpretare quali informazioni sono specifiche e quali sono metriche di output.
    -Se una riga contiene più metriche di output, suddividi la riga in più righe, ciascuna con una sola misura e un solo valore di outcome.
    -Includi eventuali valori mancanti indicandoli come "-none-" dalla sezione delle specifiche o metriche.

    Esempio generico:

    Dati di input:

    |Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Level 1, 0.760|
    |Model Type, General LLM|, |Model Name, Codex Da-vinci|, |Parameter Size, 175B|,  |Level 1, 0.730|
    |Model Type, General LLM|, |Model Name, GPT-4|, |Parameter Size, 1.76T|, |Level 1, 0.861|

    |Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Level 2, 0.799|
    |Model Type, General LLM|, |Model Name, Codex Da-vinci|, |Parameter Size, 175B|,  |Level 2, 0.799|
    |Model Type, General LLM|, |Model Name, GPT-4|, |Parameter Size, 1.76T|, |Level 2, 0.866|

    |Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Level 3, 0.408|
    |Model Type, General LLM|, |Model Name, Codex Da-vinci|, |Parameter Size, 175B|,  |Level 3, 0.392|
    |Model Type, General LLM|, |Model Name, GPT-4|, |Parameter Size, 1.76T|, |Level 3, 0.700|


    Caption: "Table 1: Benchmark results of execution match of all models we tested on the 'dev' SPIDER dataset."

    Paragraphs: "In our experimentation, we organized the models into three distinct groups as illustred i n Table 1: general purpose LLms,.
    Code-Specific LLMs, and Sequence-to-Sequence models. Table 1 further presents the Execution Match score on the SPIDER dataset for each studied LLM 
    and for each of the four difficulty levels. Note"  

    Output atteso:

    |{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.760|
    |{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.799|
    |{|Model Type, General LLM|, |Model Name, ChatGPT-3.5-turbo|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.408|
    
    |{|Model Type, General LLM|, |Model Name, Codex Da-vinci|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.730|
    |{|Model Type, General LLM|, |Model Name, Codex Da-vinci|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.799|
    |{|Model Type, General LLM|, |Model Name, Codex Da-vinci|, |Parameter Size, 175B|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.392|

    |{|Model Type, General LLM|, |Model Name, GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, 1|}, Execution Match , 0.861|
    |{|Model Type, General LLM|, |Model Name, GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, 2|}, Execution Match , 0.866|
    |{|Model Type, General LLM|, |Model Name, GPT-4|, |Parameter Size, 1.76T|, |Dataset, Spider dev|, |Difficulty Level, 3|}, Execution Match , 0.700|

    Concentrati solo sui dati forniti e non fare inferenze al di fuori di ciò che è descritto esplicitamente.
    Se qualcosa non è chiaro, interpreta in modo conservativo basandoti su caption e paragraphs.
    Astieniti dal restituire informazioni aggiuntive o note ulteriori che esulano dall'output richiesto da noi.

    I dati su cui devi lavorare sono:

    -lista:""" + lista + """

    -caption:""" + caption + """

    -paragraphs:""" + paragraphs

    return prompt