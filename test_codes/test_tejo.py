from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from test_locators import locators
from test_data import data
import pytest


class Test_HRM :
   
    # Generator function
    @pytest.fixture
    def booting_functions (self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
   
   
# Test Login
    def test_Browsing(self,booting_function):
       from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from test_locators import locators
from test_data import data
import pytest


class Test_HRM :
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
   
   
# Test Login
    def test_Browsing(self,booting_function):
       self.driver.get(data.Orange_Data().url)
       self.driver.maximize_window()
       sleep(10)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locator().username_locator).send_keys(data.Orange_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locator().password_locator).send_keys(data.Orange_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locator().submitButton_locator).click()
      
#TO select PIM_MODULE    
       sleep(10)
       self.driver.find_element(by=By . XPATH, value=locators.Orange_Locator().PIM_CNT).click()
#TO Select EXISTING EMPLYOEE
       sleep(10)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locator().edit_employee).click() 
       sleep(10)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locator().name).send_keys(data.Orange_Data().middle_name) 
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locator().save).click()     
         
#TO ADD AN EMPLOYEE TO LIST        
       sleep(10) 
       self.driver.find_element(by=By. XPATH, value=locators.Orange_Locator().Add_employee).click()
    
       sleep(10)    
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locator().first_input).send_keys(data.Orange_Data().firsy_name)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locator(). second_input).send_keys(data.Orange_Data().second_name)
       self.driver.find_element(by=By.NAME, value=locators.Orange_Locator().last_input).send_keys(data.Orange_Data().last_name)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locator().save_details).click() 
         
#TO DELETE AN EMPLYOEE FROM EXISTING LIST    
       sleep(10)
       self.driver.find_element(by=By.XPATH, value=locators.Orange_Locator().emplyoee_list).click() 
    
       sleep(10)
       self.driver.find_element(by=By.XPATH,value=locators.Orange_Locator().delete).click()
       self.driver.find_element(by=By.XPATH,value=locators.Orange_Locator().pop_up).click()
        
       assert self.driver.title != 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
       print("SUCCESSFULLY : LOGGED ,ADDED EMPLYOEE, EDITED EMPLYOEE, DELETED AN EMPLYOEE OF OrangeHRM")

    
 
      

      