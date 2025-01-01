from seleniumbase import SB
import time

SELECTOR = "body > div.gl-h-full.gl-flex.gl-flex-wrap > div.container.gl-self-center > div > div.gl-my-5 > div.col-sm-12.gl-text-center > h1"

with SB(uc=True, test=True, locale_code="fr", headed=False, incognito=True) as sb:
    url = "https://gitlab.com/users/sign_in"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.save_screenshot_to_logs()
    if sb.is_element_present(SELECTOR):
        print("It worked! Found the element using v1!")

time.sleep(3)

with SB(uc=True, test=True, locale_code="fr", headed=False) as sb:
    url = "https://gitlab.com/users/sign_in"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.cdp.gui_click_element("#HJup0 > div")
    sb.sleep(2)
    sb.save_screenshot_to_logs()
    if sb.is_element_present(SELECTOR):
        print("It worked! Found the element using v2!")
