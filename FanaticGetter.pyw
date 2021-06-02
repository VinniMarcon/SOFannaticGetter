from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from plyer import notification
import time

#########################################################################

# PREENCHA ABAIXO COM AS INFORMACOES NECESSARIAS PARA QUE O SCRIPT FUNCIONE:

# digite seu login e senha do site para que o script autentique seu login 
# quando abrir um navegador remoto 
# (navegadores remotos abrem com todos os sites deslogados)

email = 'insira seu e-mail aqui'

password = 'insira sua senha aqui'

hide = False
# definir essa linha como True permite que o script esconda a janela enquanto o processo eh executado, impedindo que uma janela seja aberta e atrapalhe seu trabalho. Voce precisara defini-la como False novamente caso deseja verificar um erro causado durante o processo.

######################################################################

def Notify(tt, msg):
    notification.notify(
        title=tt,
        message=f'{msg}',
        app_name='Python FanaticGetter',
    )
    

######################################################################

fanaticPoints = None
alreadyGet = True

# os sleeps garantem que algumas funcionalidades como a internet e a pagina carregada 
# estejam estaveis antes de prosseguir, voce pode remove-las se achar melhor
time.sleep(3)

if not hide:
    driver = webdriver.Firefox()
else:
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

driver.get('https://stackoverflow.com/')

time.sleep(1)

try:
    login = driver.find_elements_by_class_name('login-link')
    login[0].click()

    time.sleep(1)

    email_box = driver.find_element_by_id('email')
    email_box.send_keys(email)

    time.sleep(1)

    pass_box = driver.find_element_by_id('password')
    pass_box.send_keys(password)

    time.sleep(1)

    a = driver.find_element_by_id('submit-button')
    a.click()

    time.sleep(4)

    p = driver.find_elements_by_class_name('my-profile')
    p[0].click()

    i = driver.find_elements_by_class_name('iconGearSm')
    i[1].click()

    g = driver.find_elements_by_class_name('js-badge-class-Gold')

    time.sleep(1)

    for x in g:
        if x.text[:7].strip() == 'Fanatic':
            alreadyGet = False
            txt = x.text[9:]
            fanaticPoints = txt[:7].strip()

    time.sleep(1)
except:
    Notify("ERRO!","Um erro ocorreu durante o processo, verifique se as credenciais estão corretas ou se o stackoverflow detectou o acesso como um BOT!")

if alreadyGet == True or fanaticPoints == "100/100":
    Notify("CONCLUÍDO!","Você concluiu a medalha de ouro Fanatic, voce ja pode deletar o script!")
else:
    Notify("EM PROGRESSO!",f"Script executado com sucesso, mais um dia contado na medalha. Progresso da Fanatic: {fanaticPoints}")

driver.close()