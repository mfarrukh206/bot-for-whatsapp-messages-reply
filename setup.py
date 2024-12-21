from chrome_profile import create_chrome

    
def login():
    driver = create_chrome()
    driver.get("https://web.whatsapp.com/")
    input("Press Enter after logging in")

login()