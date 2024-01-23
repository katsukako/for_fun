import markdown, time, re

# read .md file
def read_file(link="../diary_new.md"):
    path =input(f"now {link} to enter to go or new path:")
    link = path if path else link 
    with open(link, "r", encoding="utf-8") as file:
        show_html = markdown.markdown(file.read())
    return show_html

# delete html tags
def delete_blocks(text):
    print("starting...")
    html_rule = re.compile(r"<.*?>")
    return re.sub(html_rule, "", text)

# show with 'animation'
def show(clean_text):
    speed = input('how fast? input a num:')
    for content in clean_text:
        print(content, end="")
        time.sleep(float(speed))

def main():
    file = read_file()
    text = delete_blocks(file)
    show(text)

while True:
    try:
        print()
        main()
        print()
    except KeyboardInterrupt as err:
        print("exit")
        break


