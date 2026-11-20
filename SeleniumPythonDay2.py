#DAY 02
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(executable_path=r"E:\chromedriver_win32\chromedriver.exe"))
driver.get("https://www.youtube.com/watch?v=D8DZahU4WfM&t=2996s")



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/watch?v=D8DZahU4WfM&t=2996s")