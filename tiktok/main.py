from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def browser(quantity_emails, region):
    try:
        print("Started")
        for email in range (quantity_emails):
            driver = webdriver.Edge()
            driver.get("https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1681686151&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d00d6cef6-bf18-ba2c-f681-06c66163b1af&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=719e0612c5c04c6e94c64b4e0acd40ea")
            mail_label = driver.find_element(By.NAME, "MemberName")
            mail_label.send_keys("email_name")
    except Exception as e:
        print(f"Error: {e}")


