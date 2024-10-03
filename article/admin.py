from selenium import webdriver
import time

# Firefox sürücüsünün yolu (geckodriver indirip yüklemiş olmanız gerekiyor)

# Firefox tarayıcısını başlatın ve arka planda çalışmasını sağlayın
firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
driver = webdriver.Firefox()

# Tarayıcıda açmak istediğiniz sayfanın URL'sini belirtin
url = 'https://oasis.izmirekonomi.edu.tr'

# Sayfayı açın
driver.get(url)

# Belirli bir süre boyunca sayfayı yenileyin (örneğin, 60 saniye)
yenileme_araligi = 60  # saniye cinsinden
while True:
    time.sleep(yenileme_araligi)
    driver.refresh()
