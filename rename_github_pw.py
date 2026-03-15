from playwright.sync_api import sync_playwright
import time
import sys
import os

print("선생님의 기존 로그인 세션을 Playwright 모듈로 안전하게 조작하기 위해 크롬을 잠시 종료합니다...")
os.system("taskkill /F /IM chrome.exe /T")
os.system("taskkill /F /IM chromedriver.exe /T")
time.sleep(3)

with sync_playwright() as p:
    try:
        print("Playwright 로봇이 선생님의 크롬 프로필(Default) 데이터를 이용하여 실행됩니다...")
        browser_context = p.chromium.launch_persistent_context(
            user_data_dir=r"C:\Users\eyedr\AppData\Local\Google\Chrome\User Data",
            channel="chrome",
            headless=False,
            args=["--start-maximized", "--no-sandbox"]
        )
        page = browser_context.pages[0] if browser_context.pages else browser_context.new_page()
        
        print("GitHub 계정 설정 페이지로 이동 중...")
        page.goto("https://github.com/settings/admin", wait_until="load")
        time.sleep(3)
        
        # 선생님 화면에 어떻게 보이는지 확인
        print(f"현재 열린 페이지 주소: {page.url}")
        
        change_btn = page.locator("button", has_text="Change username").first
        if change_btn.is_visible():
            print("'Change username' 버튼 감지 및 클릭!")
            change_btn.click()
            time.sleep(2)
            
            understand_btn = page.locator("button", has_text="I understand").first
            if understand_btn.is_visible():
                print("경고창 'I understand' 버튼 클릭!")
                understand_btn.click()
                time.sleep(2)
            
            # input box
            print("새로운 아이디 'charlotte-shin-art' 입력 중...")
            login_inputs = page.locator("input[name*='login'], input[id*='login']").all()
            for inp in login_inputs:
                if inp.is_visible():
                    inp.fill("charlotte-shin-art")
                    break
            
            time.sleep(3)
            
            submit_btn = page.locator("button", has_text="Change my username").first
            if submit_btn.is_visible():
                print("최종 'Change my username' 버튼 클릭!")
                submit_btn.click()
                print("✅ 성공적으로 아이디가 변경되었습니다!")
                time.sleep(5)
            else:
                print("최종 확인 버튼을 찾을 수 없습니다.")
        else:
            print("❌ 'Change username' 버튼을 찾지 못했습니다. (이미 변경되었거나, 다른 화면일 수 있습니다.)")
            
        browser_context.close()
    except Exception as e:
        print(f"\n[오류 발생] Playwright 제어 중 에러: {e}")
