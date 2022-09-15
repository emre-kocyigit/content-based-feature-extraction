from bs4 import BeautifulSoup

with open("mini_dataset/1.html") as f:
    test = f.read()

soup = BeautifulSoup(test, "html.parser")


# has_title
def has_title(soup):
    if len(soup.title.text) > 0:
        return 1
    else:
        return 0


# has_input
def has_input(soup):
    if len(soup.find_all("input")):
        return 1
    else:
        return 0


# has_button
def has_button(soup):
    if len(soup.find_all("button")) > 0:
        return 1
    else:
        return 0


# has_image
def has_image(soup):
    if len(soup.find_all("image")) == 0:
        return 0
    else:
        return 1


# has_submit
def has_submit(soup):
    for button in soup.find_all("input"):
        if button.get("type") == "submit":
            return 1
        else:
            pass
    return 0


# has_link
def has_link(soup):
    if len(soup.find_all("link")) > 0:
        return 1
    else:
        return 0


# has_password
def has_password(soup):
    for input in soup.find_all("input"):
        if (input.get("type") or input.get("name") or input.get("id")) == "password":
            return 1
        else:
            pass
    return 0


# has_email_input
def has_email_input(soup):
    for input in soup.find_all("input"):
        if (input.get("type") or input.get("id") or input.get("name")) == "email":
            return 1
        else:
            pass
    return 0


# has_hidden_element
def has_hidden_element(soup):
    for input in soup.find_all("input"):
        if input.get("type") == "hidden":
            return 1
        else:
            pass
    return 0


# has_audio
def has_audio(soup):
    if len(soup.find_all("audio")) > 0:
        return 1
    else:
        return 0


# has_video
def has_video(soup):
    if len(soup.find_all("video")) > 0:
        return 1
    else:
        return 0


# number_of_inputs
def number_of_inputs(soup):
    return len(soup.find_all("input"))


# number_of_buttons
def number_of_buttons(soup):
    return len(soup.find_all("button"))


# number_of_images
def number_of_images(soup):
    image_tags = len(soup.find_all("image"))
    count = 0
    for meta in soup.find_all("meta"):
        if meta.get("type") or meta.get("name") == "image":
            count += 1
    return image_tags + count


# number_of_option
def number_of_option(soup):
    return len(soup.find_all("option"))


# number_of_list
def number_of_list(soup):
    return len(soup.find_all("li"))


# number_of_TH
def number_of_TH(soup):
    return len(soup.find_all("th"))


# number_of_TR
def number_of_TR(soup):
    return len(soup.find_all("tr"))


# number_of_href
def number_of_href(soup):
    count = 0
    for link in soup.find_all("link"):
        if link.get("href"):
            count += 1
    return count


# number_of_paragraph
def number_of_paragraph(soup):
    return len(soup.find_all("p"))


# number_of_script
def number_of_script(soup):
    return len(soup.find_all("script"))


# length_of_title
def length_of_title(soup):
    return len(soup.title.text)


print("has_title --> ", has_title(soup))
print("has_input --> ", has_input(soup))
print("has_button --> ", has_button(soup))
print("has_image --> ", has_image(soup))
print("has_submit --> ", has_submit(soup))
print("has_link --> ", has_link(soup))
print("has_password --> ", has_password(soup))
print("has_email_input --> ", has_email_input(soup))
print("has_hidden_element --> ", has_hidden_element(soup))
print("has_audio --> ", has_audio(soup))
print("has_video --> ", has_video(soup))
print("number_of_inputs --> ", number_of_inputs(soup))
print("number_of_buttons --> ", number_of_buttons(soup))
print("number_of_images --> ", number_of_images(soup))
print("number_of_option --> ", number_of_option(soup))
print("number_of_list --> ", number_of_list(soup))
print("number_of_TH --> ", number_of_TH(soup))
print("number_of_TR --> ", number_of_TR(soup))
print("number_of_href --> ", number_of_href(soup))
print("number_of_paragraph --> ", number_of_paragraph(soup))
print("number_of_script --> ", number_of_script(soup))
print("length_of_title --> ", length_of_title(soup))









