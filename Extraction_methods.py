from bs4 import BeautifulSoup

def extract_claims_from_relational_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    extracted_data = []
    
    if table:
        rows = table.find_all('tr')
        
        # Estrai le intestazioni
        col_headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
        
        # Itera sulle righe, escludendo la riga di intestazione
        for row in rows[1:]:
            cells = row.find_all(['td', 'th'])  # Inclusi eventuali <th> nelle righe
            if len(cells) != len(col_headers):
                continue  # Salta righe malformate
            
            # Combina intestazioni e celle
            row_data = [f"|{col_headers[i]}, {cells[i].get_text(strip=True)}|" for i in range(len(cells))]
            extracted_data.append(f"{{{', '.join(row_data)}}}")

        #extracted_data in input al LLM con LLM_Extraction_Prompt per generare i claims corretti


    
    return extracted_data

# Test del codice
html_content = '''
'''

claims = extractclaims_from_relational_table(html_content)
for claim in claims:
    print(claim)