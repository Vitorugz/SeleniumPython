# Importando Bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

# Criando nosso navegador e definindo como google Chrome
driver = webdriver.Chrome()

# Definindo algumas opções usadas ao iniciar nosso navegador
options = webdriver.ChromeOptions()
# Exemplo a opção de iniciar com o navegador maximizado
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Variavel com a URL que iremos abrir
site_url = "https://demo.automationtesting.in/Register.html"

# Abrindo o navegador com o site desejado
driver.get(site_url)

name = 'Jorge'
# Encontrando um elemento no site apartir do seu XPATH ( obtido no menu de inspecionar elementos do google ), e enviando um texto para ele
driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys(name)

last_name = 'Silva'
driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys(last_name)

address = 'Rua Teste, Nº 123, Bairro Testando'
driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys(address)

email = 'testando123@testando.com'
# Aqui iremos encontrar um elemento usando seu ID, porém este ID esta relacionado a div pai do Input que queremos enviar nosso e-mail
# Desta forma, precisamos informar qual o ID da div, e dentro desta div, buscar nosso input
div = driver.find_element(By.ID, 'eid')
# Após definirmos nossa div, precisamos buscar nosso Input e enviar nosso email
div.find_element(By.TAG_NAME, 'input').send_keys(email)

tell = "11 9999999999"
# Aqui estamos buscando um elemento pelo seu CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, '#basicBootstrapForm > div:nth-child(4) > div > input').send_keys(tell)

# Aqui iremos criar um elemento select, para que possamsos selecionar uma opção em nosso site
skills = driver.find_element(By.XPATH, '//*[@id="Skills"]')
select_skills = Select(skills)
# Aqui iremos selecionar um elemento de acordo com o value dele
select_skills.select_by_value("APIs")

# Aqui faremos o mesmo processo, porém selecionando de acordo com o texto visivel
country = driver.find_element(By.XPATH, '//*[@id="country"]')
select_country = Select(country)
select_country.select_by_visible_text("Japan")

# aqui iremos usar uma função do selenium para colocar o nosso mouse sobre um menu, para que mais opções apareçam
# Neste hover, definimos qual elemento iremos levar nosso mouse
hover = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[9]/a')
# Aqui iremos fazer a ação de mover o mouse para o elemento definido acima 
ActionChains(driver)\
    .move_to_element(hover)\
    .perform()
# Após aparecerem mais opções, iremos clicar em uma das opções do menu suspenso
driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[9]/ul/li[4]/a').click()

# Por precaução, como iremos mudar de página, podemos colocar uma espera de no maximo 10s para que aguarde o total carregamento da tela para assim executar o próximo passo
driver.implicitly_wait(10)

# Aqui, iremos importar um arquivo para o site. Para importarmos, precisamos apenas enviar o caminho do arquivo, para um input do tipo file
driver.find_element(By.XPATH, '//*[@id="input-4"]').send_keys(r'C:\Users\vitor\OneDrive\Área de Trabalho\imgTest.png')

time.sleep(3)