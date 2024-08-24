from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys

class FromPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = driver.find_element(By.ID, "firstName")
        self.last_name_input = driver.find_element(By.ID, "lastName")
        self.email_input = driver.find_element(By.ID, "userEmail")
        self.gender_radio_button = driver.find_element(By.XPATH, "//label[@for= 'gender-radio-2']")
        self.mobile_input = driver.find_element(By.ID, "userNumber")
        self.date_of_birth_input = driver.find_element(By.ID, "dateOfBirthInput")
        self.subjects_input = driver.find_element (By.ID, "subjectsInput")
        self.hobbies_checkbox = driver.find_element(By.XPATH, "//label[text()= 'Music']")
        self.upload_picture_input = driver.find_element(By.ID, "uploadPicture")
        self.current_address_input = driver.find_element(By.ID, "currentAddress")
        self.state_dropdown = driver.find_element(By.ID, "react-select-3-input")
        self.city_dropdown = driver.find_element(By.ID, "react-select-4-input")
        self.submit_button = driver.find_element(By.ID, "submit")

    def fill_first_name(self, first_name):
        self.first_name_input.send_keys(first_name)

    def fill_last_name(self, last_name):
        self.last_name_input.send_keys(last_name)

    def fill_email(self, email):
        self.email_input.send_keys(email)

    def select_gender(self):
        self.gender_radio_button.click()

    def fill_mobile(self, mobile):
        self.mobile_input.send_keys(mobile)

    def select_date_of_birth(self, date):
        self.date_of_birth_input.send_keys(date)
        self.date_of_birth_input.send_keys(Keys.RETURN)

    def fill_subjects(self, subject):
        self.subjects_input.send_keys(subject)
        self.subjects_input.send_keys(Keys.RETURN)

    def select_hobbies(self):
        self.hobbies_checkbox.click()

    def upload_picture(self, file_path):
        self.upload_picture_input.send_keys(file_path)

    def fill_current_address(self, address):
        self.current_address_input.send_keys(address)

    def select_state(self, state):
        self.state_dropdown.send_keys(state)
        self.state_dropdown.send_keys("\n")

    def select_city(self, city):
        self.city_dropdown.send_keys(city)
        self.city_dropdown.send_keys("\n")

    def submit_form(self):
        self.submit_button.click()
