from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes

# url = "https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Stainless/dp/B00OP26T4K/ref=sr_1_1_sspa?crid=OID5XLXOCKGM&dib=eyJ2IjoiMSJ9.luyDQsWGnxgY1FNKzfH3A4pmpkBbKVnsDK0fHzqqytEXZzOQ8MVJ3nvYde3KUbQbVsHUBQPmE-ebyfBuvwE8_abmS8SF75gSOoEuY-tptz9wrsrsHg9DZrLqdtOvUZ-XZd_W6Qm_hMjJHMj9dsig_7NyOffdz3MLKviPPkCS9O5--Xi4Z66U824yihG6dfESX9WWxGh3Yzb0QiRPRE5Mx67MPE1C1tR50YXA1J1qzMM.ADKBHsUsFSq5QKksnFg2LKeMxSo-bpOYQEZYxMXwskM&dib_tag=se&keywords=instant%2Bpot%2Bduo&qid=1772635779&sprefix=instant%2Bpot%2Bduo%2Caps%2C297&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.95fd378e-6299-4723-b1f1-3952ffba15af&aref=InODXPI2eh&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
# url= "https://www.loraxcompliance.com/"
url="https://www.python.org/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(url)









# price_dollar =  driver.find_element(By.CLASS_NAME,value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction").text
#
# print(f"The price is £{price_dollar}.{price_cents}")

#search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link=driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)


# bug_link=driver.find_element(By.XPATH,value='//*[@id="feature-bullets"]/h1')
# print(bug_link.text)


#closes tab
# driver.close()
#closes the browser




driver.quit()