from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from pynput.keyboard import Key, Controller
chromedriver="F:\Python 3.8.3\chromedriver_win32\chromedriver"
keyboard=Controller()



def option1():
    username=input("Enter your username: ")
    password=input("Enter your Password: ")
    number_of_post=int(input("Enter the number of posts to be liked and commented: "))
    hash=input("Enter the hashtag: ")
    driver=webdriver.Chrome(chromedriver)
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(username)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()   #Not Now
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()    #Not Now
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("#"+hash)      # inputing the hash
    time.sleep(5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(8)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a').click()    #clicking the first post
    time.sleep(3)
    number_of_post=(number_of_post-1)*2
    number_of_post+=1
    for i in range(1,number_of_post):
        if(i>1 and i%2==1):
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
            time.sleep(3)
            continue
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div').click()  #liking the post
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()   # clicking the comment area
        time.sleep(2)

        keyboard.type("Hey , I have started a new page on IG. I need your support to grow it. Please Follow me !")

        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(3)
        if i==1:
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
            time.sleep(2)
        else:
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
            time.sleep(2)
        time.sleep(6)


def option2():
    username=input("Enter your username: ")
    password=input("Enter your Password: ")
    target_username=input("Enter the target username: ")
    number_of_post=int(input("Enter the number of posts to be liked and commented: "))
    comment=input("Enter the comment: ")
    driver=webdriver.Chrome(chromedriver)
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(username)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()   #Not Now
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()    #Not Now
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(target_username)      # inputing the username
    time.sleep(5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(8)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]').click()    #clicking the first post
    time.sleep(3)
    number_of_post=(number_of_post-1)*2
    number_of_post+=1
    for i in range(1,number_of_post):
        if(i>1 and i%2==1):
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
            time.sleep(3)
            continue
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div').click()  #liking the post
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()   # clicking the comment area
        time.sleep(2)

        keyboard.type(comment)

        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(3)
        if i==1:
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click()
            time.sleep(2)
        else:
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click()
            time.sleep(2)
        time.sleep(6)
def option3():
    username=input("Enter your username: ")
    password=input("Enter your Password: ")
    target_username=input("Enter the target username: ")
    message1=input("Enter the  message: ")
    number_of_times=int(input("Enter the number of times for the message to be sent: "))
    driver=webdriver.Chrome(chromedriver)
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(username)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()   #Not Now
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()    #Not Now
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(target_username)      # inputing the username
    time.sleep(5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(8)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/button').click()
    time.sleep(2)
    for i in range(0,number_of_times):
        keyboard.type(message1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    


print("WELCOME TESTER !")
print("This is a Menu-Driven program for Instagram Automation Bot\n")
print("Choose one option: (1 or 2) ")
print("0. Exit ")
print("1. Like and Comment on a post of a particular Hashtag .")
print("2. Like and Comment on a post of a particular username .")
print("3. Direct message to someone in loop .(This is a BETA mode)\n")
option=int(input("Enter your option: "))
print()
if option==0:
    print("You have exited the program")
    print("Thank You !")
elif option==1:
    option1()
elif option==2:
    option2()
elif option==3:
    option3()
else:
    print("Invalid Input")
