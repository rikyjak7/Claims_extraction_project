from bs4 import BeautifulSoup

def extractclaims_from_relational_table(html_content):    
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')    
    extracted_data = []
    if table:
        rows = table.find_all('tr')
        col_headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
        for row in rows[1:]:
            cells = row.find_all('td')
            row_data = [f"|{col_headers[i]}, {cells[i].get_text(strip=True)}|" for i in range(len(cells))]
            extracted_data.append(f"{{{', '.join(row_data)}}}")
            return extracted_data

