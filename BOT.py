from selenium import webdriver
import time


def BOT():
    #Setar o navegador do bot como sendo o Google Chrome
    navegator = webdriver.Chrome()
    navegator.get("https://www.artwalk.com.br/tenis-vans-era-59-4589m-e-400/p")
    navegator.find_element_by_xpath('/html/body/main/section[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/ul/li[2]/span/label[5]').click()
    navegator.find_element_by_xpath('//*[@id="buscar-localizacao"]').send_keys("22060020")
    navegator.find_element_by_xpath('//*[@id="btn-buscar-cep"]/fieldset/div[1]/div/button').click()
    time.sleep(1000000)


BOT()

