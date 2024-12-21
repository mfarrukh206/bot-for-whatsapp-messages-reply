from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import random
from chrome_profile import create_chrome
from auto_reply_dict import auto_reply_messages

class WhatsappBot:

    def __init__(self, url):
        self.driver = create_chrome()
        self.driver.get(url)
        print("Bot is running...")

    def check_for_new_messages(self):
        try:
            unread_chats = self.driver.find_elements(By.XPATH, '//span[contains(@aria-label, "unread message")]')
            
            if unread_chats:
                unread_chats[1].click()
                print("Clicked on unread chat.")
                time.sleep(3)
                self.process_message()
            else:
                print("No unread messages.")
                
        except Exception as e:
            print(f"Error checking for new messages: {e}")

    def process_message(self):
        try:
            message_row = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="row"]')[-1]
            try:
                message = message_row.find_element(By.CSS_SELECTOR, '.message-in .copyable-text')
            except:
                return False
            
            last_message = message.text.lower()

            response = auto_reply_messages.get(last_message, "Sorry, I didn't understand that.")


            # if "hello" in last_message.lower():
            #     response = "Hi there!"
            # elif "hi" in last_message.lower():
            #     response = "Hello! "
            # elif "how are you" in last_message.lower():
            #     response = "I'm doing well, thank you!"
            # elif "ok" in last_message.lower():
            #     response = "Ok, thank you!"
            # elif "bye" in last_message.lower() or "by" in last_message.lower():
            #     response = "Bye! See you soon!"
            # elif "whats up" in last_message.lower():
            #     response = "Nothing much, just hanging out!"
            # else:
            #     response = "Sorry, I didn't understand that."

            self.send_reply(response)

        except Exception as e:
            print(f"Error processing message: {e}")

    def send_reply(self, response):
        try:
            message_box = self.driver.find_element(By.XPATH, '//div[@aria-placeholder="Type a message"]')
            
            self.driver.execute_script("arguments[0].focus();", message_box)
            
            message_box.send_keys(response)
            message_box.send_keys(Keys.ENTER)
            print(f"Auto-reply sent: {response}")
            message_box.send_keys(Keys.ESCAPE)
        except Exception as e:
            print(f"Error replying to message: {e}")


    def run(self):
        while True:
            self.check_for_new_messages()
            time.sleep(5)


bot = WhatsappBot("https://web.whatsapp.com/")


bot.run()

input("Press Enter to Exit..")
