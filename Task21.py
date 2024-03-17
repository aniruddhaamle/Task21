from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class LoginAutomation:
    """
    This class is used to login into https://www.saucedemo.com/
    """

    def __init__(self, url="https://www.saucedemo.com/", username="standard_user", password="secret_sauce"):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        """
        This method is used to open the browser and go to https://www.saucedemo.com/ .
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(3)
        obj1.print_cookies()
        sleep(3)

    def quit(self):
        sleep(50)
        self.driver.quit()

    def Logout(self):
        sleep(3)
        self.driver.find_element(by=By.ID, value="react-burger-menu-btn").click()
        sleep(3)
        self.driver.find_element(by=By.ID, value="logout_sidebar_link").click()
        sleep(3)
        obj1.print_cookies()


    def login(self):
        """
        This method is used to login to https://www.saucedemo.com/ .
        """
        self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
        sleep(2)
        self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
        sleep(2)
        self.driver.find_element(by=By.ID, value="login-button").click()
        sleep(2)
        if self.driver.current_url == "https://www.saucedemo.com/inventory.html":
            print("Login Successful")
        else:
            print("Login Unsuccessful")
        sleep(3)
        obj1.print_cookies()

    def getTitle(self):
        """
        This method is used to get the Title of the current page.
        """
        print("Title of webpage is :" + self.driver.title)

    def getCurrentURL(self):
        """
        This method is used to get the url of the current page.
        """
        print("Current URL is :" + self.driver.current_url)

    def extract_content(self):
        """
        This method is used to extract of the current page and save it in text file.
        """
        results = self.driver.find_elements(By.XPATH, "//*[@id='root']")  # extract page content into list
        for result in results:
            listToStr = result.text.split()
            print(listToStr)
            listToStr = ' '.join(map(str, listToStr))  # Convert list to string
            # save it to a file
            with open("results.txt", "w") as f:
                f.write(listToStr)

    def print_cookies(self):
        print(self.driver.get_cookies())


obj1 = LoginAutomation()
obj1.boot()
obj1.login()
# obj1.getTitle()
# obj1.getCurrentURL()
# obj1.extract_content()
obj1.Logout()
obj1.quit()

