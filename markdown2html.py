# imports

import os.path
import re
import sys
import shutil
import uuid
import markdown
import subprocess
from bs4 import BeautifulSoup
from slugify import slugify

# global vars

article_name = ""
output_programs = ""
index_hrefs = []
output_soup = ""
output_html = ""

# functions

def reformater_html(code_html):
    soup = BeautifulSoup(code_html, 'html.parser')
    return soup.prettify()

def find_programs_get_program_param(program_param, lines, i):
    program_start = i + 1
    j = 0
    while j < len(program_param):
        for key_param in program_param:
            if lines[program_start + j].startswith(key_param):
                valeur = lines[program_start + j][len(key_param):].strip()
                if valeur != '':
                    program_param[key_param] = valeur
        j += 1
    return(program_start + j)

def find_programs_convert_inline_code(program_param, lines, program_end):
    html_code = ''
    code = ''
    code_debut = program_end
    j = 0
    while True:
        try:
            if not lines[code_debut + j]: break
        except IndexError:
            html_code = "error : end of inline program not found..."
            break        
        if '<!-- program>' in lines[code_debut + j]:
            html_code = "error : other start of inline program found..."
            break
        if '<program -->' in lines[code_debut + j]:
            break
        if lines[code_debut + j] != '':
            code += lines[code_debut + j]
        j += 1
    if html_code == "":
        echo_command = ["echo", code]        
        if program_param['number:'] == '0':                        
            option_number = f"full,style={program_param['theme:']}"                        
        else:                        
            option_number = f"full,style={program_param['theme:']},linenos=1"
        pygmentize_command = [
            "pygmentize",
            "-f",
            "html",
            "-l",
            f"{program_param['langage:']}",
            "-O",
            f"{option_number}"
        ]
        with subprocess.Popen(echo_command, stdout=subprocess.PIPE) as echo_proc:
            with subprocess.Popen(pygmentize_command, stdin=echo_proc.stdout, stdout=subprocess.PIPE) as pygmentize_proc:
                subprocess_output, _ = pygmentize_proc.communicate()
        return(subprocess_output.decode("utf-8"))

def find_programs_convert_file_code(program_param):
    html = f"{article_name}/{program_param['code:']}"
    check_file = os.path.isfile(html)
    if check_file:
        if program_param['number:'] == '0':
            option_number = f"full,style={program_param['theme:']}"
        else:
            option_number = f"full,style={program_param['theme:']},linenos=1"
        pygmentize_command =\
            "pygmentize "+\
            "-f "+\
            "html "+\
            "-l "+\
            f"{program_param['language:']} "+\
            "-O "+\
            f"{option_number} "+\
            f"{article_name}/{program_param['code:']}"
        return(subprocess.getoutput(pygmentize_command))    
    else:        
        return(f"error : , {article_name}/{program_param['code:']} no exist")

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

def find_programs():
    global article_name
    global output_programs
    with open(f"{article_name}/article.md", 'r') as f:
        lines = f.readlines()
    cpt_program = 0
    for i, line in enumerate(lines):
        if line.startswith('<!-- program>'):
            cpt_program += 1            
            program_param = {
                'number:':'',
                'number-color:':'',
                'number-background-color:':'',
                'number-border:':'',
                'number-border-radius:':'',
                'number-padding-left-right:':'',
                'number-margin-left:':'',
                'number-margin-right:':'',
                'number-font-weight:':'',
                'box-background:':'',
                'box-border:':'',                 
                'box-border-radius:':'',
                'box-shadow:':'',
                'box-font-size:':'',
                'box-font-family:':'',
                'box-line-height:':'',
                'box-width:':'',
                'box-height:':'',
                'box-margin-top:':'',
                'box-margin-bottom:':'',
                'box-margin-left:':'',
                'box-margin-right:':'',
                'language:':'',
                'theme:':'',
                'code:':''
            }
            program_end = find_programs_get_program_param(program_param, lines, i)
            if program_param['code:'] == "":
                html_code = find_programs_convert_inline_code(program_param, lines, program_end)                                        
            else:
                html_code = find_programs_convert_file_code(program_param)
            if not html_code.startswith('error'):
                html_code = find_programs_format_html_code(program_param, html_code)                
                html_code = html_code.replace('<body>', '')
                html_code = html_code.replace('</body>', '')
                html_code = html_code.replace('</html>', '')
                html_code = html_code.replace('</head>', '')
                identifiant_unique = uuid.uuid4()                
                html_code = re.sub(r'^body', f".highlight-{identifiant_unique}", html_code, flags=re.MULTILINE)
                html_code = html_code.replace('class="highlight"', f'class="highlight-{identifiant_unique}"')
                html_code = html_code.replace('.normal', f".normal-{identifiant_unique}")
                html_code = html_code.replace('class="normal"', f'class="normal-{identifiant_unique}"')
            output_programs += html_code
        output_programs += line
    print(f"Number of tags <program> found : {cpt_program}")

def find_hrefs():
    global output_soup
    global article_name
    global output_html
    output_soup = BeautifulSoup(output_html, 'html.parser')
    print("Conversion of tags <h3> to <a href>")
    for h3 in output_soup.find_all("h3"):
        balise_section = output_soup.new_tag("section")
        balise_section.string = h3.string
        slugify_title = slugify(h3.string)
        balise_section.attrs['id'] = slugify_title
        h3.replace_with(balise_section)
        ahref = f"<a href='{article_name}/article.html#{slugify_title}' target='iframe_main_content' class='custom-link-list-index' onclick='click_index()'>{h3.string}</a>"
        index_hrefs.append(ahref)
    print("Converting internal links to index starting with the character '-'")
    print("Modifying external links to open in a new tab")
    for a in output_soup.find_all("a", href=True):
        try:        
            if a.string.startswith('-'):
                index_hrefs.append(f"<a href='{article_name}/{a['href']}' target='iframe_main_content'  class='custom-link-list-index' onclick='click_index()'>{a.string.lstrip('-')}</a>")
                new_tag = output_soup.new_tag('span')
                new_tag.string = a.string.lstrip("-")
                a.replace_with(new_tag)
            href = a.get('href')
            if href.startswith('http'):
                if 'https' in href:
                    a['target'] = '_blank'                    
        except AttributeError:            
            print("'NoneType' object has no attribute 'startswith'")
            print("=> if a.string.startswith('-'):")

def update_md_file(arg_md_file: str) -> bool:
	global article_name
	path, extension = os.path.splitext(arg_md_file)	
	os.makedirs(path, exist_ok=True)
	shutil.copy(arg_md_file, f"{path}/article.md")
	print(f"Source file {arg_md_file}")
	print(f"Destination file {path}/article.md")
	article_name = path

# main

if len( sys.argv ) > 1:
    if update_md_file(sys.argv[1]):
        print("The Markdown file does not exist")
        exit(1)
else:
    print("The Markdown file is missing")
    exit(1)
        
print("Search for code sections related to <program>")
find_programs()
print("Conversion from Markdown to HTML")
output_html = markdown.markdown(output_programs, extensions=['fenced_code', 'codehilite'])
print("Creation and search for links for creating an index")
find_hrefs()
print("Saving the index section.html")
file1 = open(f"{article_name}/sections.html", "w")
for i in index_hrefs:
    file1.write(i + '\n')
file1.close()
print("Loading the markdown2html.css file")
with open('markdown2html.css', 'r') as fichier:
    style_html = fichier.read()
print("Loading the markdown.css file")

with open('markdown.css', 'r') as fichier:
    style_markdown = fichier.read()
javascript = "<script>\n"+\
    "window.addEventListener('DOMContentLoaded', function() {\n"+\
        "var links = document.getElementsByTagName('a');\n"+\
        "for (var i = 0; i < links.length; i++) {\n"+\
            "links[i].addEventListener('click', function(event) {\n"+\
                "var link = event.target.href;\n"+\
                "if (link.includes('#')) {\n"+\
                    "event.preventDefault();\n"+\
                    "window.parent.postMessage({type: 'linkClicked', link: link}, '*');\n"+\
                "}\n"+\
            "});\n"+\
        "}\n"+\
    "});\n"+\
    "</script>\n"
print("Creation of the HTML file")
fichier_html =  "<!DOCTYPE html>"+\
    "<html lang='fr'>"+\
        "<head>"+\
            "<meta charset='UTF-8' />"+\
            "<meta name='viewport' content='width=device-width'>"+\
            "<style>"+\
                f"{style_html}{style_markdown}"+\
            "</style>"+\
        "</head>"+\
        "<body>"+\
			f"{output_soup.prettify()}"+\
        "</body>"+\
        f"{javascript}"+\
    "</html>"

print("Save the html file article.html")
file1 = open(f"{article_name}/article.html", "w")
file1.write(reformater_html(fichier_html))
file1.close()
exit(0)
