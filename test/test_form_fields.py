import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from page import FromPage
import allure


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://demoqa.com/automation-practice-form")
    yield driver
    driver.quit()


@allure.feature("Form Submission")
def test_from_submission(driver):
    page = FromPage(driver)
    page.fill_first_name("Adelia")
    page.fill_last_name("Ilyasova")
    page.fill_email("adelia@example.com")
    page.select_gender()
    page.fill_mobile("1234567890")
    page.select_date_of_birth("04 Mar 2003")
    page.fill_subjects("Computer Science")
    page.select_hobbies()
    page.upload_picture(r"C:\Users\user\Desktop\photo_2024.jpg")
    page.fill_current_address("221b Baker street")
    page.select_state("Haryana")
    page.select_city("Karnal")
    page.submit_form()

    confirmation_model = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    assert confirmation_model.text == "Thanks for submitting the form"
