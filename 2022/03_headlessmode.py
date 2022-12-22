
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# # 使用headless 模式只需给webdriver 添加 options 参数即可， headless 模式下剪贴板无法操作！
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument("User-Agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
chrome_options.add_argument("log-level=3") # 终端不显示 错误提示 SSL error code 1
browser  = webdriver.Chrome(options=chrome_options)
