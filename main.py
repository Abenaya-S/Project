#Main.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from Test_Data.data import Employee_Data
from Test_Locators.locators import Employee_Locators


class Employee:
        
    
    
    def login(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(Employee_Data().url)
        sleep(2)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().username_locator).send_keys(Employee_Data().username)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().password_locator).send_keys(Employee_Data().password1)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().submitBox_locator).click()
        sleep(7)
        print('The user is logged in successfully')
        self.driver.quit()

    def invalidlogin(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(Employee_Data().url)
        sleep(2)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().username_locator).send_keys(Employee_Data().username)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().password_locator).send_keys(Employee_Data().password2)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().submitBox_locator).click()
        sleep(7)
        print('Invalid credentials')
        self.driver.quit()

    def addemployee(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(Employee_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().username_locator).send_keys(Employee_Data().username)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().password_locator).send_keys(Employee_Data().password1)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().submitBox_locator).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Pimmodulebutton_locator).click()
        sleep(6)
        self.driver.find_element(by=By.LINK_TEXT, value=Employee_Locators().AddEmployee_locator).click()
        sleep(3)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().Firstname_locator).send_keys(Employee_Data().firstName)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().Middlename_locator).send_keys(Employee_Data().middleName)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().Lastname_locator).send_keys(Employee_Data().lastName)
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().saveBox_locator).click()
        sleep(7)
        print('Employee successfully added')
        self.driver.quit()

    def editemployeedetails(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(Employee_Data().url)
        sleep(2)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().username_locator).send_keys(Employee_Data().username)
        self.driver.find_element(by=By.NAME, value=Employee_Locators().password_locator).send_keys(Employee_Data().password1)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().submitBox_locator).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Pimmodulebutton_locator).click()
        sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value=Employee_Locators().Employeelist_locator).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Employeename_locator).send_keys(Employee_Data().Employeename)
        sleep(6)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Searchbutton_locator).click()
        sleep(4)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Editbutton_locator).click()
        sleep(10)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Nickename_locator).send_keys(Employee_Data().Nickname)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().otherid_locator).send_keys(Employee_Data().otherid)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Drivinglicensenumber_locator).send_keys(Employee_Data().Drivinglicensenumber)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().LicenseExpiryDate_locator).send_keys(Employee_Data().LicenseExpiryDate)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().SSNNumber_locator).send_keys(Employee_Data().SSNNumber)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().SINNumber_locator).send_keys(Employee_Data().SINNumber)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().MilitaryService_locator).send_keys(Employee_Data().MilitaryServiceBox)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().GenderBox_locator).click()
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Dateofbirth_locator).send_keys(Employee_Data().Dateofbirth)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Save1_locator).click()
        self.driver.find_element(by=By.XPATH, value=Employee_Locators().Save2_locator).click()
        sleep(7)
        print('Employee details successfully edited')
        self.driver.quit()




    def deleteemployeedetails(self):
          self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          self.driver.maximize_window()
          self.driver.get(Employee_Data().url)
          sleep(3)
          self.driver.find_element(by=By.NAME, value=Employee_Locators().username_locator).send_keys(Employee_Data().username)
          self.driver.find_element(by=By.NAME, value=Employee_Locators().password_locator).send_keys(Employee_Data().password1)
          self.driver.find_element(by=By.XPATH, value=Employee_Locators().submitBox_locator).click()
          sleep(2)
          self.driver.find_element(by=By.XPATH, value=Employee_Locators().Pimmodulebutton_locator).click()
          sleep(3)
          self.driver.find_element(by=By.LINK_TEXT, value=Employee_Locators().Employeelist_locator).click()
          sleep(2)
          self.driver.find_element(by=By.XPATH, value=Employee_Locators().Employeename_locator).send_keys(Employee_Data().Employeename)
          self.driver.find_element(by=By.XPATH, value=Employee_Locators().Searchbutton_locator).click()
          sleep(2)
          self.driver.find_element(by=By.XPATH, value=Employee_Locators().Selectbutton_locator).click()
          sleep(1)
          self.driver.find_element(by=By.XPATH, value=Employee_Locators().Deletebutton1_locator).click()
          sleep(2)
          self.driver.find_element(by=By.XPATH, value=Employee_Locators().Deletebutton2_locator).click()
          sleep(7)
          print('Employee successfully deleted')
          self.driver.quit()




Abe = Employee()

Abe.login()

Abe.invalidlogin()

Abe.addemployee()

Abe.editemployeedetails()

Abe.deleteemployeedetails()

while(True):
   pass


