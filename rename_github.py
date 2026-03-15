import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("선생님의 기존 크롬 세션을 사용하기 위해 열려있는 크롬 브라우저를 강제 종료합니다...")
os.system("taskkill /F /IM chrome.exe /T")
time.sleep(4)

options = Options()
options.add_argument(r"user-data-dir=C:\Users\eyedr\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"profile-directory=Default")
options.add_argument("--start-maximized")
# 에러 방지용 옵션들 추가
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print(f"Chrome 브라우저 시작 실패: {e}")
    sys.exit(1)

wait = WebDriverWait(driver, 15)

try:
    print("GitHub 계정 설정 페이지(https://github.com/settings/admin)로 이동합니다...")
    driver.get("https://github.com/settings/admin")
    time.sleep(3)
    
    if "login" in driver.current_url and "settings" not in driver.current_url:
        print("[에러] GitHub 로그인이 풀려있습니다.")
        sys.exit(1)

    print("'Change username' 버튼을 찾아 클릭합니다...")
    change_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Change username') or contains(., 'username')]")))
    change_btn.click()
    
    print("경고창이 뜨면 'I understand' 버튼을 클릭합니다...")
    time.sleep(2)
    understand_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'I understand')]")))
    understand_btn.click()
    
    print(f"새로운 아이디 'charlotte-shin-art'를 입력합니다...")
    time.sleep(2)
    input_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and (contains(@name, 'login') or contains(@id, 'login'))]")))
    input_field.clear()
    input_field.send_keys("charlotte-shin-art")
    
    time.sleep(3)
    
    print("최종 'Change my username' 버튼을 클릭하여 확정합니다...")
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Change my username')]")))
    submit_btn.click()
    
    print("성공적으로 아이디를 변경했습니다!")
    time.sleep(5)
    
except Exception as e:
    print(f"\n[자동화 오류 발생] 브라우저 화면이 예상과 다릅니다. 에러 상세: {e}")
finally:
    driver.quit()
