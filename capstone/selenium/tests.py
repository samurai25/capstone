from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import unittest


service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)


class WebpageTests(unittest.TestCase):     

    def test_title(self):
        """Make sure title is correct"""
        driver.get("http://127.0.0.1:8000/")
        self.assertEqual(driver.title, "ePortfolio")
        
    def test_login(self):
        """Make sure login works"""
        driver.get("http://127.0.0.1:8000/accounts/login/")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("testuser")
        password.send_keys("testpassword123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Hello, testuser!")
        
    def test_about(self):
        """Make sure about page works"""
        driver.get("http://127.0.0.1:8000/about/testuser/")
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "About Me")  

    def test_projects(self):
        """Make sure projects page works"""
        driver.get("http://127.0.0.1:8000/projects/testuser/")
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "My Projects")

    # Test adding a project
        wait = WebDriverWait(driver, 10)
        add = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'+add project')]")))
       
        add.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Add Project")
        title = driver.find_element(By.NAME, "title")
        title.click()
        title.clear()
        title.send_keys("Selenium Test")
        
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, 'add_project')))
        button.click()

        wait = WebDriverWait(driver, 10)
        h2 = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))

        self.assertEqual(h2.text, "My Projects")
        
        # Test project page
        wait = WebDriverWait(driver, 10)
        project = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Selenium Test')]")))
        project.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Project: Selenium Test")
    
        # Test editing a project
        wait = WebDriverWait(driver, 10)
        edit = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Edit')]")))
        edit.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Edit Project")
        
        title = driver.find_element(By.NAME, "title")
        title.click()
        title.clear()
        title.send_keys("Selenium Test")
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, 'save_project')))
        button.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Project: Selenium Test")

        # Test deleting a project
        projects = driver.find_element(By.XPATH, "//a[contains(text(), 'Projects')]")
        projects.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "My Projects")
        project = driver.find_element(By.XPATH, "//p[contains(text(), 'Selenium Test')]")
        button = project.find_element(By.XPATH, "//button[contains(text(), 'X')]")
        button.click()
        delete = driver.find_element(By.XPATH, "//button[contains(text(), 'Yes')]")
        delete.click()
        deleted_project = WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.XPATH, '//p[contains(text(), "Selenium Test")]')))
        self.assertEqual(deleted_project, True)
    
    def test_contact(self):
        """Make sure contact page works"""
        driver.get("http://127.0.0.1:8000/contact/testuser/")
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Contact")
        
    def test_profile(self):
        """Make sure profile page works"""

        driver.get("http://127.0.0.1:8000/profile/")
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "My Profile")
        driver.find_element(By.CSS_SELECTOR, "a[href='/edit_profile/']").click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h2").text, "Edit Profile")

        driver.find_element(By.NAME, "first_name").click()
        driver.find_element(By.NAME, "first_name").clear()
        driver.find_element(By.NAME, "first_name").send_keys("Selenium Test")
        driver.find_element(By.ID, "id_role").click()
        wait = WebDriverWait(driver, 10) 
        button = wait.until(EC.element_to_be_clickable((By.ID, 'save_profile')))
        button.click()
        self.assertEqual(driver.find_element(By.ID, "first_name").text, "Selenium Test")
       
        
if __name__ == "__main__":
    unittest.main()
