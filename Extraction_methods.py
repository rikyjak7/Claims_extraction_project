from bs4 import BeautifulSoup

# Esempio di utilizzo
html_content = '''
            <table class=\"ltx_tabular ltx_guessed_headers ltx_align_middle\" id=\"S4.T2.5.1\">\n<thead class=\"ltx_thead\">\n<tr class=\"ltx_tr\" id=\"S4.T2.5.1.1.1\">\n<th class=\"ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_tt\" id=\"S4.T2.5.1.1.1.1\">Model</th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt\" id=\"S4.T2.5.1.1.1.2\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.1.1.2.1\">L=0.5</span></th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt\" id=\"S4.T2.5.1.1.1.3\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.1.1.3.1\">L=0.2</span></th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt\" id=\"S4.T2.5.1.1.1.4\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.1.1.4.1\">L=0.1</span></th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt\" id=\"S4.T2.5.1.1.1.5\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.1.1.5.1\">L=0.05</span></th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt\" id=\"S4.T2.5.1.1.1.6\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.1.1.6.1\">L=0.02</span></th>\n</tr>\n<tr class=\"ltx_tr\" id=\"S4.T2.5.1.2.2\">\n<th class=\"ltx_td ltx_align_left ltx_th ltx_th_column ltx_th_row ltx_border_t\" id=\"S4.T2.5.1.2.2.1\">GPT2-small</th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_t\" id=\"S4.T2.5.1.2.2.2\">0.131</th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_t\" id=\"S4.T2.5.1.2.2.3\">0.135</th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_t\" id=\"S4.T2.5.1.2.2.4\">0.131</th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_t\" id=\"S4.T2.5.1.2.2.5\">0.135</th>\n<th class=\"ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_t\" id=\"S4.T2.5.1.2.2.6\">0.132</th>\n</tr>\n</thead>\n<tbody class=\"ltx_tbody\">\n<tr class=\"ltx_tr\" id=\"S4.T2.5.1.3.1\">\n<th class=\"ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t\" id=\"S4.T2.5.1.3.1.1\">GPT2-small-</th>\n<td class=\"ltx_td ltx_border_t\" id=\"S4.T2.5.1.3.1.2\"/>\n<td class=\"ltx_td ltx_border_t\" id=\"S4.T2.5.1.3.1.3\"/>\n<td class=\"ltx_td ltx_border_t\" id=\"S4.T2.5.1.3.1.4\"/>\n<td class=\"ltx_td ltx_border_t\" id=\"S4.T2.5.1.3.1.5\"/>\n<td class=\"ltx_td ltx_border_t\" id=\"S4.T2.5.1.3.1.6\"/>\n</tr>\n<tr class=\"ltx_tr\" id=\"S4.T2.5.1.4.2\">\n<th class=\"ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb\" id=\"S4.T2.5.1.4.2.1\">share-encoder</th>\n<td class=\"ltx_td ltx_align_center ltx_border_bb\" id=\"S4.T2.5.1.4.2.2\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.4.2.2.1\">0.248</span></td>\n<td class=\"ltx_td ltx_align_center ltx_border_bb\" id=\"S4.T2.5.1.4.2.3\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.4.2.3.1\">0.265</span></td>\n<td class=\"ltx_td ltx_align_center ltx_border_bb\" id=\"S4.T2.5.1.4.2.4\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.4.2.4.1\">0.264</span></td>\n<td class=\"ltx_td ltx_align_center ltx_border_bb\" id=\"S4.T2.5.1.4.2.5\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.4.2.5.1\">0.255</span></td>\n<td class=\"ltx_td ltx_align_center ltx_border_bb\" id=\"S4.T2.5.1.4.2.6\"><span class=\"ltx_text ltx_font_bold\" id=\"S4.T2.5.1.4.2.6.1\">0.251</span></td>\n</tr>\n</tbody>\n</table>\n\n
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

