from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest

class TestPaper2:

    @pytest.mark.task1
    def test_task_1(self, driver):
        driver.get("https://www.fairprice.com.sg/")
        wait = WebDriverWait(driver, 10)

        # Search for pringles
        search_bar = driver.find_element(By.XPATH, "//input[@id='search-input-bar']")
        search_bar.send_keys("pringles")
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@class='sc-a96d6768-7 fcoLHR']")))
        search_button = driver.find_element(By.XPATH, "//a[@class='sc-a96d6768-7 fcoLHR']")
        driver.execute_script("return arguments[0].click();", search_button)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/search?query=pringles"))

        # Find correct product
        products = driver.find_elements(By.XPATH, "//div[@class='sc-e68f503d-1 ihIPNR']")
        pringles = products[1]
        driver.execute_script("return arguments[0].click();", pringles)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/product/pringles-potato-crisps-sour-cream-onion-150g-12387644"))

        # Add one to cart
        add_to_cart = driver.find_element(By.XPATH, "//button[@class='sc-f40c9526-6 bGoBHX']")
        driver.execute_script("return arguments[0].click();", add_to_cart)

        # First-time validation
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='sc-26556e54-2 hScVig']")))
        postal_code = driver.find_element(By.XPATH, "//input[@class='sc-26556e54-2 hScVig']")
        postal_code.send_keys("528494")
        actions.send_keys(Keys.ENTER)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='suggestion-item']")))
        suggestions = driver.find_elements(By.XPATH, "//div[@class='suggestion-item']")
        address = suggestions[0]
        address.click()
        confirm_address = driver.find_element(By.XPATH, "//button[@class='sc-e209a1d1-7 bZuYjG']")
        confirm_address.click()

        # badges = driver.find_elements(By.XPATH, "//*[contains(text(), '1')]")
        # assert len(badges) == 57

        # Add more
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")))
        circle_buttons = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")
        add = circle_buttons[1]
        driver.execute_script("return arguments[0].click();", add)
        inputs_check = driver.find_elements(By.XPATH, "//input[@class='sc-43bf2827-0 jZsSbP']")
        check_input = inputs_check[0]
        assert check_input.get_attribute('value') == '2'

        # Search for indomie
        search_bar = driver.find_element(By.XPATH, "//input[@id='search-input-bar']")
        search_bar.send_keys("indomie")
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@class='sc-a96d6768-7 fcoLHR']")))
        search_button = driver.find_element(By.XPATH, "//a[@class='sc-a96d6768-7 fcoLHR']")
        driver.execute_script("return arguments[0].click();", search_button)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/search?query=indomie"))

        # Find correct product
        indomie = driver.find_element(By.XPATH, "//*[contains(text(), 'Indomie Instant Noodles - Soto')]")
        driver.execute_script("return arguments[0].click();", indomie)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/product/indomie-instant-noodles-soto-5-x-78g-13074179"))

        # Add one to cart
        add_to_cart = driver.find_element(By.XPATH, "//button[@class='sc-f40c9526-6 bGoBHX']")
        driver.execute_script("return arguments[0].click();", add_to_cart)

        # Add 2 more
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")))
        circle_buttons = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")
        add = circle_buttons[1]
        driver.execute_script("return arguments[0].click();", add)
        driver.execute_script("return arguments[0].click();", add)
        check_input = driver.find_element(By.XPATH, "//input[@class='sc-43bf2827-0 jZsSbP']")
        assert check_input.get_attribute('value') == '3'

        # Navigate to cart
        cart = driver.find_element(By.XPATH, "//a[@class='sc-87d8844f-4 HekhK']")
        driver.execute_script("return arguments[0].click();", cart)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/cart"))

        # Check indomie cost == $7.95
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), '$7.95')]")))

        # Check pringles == 2
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='sc-43bf2827-2 hnefVS']/input")))
        product_quants = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-2 hnefVS']/input")
        pringles_quant = product_quants[0]
        assert pringles_quant.get_attribute('value') == '2'

        # Make pringles == 1
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")))
        circle_buttons = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")
        minus = circle_buttons[0]
        driver.execute_script("return arguments[0].click();", minus)
        product_quants = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-2 hnefVS']/input")
        pringles_quant = product_quants[0]
        assert pringles_quant.get_attribute('value') == '1'

        # Check pringles price updated
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), '$3.50')]")))

        # Remove all indomie from the cart
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")))
        circle_buttons = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")
        minus = circle_buttons[2]
        driver.execute_script("return arguments[0].click();", minus)
        driver.execute_script("return arguments[0].click();", minus)
        driver.execute_script("return arguments[0].click();", minus)
        assert wait.until_not(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Indomie Instant Noodles - Soto')]")))

        # Empty cart
        wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")))
        circle_buttons = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")
        minus = circle_buttons[0]
        # TODO - why do i need to execute this twice to work
        driver.execute_script("return arguments[0].click();", minus)
        driver.execute_script("return arguments[0].click();", minus)
        # assert wait.until_not(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Pringles Potato Crisps - Sour Cream & Onion')]")))

        # Check the cart to be empty
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your cart is empty')]")))

    @pytest.mark.task2
    def test_task_2(self, driver):
        driver.get("https://www.fairprice.com.sg/")
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        # Click on categories
        filters = driver.find_elements(By.XPATH, "//a[@class='sc-c389c434-3 eEXWOw']")
        categories = filters[0]
        driver.execute_script("return arguments[0].click();", categories)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/categories"))

        # Check 20 categories
        all_categories = driver.find_elements(By.XPATH, "//ul[@class='sc-f363cdf4-0 gsrWvp']/li")
        actual_num = len(all_categories) // 2
        assert actual_num == 20

        # Select bread
        bread = driver.find_element(By.XPATH, "//*[contains(text(), 'breads')]")
        driver.execute_script("return arguments[0].click();", bread)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/category/breads--1"))

        # Check gardania is there
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Gardenia Enriched White Bread')]")))

        # Check price is 3.20
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), '$3.20')]")))

        # Find correct product
        breads = driver.find_elements(By.XPATH, "//*[contains(text(), 'Gardenia Enriched White Bread')]")
        correct_bread = breads[1]
        driver.execute_script("return arguments[0].click();", correct_bread)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/product/gardenia-enriched-white-bread-600g-10099606"))

        # Add one to cart
        add_to_cart = driver.find_element(By.XPATH, "//button[@class='sc-f40c9526-6 bGoBHX']")
        driver.execute_script("return arguments[0].click();", add_to_cart)

        # First-time validation
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='sc-26556e54-2 hScVig']")))
        postal_code = driver.find_element(By.XPATH, "//input[@class='sc-26556e54-2 hScVig']")
        postal_code.send_keys("528494")
        actions.send_keys(Keys.ENTER)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='suggestion-item']")))
        suggestions = driver.find_elements(By.XPATH, "//div[@class='suggestion-item']")
        address = suggestions[0]
        address.click()
        confirm_address = driver.find_element(By.XPATH, "//button[@class='sc-e209a1d1-7 bZuYjG']")
        confirm_address.click()

        # Add one more to cart (Total 2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")))
        circle_buttons = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")
        add = circle_buttons[1]
        driver.execute_script("return arguments[0].click();", add)
        check_input = driver.find_element(By.XPATH, "//input[@class='sc-43bf2827-0 jZsSbP']")
        assert check_input.get_attribute('value') == '2'

        # Select categories again
        filters = driver.find_elements(By.XPATH, "//a[@class='sc-c389c434-3 eEXWOw']")
        categories = filters[0]
        driver.execute_script("return arguments[0].click();", categories)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/categories"))

        # Select breakfast
        breakfast = driver.find_element(By.XPATH, "//*[contains(text(), 'breakfast')]")
        driver.execute_script("return arguments[0].click();", breakfast)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/category/breakfast-1"))

        # Add 2 fairprice rolled oats
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'FairPrice Rolled Oats')]")))
        rolled_oats = driver.find_elements(By.XPATH, "//*[contains(text(), 'FairPrice Rolled Oats')]")
        rolled_oats_product = rolled_oats[1]
        driver.execute_script("return arguments[0].click();", rolled_oats_product)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/product/fairprice-rolled-oats-1kg-12331704"))
        add_to_cart = driver.find_element(By.XPATH, "//button[@class='sc-f40c9526-6 bGoBHX']")
        driver.execute_script("return arguments[0].click();", add_to_cart)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")))
        circle_buttons = driver.find_elements(By.XPATH, "//div[@class='sc-43bf2827-5 grwDbY']")
        add = circle_buttons[1]
        driver.execute_script("return arguments[0].click();", add)
        check_input = driver.find_element(By.XPATH, "//input[@class='sc-43bf2827-0 jZsSbP']")
        assert check_input.get_attribute('value') == '2'

        # Navigate to cart
        cart = driver.find_element(By.XPATH, "//a[@class='sc-87d8844f-4 HekhK']")
        driver.execute_script("return arguments[0].click();", cart)
        assert wait.until(ec.url_to_be("https://www.fairprice.com.sg/cart"))

        # Check rolled oats cost == $9.60
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), '$9.60')]")))

        # Check bread cost == $6.40
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), '$6.40')]")))

        # Check total == $16
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), '$16.00')]")))

