from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time 
import numpy as np

love_words = np.array(['Sadaqo','Qurbano','Shaisto','Jaro','Zirgo','Babako'])
love_sentences = np.array([
    "You light up my life.",
    "Every moment with you is a treasure.",
    "You have my heart forever.",
    "I am grateful for your love.",
    "You make my world complete.",
    "With you, I am home.",
    "Your smile brightens my day.",
    "I cherish every moment with you.",
    "You are my greatest adventure.",
    "Together, we are unstoppable."
])
commitment_sentences = np.array([
    "I promise to stand by you through thick and thin.",
    "You are my partner, and I will always support you.",
    "I am committed to growing together and nurturing our love.",
    "I will always prioritize our relationship above all else.",
    "You are my forever, and I will cherish you always.",
    "I promise to listen to you and understand your feelings.",
    "Together, we will build a beautiful future.",
    "I will always be faithful and true to you.",
    "You are my priority, and I will always make time for us.",
    "I vow to love you unconditionally for all my days."
])
love_sentences_urdu = np.array([
    "تم میری زندگی کی سب سے خوبصورت حقیقت ہو۔",
    "میرا دل ہمیشہ تمہارے ساتھ دھڑکتا ہے۔",
    "تمہارے بغیر میری دنیا ادھوری ہے۔",
    "تمہاری محبت میری زندگی کا سب سے قیمتی خزانہ ہے۔",
    "میں تمہیں دل کی گہرائیوں سے چاہتا ہوں۔",
    "تم میرے خوابوں کی تعبیر ہو۔",
    "ہر پل تمہارے ساتھ جینے کا وعدہ کرتا ہوں۔",
    "تمہاری مسکراہٹ میری دنیا روشن کر دیتی ہے۔",
    "تمہارے ساتھ ہر لمحہ ایک حسین یاد بن جاتا ہے۔",
    "میری محبت ہمیشہ تمہارے ساتھ رہے گی۔"
])
farewell_sentences = np.array([
    "الوداع، ہمیشہ یاد آؤ گے۔",
    "یہ جدا ہو جانا مشکل ہے، لیکن ہمیشہ دل میں رہو گے۔",
    "تمہاری کمی ہمیشہ محسوس ہوگی۔",
    "اللہ تمہیں ہمیشہ خوش رکھے، الوداع۔",
    "اللہ حافظ، جب تک پھر سے ملاقات نہ ہو۔",
    "Goodbye, you will always be missed.",
    "Parting is hard, but you will stay in my heart forever.",
    "Wishing you all the best, farewell.",
    "Take care, until we meet again.",
    "May our paths cross again soon. Farewell!"
])
sorry_sentences = np.array([
    # Urdu

    "مجھے معاف کر دو، میں غلطی پر تھا۔",
    "میں دل سے معذرت چاہتا ہوں۔",
    "میری غلطی تھی، براہ کرم مجھے معاف کر دو۔",
    "مجھے افسوس ہے، میں نے آپ کو تکلیف دی۔",
    "میری بات سے آپ کو دکھ پہنچا، معاف کیجیے گا۔",
    "براہ کرم، میری معذرت قبول کریں۔",
    "مجھے اندازہ ہے کہ میں نے غلط کیا، معاف کر دیں۔",
    "مجھے اپنی غلطی کا احساس ہے، آپ کو دکھ دیا۔",
    "آپ کی دل آزاری کا بہت افسوس ہے، معاف کیجیے۔",
    "میں اپنی حرکت پر شرمندہ ہوں، معافی چاہتا ہوں۔",
    
    # English
    "I think you are mad at me"
    "I’m truly sorry for my mistake.",
    "Please forgive me, I didn’t mean to hurt you.",
    "I apologize from the bottom of my heart.",
    "I regret my actions and seek your forgiveness.",
    "I am sorry for causing you pain.",
    "Please accept my sincere apology.",
    "It was my fault, and I am truly sorry.",
    "I didn’t mean to upset you, I’m really sorry.",
    "I feel terrible for what I did, please forgive me.",
    "I apologize for my behavior, it won’t happen again."
])

# print(love_words)

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for manual login (scan the QR code)
print("Please scan the QR code for WhatsApp Web login.")
time.sleep(25)


# Locate the search bar where you can input the contact name
search_bar = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @role="textbox"]')

# Clear the search bar (optional, in case there's any pre-filled text)
search_bar.clear()

# Enter the search term "Maham"
search_bar.send_keys("SS")

# Wait a bit to see the results appear
# time.sleep(2)  # Adjust as needed

# Optionally press Enter to select the first result (if needed)
search_bar.send_keys(Keys.RETURN)

# Locate the message input area where you can type your message
message_input = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')
for i in range(10):
    # Clear the message input area (optional)
    message_input.clear()
    # random_word = np.random.choice(love_words)
    # random_word = np.random.choice(love_sentences)
    # random_word = np.random.choice(commitment_sentences)
    # random_word = np.random.choice(love_sentences_urdu)
    # random_word = np.random.choice(farewell_sentences)
    # random_word = np.random.choice(sorry_sentences)
    # time.sleep(0.2)

    # Type "AoA" into the message input area
    # message_input.send_keys(random_word)
    # message_input.send_keys('mere charging khatm horhe a me tora charge krta hn phir teray sath pora din guzaron ga')
    message_input.send_keys('  v')

    # Press Enter to send the message
    message_input.send_keys(Keys.RETURN)

# Wait a moment to see the message sent
time.sleep(5)  # Adjust as needed
