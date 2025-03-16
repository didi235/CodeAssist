from selenium import webdriver

# تشغيل المتصفح
driver = webdriver.Chrome()
driver.get("https://www.google.com")

print("✅ Selenium يعمل بشكل صحيح!")
driver.quit()
