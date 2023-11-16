import webbrowser
import pyautogui as pt
import pyperclip
import openai
from __init__ import KEY

openai.api_key = KEY
model = 'gpt-3.5-turbo'


def open_notification():
    notification_position = pt.locateCenterOnScreen('whatsapp/notification.PNG', confidence=0.9)
    print(notification_position, notification_position[0], notification_position[1])
    pt.moveTo(notification_position[0] - 20, notification_position[1])
    pt.click()


# def open_chrome():
#     chrome_position = pt.locateCenterOnScreen('whatsapp/chrome.PNG', confidence=0.8)
#     print(chrome_position)
#     pt.click(chrome_position)


def gpt_response():
    response = openai.ChatCompletion.create(model=model,
                                            messages=[{"role": "user",
                                                       "content": "{}".format(copied_text)}])
    pt.click(750, 695)
    response_list = response['choices'][0]['message']['content'].split("\n")
    for sentence in response_list:
        pt.write(f'{sentence}', interval=0.004)
        pt.hotkey('shift', 'enter')
    pt.press('enter')

webbrowser.open_new_tab("https://web.whatsapp.com")
# open_chrome()
# pt.sleep(2)
#
# pt.hotkey('ctrl', 't')
#
# pt.write('web.whatsapp.com', interval=0.1)
# pt.press('enter')

while True:

    try:
        pt.sleep(10)
        open_notification()
        pt.sleep(2)
        pt.tripleClick(x=484, y=627)
        pt.hotkey('ctrl', 'c')
        copied_text = pyperclip.paste()
        gpt_response()
        pt.click(220, 210)
        pt.sleep(20)

    except TypeError:
        pt.sleep(10)
        continue
