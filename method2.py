print ("Belajar Argument List")

def create_html (tag, text, **attributes) :
    html = f"<{tag}"

    for key, velue in attributes.items():
        html = html + f" {key}='{velue}'"

    html = html + f">{text}</{tag}>"
    return html

html = create_html ("p", "hello phyton", style="paragraf")
print (html)
html = create_html ("a", "ini link", href="www.inisiator.com", style="link")
print (html)
html = create_html ("div", "ini div", style="contoh tambahan")
print (html)

