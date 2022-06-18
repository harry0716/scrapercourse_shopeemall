from selenium import webdriver                             
from webdriver_manager.chrome import ChromeDriverManager   
from selenium.webdriver.common.by import By  
import time
from selenium.webdriver.common.action_chains import ActionChains #導入selenium的ActionChains套件

driver = webdriver.Chrome(ChromeDriverManager().install()) 

driver.get('https://shopee.tw/mall/%E6%9B%B8%E7%B1%8D%E5%8F%8A%E9%9B%9C%E8%AA%8C%E6%9C%9F%E5%88%8A-cat.11041120')  
time.sleep(5)

ActionChains(driver).move_by_offset(100,100).click().perform()  #用ActionChains動作鏈模組移動滑鼠到(100,100)的位置
                                                                #，呼叫click方法點擊屬左鍵，在呼叫perform方法執行。

cards = driver.find_elements(By.CSS_SELECTOR, "div[class='col-xs-2 recommend-products-by-view__item-card-wrapper']")

items = []
for card in cards:
    #ActionChains(driver).move_to_element(card).perform()  #自動化移動滑鼠到每一個商品區塊元素

    title = card.find_element(By.CSS_SELECTOR, "div[class='ie3A+n bM+7UW Cve6sh']").text
    price = card.find_element(By.CSS_SELECTOR, "div[class='vioxXd rVLWG6']").text
    link = card.find_element(By.TAG_NAME,"a").get_attribute('href')
    items.append((title,price,link))

#print(items)

result = []
for item in items:  #items的第三個抓取物件，就是商品的超連結(link)，就是子網頁連結。
    driver.get(item[2])  #子網頁連結在索引值2

    for i in range(5):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  #滾動滑鼠
        time.sleep(3)   #滑鼠滾動後設定等待時間

    comments = driver.find_elements(By.CSS_SELECTOR, "div[class='Em3Qhp'")  #用定位元素，尋找所有class屬性值為Em3Qhp的物件
    for comment in comments:
        result.append((item[0],item[1],comment.text))  #用text屬性爬取評價上的資料
    break

print(result)