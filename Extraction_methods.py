from bs4 import BeautifulSoup

# Esempio di utilizzo
html_content = '''
'''
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
            extracted_data.append(f"{{{', '.join(row_data)}}}")

        #extracted_data in input al LLM con LLM_Extraction_Prompt per generare i claims corretti

    return extracted_data

claims = extract_claims_from_relational_table(html_content)
for claim in claims:
    print(claim)

