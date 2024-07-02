**Description**

`markdown2html.py` is a Python script that converts a Markdown file to HTML. It performs the following tasks:

1. It transforms `<h3>` tags into `<a href>` tags, creating sections with unique identifiers.
2. These anchors are added to a `sections.html` file.
3. In the `index` file, you can add links to other files by inserting a hyphen (`-`)
before the file name (e.g., `[-my PDF](document.pdf)`).
4. The script identifies special code blocks delimited by `<!--program>` and `<program-->`.
These blocks define code display areas with attributes and highlight the code using Pygments,
a syntax highlighting tool.
5. It creates the HTML file by integrating the `markdown2html.css` and `markdown.css` files.
6. `markdown2html.css` defines the style for the HTML page, while `markdown.css` styles the Markdown file.

**Usage**

1. Create a directory with the files `markdown2html.py`, `markdown2html.css`, and `markdown.css`.
2. Execute the Python script with your Markdown file:
   ```
   python3 markdown2html.py my_file.md
   ```
3. A directory named `my_file` will be created, containing three files:
   - `article.html`: the main HTML file.
   - `article.md`: a copy of the Markdown file.
   - `sections.html`: an index of links created using `###` and `[-...]()` tags.

**Dependency**

- Pygments: Download and install it or use `pip install Pygments`.
  Example usage: `pygmentize -S paraiso-dark -f html -a .codehilite`

**Program Tags**

- Attributes must be placed between `<!-- program> ... <program -->`.
- The first series of attributes (`number-...`) customizes line numbers.
- The `box-...` series relates to the box and code appearance.
- The last attributes in the list (`language` and `theme`) correspond to Pygments options.
- In the "tags" section, when specifying the `code` attribute, you can provide either an
existing file name or if you want to write the code directly, you can do so as follows:

<!-- program>
...
language: python
theme: fruity
code:
print("Hello")
print("World!")
<program -->

With the existing file:

<!-- program>
...
language: js
theme: github-dark
code: script.js
<program -->

**Examples**

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

In the "Examples" section, many attributes are listed without values.
These attributes are optional and are used to customize the appearance of the code block.
If an attribute is not specified, the program will use default values.
You can experiment with different values to achieve the desired look for your code block.

Feel free to experiment with different values for your code block appearance! 😊

