from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import pytest

# TODO - pagination thing
# TODO - test screenshot is working

class TestPaper1:

    @pytest.mark.task1
    def test_task_1(self, driver):

        driver.get("https://www.tp.edu.sg/home.html")

        # Bar is visible
        bar = driver.find_element(By.XPATH, "//div[@class='header-search-box']")
        assert bar.is_displayed()

        # Check text displays 108
        search = driver.find_element(By.XPATH, "//div[@class='header-search-box']/input")
        search.send_keys("artificial intelligence")
        search_button = driver.find_element(By.XPATH, "//a[@class='header-search-icon']")
        driver.execute_script("return arguments[0].click();", search_button)
        wait = WebDriverWait(driver, 10)
        wait.until(ec.url_to_be("https://www.tp.edu.sg/search.html?keyword=artificial%20intelligence"))
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='filter-mobile']")))
        result = driver.find_element(By.XPATH, "//*[contains(text(), 'Displaying 1 - 10 Results of 108')]")
        assert result.text == "Displaying 1 - 10 Results of 108"

        # Check AI Empowerment exists
        topics = driver.find_elements(By.XPATH, "//div[@class='item']/a")
        topic_here = False
        for topic in topics:
            if topic.text == "AI Empowerment Hub":
                topic_here = True
        assert topic_here

        # Filter by course and check 37 results
        filters = driver.find_elements(By.XPATH, "//label[@class='custom-checkbox']/input")
        course_checkbox = filters[2]
        driver.execute_script("return arguments[0].click();", course_checkbox)
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Displaying 1 - 10 Results of 37')]")))
        result = driver.find_element(By.XPATH, "//*[contains(text(), 'Displaying 1 - 10 Results of 37')]")
        assert result.text == "Displaying 1 - 10 Results of 37"

        # Change to 30 per page, check only 2
        dropdown = driver.find_element(By.ID, "select-global-limit")
        select_dropdown = Select(dropdown)
        select_dropdown.select_by_value('30')
        options = driver.find_elements(By.XPATH, "//select[@id='select-global-limit']/option")
        option = options[2]
        assert wait.until(lambda _: option.is_selected())
        # pages = driver.find_elements(By.XPATH, "//li[@class='paginationjs-page J-paginationjs-page']/span")
        # assert len(pages) == 2

        # pages = driver.find_elements(By.XPATH, "//div[@class='paginationjs-pages']/ul/li")
        # total_pages = len(pages) - 6
        # assert total_pages == 2

        # pages = driver.find_elements(By.XPATH, "//div[@class='paginationjs-pages']")
        # assert len(pages) == 2

        pages2 = driver.find_elements(By.XPATH, "//span[contains(text(), '2')]")
        pages1 = driver.find_elements(By.XPATH, "//span[contains(text(), '1')]")
        total_pages = len(pages2) + len(pages1) - 3
        assert total_pages == 2


    @pytest.mark.task2
    def test_task_2(self, driver):
        driver.get("https://www.tp.edu.sg/landing/industry-partners.html")

        # Check image displayed
        image = driver.find_element(By.XPATH, "//div[@class='cmp-main-masthead__img']/img")
        assert image.is_displayed()

        # Check 4 ways to collab
        columns = driver.find_elements(By.XPATH, "//div[@class='cmp-tiles-component__col']")
        assert len(columns) == 4

        # Check ocbc is displayed
        logos = driver.find_elements(By.XPATH, "//div[@class='cmp-logo-box-list ']/a/img")
        ocbc = logos[2]
        assert ocbc.is_displayed()

    @pytest.mark.task3
    def test_task_3(self, driver):
        driver.get("https://www.sp.edu.sg/")

        # Search for cyber and check 78 results
        button1 = driver.find_element(By.XPATH, "//button[@class='search-button desktop-only']")
        button1.click()
        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.ID, "searchsg-input")))
        search = driver.find_element(By.ID, "searchsg-input")
        search.send_keys("cybersecurity")
        search_button = driver.find_element(By.ID, "search-button")
        search_button.click()
        wait.until(ec.url_contains("https://www.sp.edu.sg/search-results?q=cybersecurity&scope=domain"))
        frame = driver.find_element(By.ID, "searchsg-frame")
        driver.switch_to.frame(frame)
        assert wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(), 'of 78 results')]")))
        result_text = driver.find_elements(By.XPATH, "//h5")
        result = result_text[1]
        assert ['of 78 results' in result.text]

        # Check 8 pages
        pages = driver.find_elements(By.XPATH, "//ul[@class='pagination_page-number-group__giBPv']/li")
        assert len(pages) == 8

    @pytest.mark.task4
    def test_task_4(self, driver):
        driver.get("https://www.tp.edu.sg/openhouse/")

        # Verify 8 links
        wait = WebDriverWait(driver, 10)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='col-12 col-sm-6 col-md-4 wow fadeInUp']/a")))
        seminar_links = 0
        first_6 = driver.find_elements(By.XPATH, "//div[@class='col-12 col-sm-6 col-md-4 wow fadeInUp']/a")
        seminar_links += len(first_6)
        last_2 = driver.find_elements(By.XPATH, "//div[@class='col-12 col-sm-12 col-md-6 wow fadeInUp']/a")
        seminar_links += len(last_2)

        # Check video settings
        videos = driver.find_elements(By.XPATH, "//video")
        video = videos[0]
        assert video.get_attribute("autoplay") == 'true'
        assert video.get_attribute("loop") == 'true'

        # Redirect successful
        button = driver.find_element(By.XPATH, "//button[@class='mt-3 btn btn-main btn-sm']")
        driver.execute_script("return arguments[0].click();", button)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        assert wait.until(ec.url_to_be("https://www.tp.edu.sg/about-tp/getting-to-tp.html"))
