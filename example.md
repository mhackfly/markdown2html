### Description

<br/>

> **`markdown2html.py`** is a Python script that converts a Markdown file to HTML.
>> - it transforms **`<h3>`** tags into **`<a href>`** tags by creating sections with unique identifiers and adds these anchors in a **`sections.html` file **. In this index file you can add links to files by inserting the '-' sign in front of the file name:
Examples: **```[-my PDF](document.pdf), [-my html](file.html), [-my text](document.txt), [-my code](code.py) ```**
>> - it identifies special code blocks delimited by **`<!--program>`** and **`<program -->`**
These blocks define a code display area with [attributes](#program-tags) and highlight them with **`pygmentize`**
a code syntax highlighting tool.
>> - it creates the HTML file by integrating the files **`markdown2html.css`** and **`markdown.css`**
>>> - **`markdown2html.css`** defines the style of the HTML page
>>> - **`markdown.css`** defines styles for the markdown file

<br/>

### Usage

<br/>

> Create a directory with the files **`markdown2html.py, markdown2html.css, markdown.css`**  
> Run the Python file with your Markdown file:  
> **`python3 markdown2html.py my_file.md`**  
> A directory **`my_file`** is created, with 3 files inside:  
> **`article.html:`** the main HTML file.  
> **`article.md:`** a copy of the Markdown file.  
> **`sections.html:`** an index of links created with the tags `### and [-...]()`.  
> You can optionally modify the CSS files.  

<br/>

### Dependencies

<br/>

> Pygments:  
> [Download and install](https://pygments.org/download/) or with **`pip install Pygments`**  
> <sm>(Usage example: pygmentize -S paraiso-dark -f html -a .codehilite)</sm>  

<br/>

### Source code

<br/>


> [markdown2html.py](code_markdown2html.py.html): converts the Markdown file to HTML  
> [markdown2html.css](code_markdown2html.css.html): defines the style of the HTML page  
> [markdown.css](code_markdown.css.html): defines styles for the markdown file  
> <sm>(Theme code: Dracula)</sm>  

<br/>

### Program tags

<br/>

> Attributes must be placed between 2 tags **`<!-- program> <program -->`**  
> The first set of **`number-...`** attributes customizes the line numbers.  
> The series **`box-...`** the box and the code.  
> the last attributes in the list **`language`** and **`theme`** correspond to the options  
> from **`pygmentize`**, [languages](https://pygments.org/languages/) and [styles](https://pygments.org/styles/).  
> In the **`<Program> tags`** section, when specifying the **`code`** attribute,  
> you can either provide the name of an existing file or write the code directly.  
> For example, **`code: code_example_1.py`** assumes that **`code_example_1.py`**  
> is an existing file in the same directory.  
> If you want to write the code directly, you can do so as follows:  

> `<!-- program>`  
> `...`  
> `language: python`  
> `theme: fruity`  
> `code:`  
> `print("Hello")`  
> `print("World!")`  
> `<program -->`  
> or  
> `<!-- program>`  
> `...`  
> `language: js`  
> `theme: github-dark`  
> `code: script.js`  
> `<program -->`  

> In the "Examples" section, many attributes are listed without values.  
> These attributes are optional and are used to customize the appearance of the code block.  
> If an attribute is not specified, the program will use default values.  
> You can experiment with different values to achieve the desired look for your code block.  

<br/>

> #### Some examples

<br/>

>> #### 1 )
>>> box-shadow: inset 10px 10px 10px rgba(0,0,0,.7);  
>>> box-font-size: 10px  
>>> box-font-family: Source Code Pro  
>>> theme: fruity  

<br/>

```
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background: #171932;
box-border:
box-border-radius: 10px
box-shadow: inset 10px 10px 10px rgba(0,0,0,.7);
box-font-size: 10px
box-font-family: Source Code Pro
box-line-height: 120%
box-width: 80%
box-height: 300px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: fruity
code: code_example_1.py
```

<br/>

<!-- program>
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background: #171932;
box-border:
box-border-radius: 10px
box-shadow: inset 10px 10px 10px rgba(0,0,0,.7);
box-font-size: 10px
box-font-family: Source Code Pro
box-line-height: 120%
box-width: 80%
box-height: 300px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: fruity
code: code_example_1.py
<program -->

<br/>

>> #### 2 )
>>> box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;  
>>> box-font-size: 10px  
>>> box-font-family: Source Code Pro  
>>> theme: nord-darker  

<br/>

```
number: 1
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background:
box-border:
box-border-radius: 10px;
box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
box-font-size: 10px
box-font-family: Source Code Pro
box-line-height: 120%
box-width: 80%
box-height: 300px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: nord-darker
code: code_example_1.py
```

<br/>

<!-- program>
number: 1
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background:
box-border:
box-border-radius: 10px;
box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
box-font-size: 10px
box-font-family: Source Code Pro
box-line-height: 120%
box-width: 80%
box-height: 300px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: nord-darker
code: code_example_1.py
<program -->

<br/>

>> #### 3 )
>>> box-shadow: rgba(6, 24, 44, 0.4) 0px 0px 0px 2px, rgba(6, 24, 44, 0.65) 0px 4px 6px -1px, rgba(255, 255, 255, 0.08) 0px 1px 0px inset;  
>>> box-font-size: 16px  
>>> box-font-family: Play  
>>> theme: monokai  

<br/>

```
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background:
box-border:
box-border-radius:
box-shadow: rgba(6, 24, 44, 0.4) 0px 0px 0px 2px, rgba(6, 24, 44, 0.65) 0px 4px 6px -1px, rgba(255, 255, 255, 0.08) 0px 1px 0px inset;
box-font-size: 16px
box-font-family: Play
box-line-height: 120%
box-width: 80%
box-height: 300px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: monokai
code: code_example_1.py
```

<br/>

<!-- program>
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background:
box-border:
box-border-radius:
box-shadow: rgba(6, 24, 44, 0.4) 0px 0px 0px 2px, rgba(6, 24, 44, 0.65) 0px 4px 6px -1px, rgba(255, 255, 255, 0.08) 0px 1px 0px inset;
box-font-size: 16px
box-font-family: Play
box-line-height: 120%
box-width: 80%
box-height: 300px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: monokai
code: code_example_1.py
<program -->

<br/>

>> #### 4 )
>>> box-shadow: rgba(0, 0, 0, 0.0) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;    
>>> box-font-size: 12px  
>>> box-font-family: Ubuntu Mono  
>>> theme: fruity  

<br/>

```
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background: #1B1E3B;
box-border:
box-border-radius: 10px
box-shadow: rgba(0, 0, 0, 0.0) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;
box-font-size: 12px
box-font-family: Ubuntu Mono
box-line-height: 120%
box-width: 60%
box-height: 297px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: fruity
code: code_example_1.py
```

<br/>

<!-- program>
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background: #1B1E3B;
box-border:
box-border-radius: 10px
box-shadow: rgba(0, 0, 0, 0.0) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;
box-font-size: 12px
box-font-family: Ubuntu Mono
box-line-height: 120%
box-width: 60%
box-height: 297px
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: fruity
code: code_example_1.py
<program -->

<br/>

>> #### 5 )
>>> box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;  
>>> box-font-size: 14px  
>>> box-font-family: Outfit  
>>> box-height: auto  
>>> theme: nord  

<br/>

```
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background:
box-border:
box-border-radius: 25px
box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
box-font-size: 14px
box-font-family: Outfit
box-line-height: 110%
box-width: 70%
box-height: auto
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: nord
code: code_example_1.py
```

<br/>

<!-- program>
number: 0
number-color:
number-background-color:
number-border:
number-border-radius:
number-padding-left-right:
number-margin-left:
number-margin-right:
number-font-weight:
box-background:
box-border:
box-border-radius: 25px
box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
box-font-size: 14px
box-font-family: Outfit
box-line-height: 110%
box-width: 70%
box-height: auto
box-margin-top: 10px
box-margin-bottom: 10px
box-margin-left: 10px
box-margin-right: 10px
language: python
theme: nord
code: code_example_1.py
<program -->

<br/>

