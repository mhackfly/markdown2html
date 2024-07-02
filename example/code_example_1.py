def find_programs_format_html_code(program_param, html_code):

    div_highlight_style =\
        "overflow: auto;"+\
        f"height: {program_param['box-height:']};"+\
        f"border-radius: {program_param['box-border-radius:']};"+\
        f"width: {program_param['box-width:']};"+\
        "margin: auto;"+\
        f"border: {program_param['box-border:']};"+\
        f"background: {program_param['box-background:']};"+\
        f"box-shadow: {program_param['box-shadow:']};"

    td_linenos_style = "td.linenos .normal {"+\
                        f"color: {program_param['number-color:']};"+\
                        f"background-color: {program_param['number-background-color:']};"+\
                        f"border: {program_param['number-border:']};"+\
                        f"border-radius: {program_param['number-border-radius:']};"+\
                        f"padding-left: {program_param['number-padding-left-right:']};"+\
                        f"padding-right: {program_param['number-padding-left-right:']};"+\
                        f"margin-left: {program_param['number-margin-left:']};"+\
                        f"margin-right: {program_param['number-margin-right:']};"+\
                        f"font-weight: {program_param['number-font-weight:']};"+\
                        "}"

    html_lignes = html_code.splitlines()

    for i, ligne in enumerate(html_lignes):
        if ligne.startswith('pre {'):
            del html_lignes[:i]
            break

    html_lignes[0] = "<style>"
    
    html_lignes[1] = td_linenos_style
    html_code = "\n".join(html_lignes)
    
    soup = BeautifulSoup(html_code, 'html.parser')
    
    highlight_div = soup.find('div', attrs={'class': 'highlight'})

    if highlight_div:
        highlight_div['style'] = div_highlight_style

    html_code = soup.prettify()
    
    soup = BeautifulSoup(html_code, 'html.parser')
    
    balises_pre = soup.find_all('pre')

    for balise in balises_pre:

        balise['style'] = f"line-height: {program_param['box-line-height:']};"+\
                            f"margin-top: {program_param['box-margin-top:']};"+\
                            f"margin-bottom: {program_param['box-margin-bottom:']};"+\
                            f"margin-left: {program_param['box-margin-left:']};"+\
                            f"margin-right: {program_param['box-margin-right:']};"+\
                            f"font-family: {program_param['box-font-family:']};"+\
                            f"font-size: {program_param['box-font-size:']};"+\
                            "padding: 0;"

        if program_param['number:'] == '1':
            balise['style'] += "width: max-content;"

    html_code = soup.prettify()
    
    return(html_code)

