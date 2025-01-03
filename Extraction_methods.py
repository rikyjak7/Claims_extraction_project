from bs4 import BeautifulSoup

# Esempio di utilizzo
def extract_claims_from_relational_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    extracted_data = []
    
    if table:
        rows = table.find_all('tr')
        
        # Estrai le intestazioni
        col_headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
        col_headers_td = [td.get_text(strip=True) for td in rows[0].find_all('td')]
        sum_col_headers = len(col_headers) + len(col_headers_td)
        if len(col_headers_td) != 0:
            col_headers.extend(col_headers_td)

        # Itera sulle righe, escludendo la riga di intestazione
        for row in rows[1:]:
            cells = row.find_all(['td', 'th'])  # Inclusi eventuali <th> nelle righe
            
            if len(cells) != sum_col_headers:
                continue  # Salta righe malformate
            
            # Combina intestazioni e celle
            row_data = [f"|{col_headers[i]}, {cells[i].get_text(strip=True)}|" for i in range(len(cells))]
            extracted_data.append(f"{', '.join(row_data)}")
    return extracted_data

def extract_claims_from_nested_relational_table(html_content):

    # Parsing HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    if not table:
        return []  # Ritorno vuoto se la tabella non esiste

    rows = table.find_all('tr')
    if not rows:
        return []  # Nessuna riga trovata

    # Determinazione delle intestazioni di colonna
    col_headers = []
    first_data_row = 1  # Default a partire dalla seconda riga
    if len(rows) > 1:
        col_headers = [th.get_text(strip=True) for th in rows[0].find_all(['th', 'td'])]
        col_headers_2nd_row = [th.get_text(strip=True) for th in rows[1].find_all(['th', 'td'])]

        if len(col_headers) != len(col_headers_2nd_row) or any(h == "" for h in col_headers):

            def_headers = []

            for i in range(max(len(col_headers),len(col_headers_2nd_row))):
                if(i < len(col_headers) and i < len(col_headers_2nd_row)):
                    def_headers.append(col_headers[i] + col_headers_2nd_row[i])
                elif(i >= len(col_headers)):
                    def_headers.append(col_headers_2nd_row[i])
                else:
                    def_headers.append(col_headers[i])

            col_headers = def_headers
            first_data_row = 2  # Salta la seconda riga se è parte delle intestazioni

    # Gestione delle celle con rowspan
    rowspan_data = {}
    extracted_data = []

    for row in rows[first_data_row:]:
        cells = row.find_all(['td', 'th'])
        row_data = []
        cell_index = 0

        for i, header in enumerate(col_headers):
            if i in rowspan_data and rowspan_data[i]['span'] > 0:

                # Usa dati esistenti da rowspan
                row_data.append(f"|{header}, {rowspan_data[i]['text']}|")
                rowspan_data[i]['span'] -= 1
            elif cell_index < len(cells):

                # Nuova cella
                cell = cells[cell_index]
                cell_text = cell.get_text(strip=True) or None  # Vuota non significa "N/A"
                row_data.append(f"|{header}, {cell_text if cell_text else ''}|")
                if cell.has_attr('rowspan'):
                    rowspan_data[i] = {'text': cell_text, 'span': int(cell['rowspan']) - 1}
                cell_index += 1
            else:

                # Cella mancante
                row_data.append(f"|{header}, |")  # Mantenere il campo vuoto

        extracted_data.append(row_data)

    # Fusione delle righe mancanti basata su logica di eredità
    merged_data = []
    for i, current_row in enumerate(extracted_data):
        if i > 0:
            previous_row = merged_data[-1]
            for j in range(len(current_row)):
                
                # Mantieni vuoto se non c'è una dipendenza di rowspan
                if "N/A" in current_row[j] or current_row[j].endswith(", |") and j in rowspan_data:
                    current_row[j] = previous_row[j]
        merged_data.append(", ".join(current_row))

    return merged_data