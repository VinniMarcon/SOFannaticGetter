<!-- FANATIC BADGE GETTER (AmauterProjects) -->

<h1 style="text-align: center;">Fanatic Badge Getter</h1>
<h3 style="text-align: center;">Colete a sua primeira medalha de ouro no StackOverflow!</h3>

## Menu

* [O que é o FanaticGetter](#o-que-é-o-fanaticgetter)
* [Como o FanaticGetter funciona](#como-o-fanaticgetter-funciona)
* [Como usar o FanaticGetter](#como-usar-o-fanaticgetter)
* [Porque o uso do Geckodriver](#porque-o-uso-do-geckodriver)
* [Depois de concluir a medalha](#depois-de-concluir-a-medalha)
* [Problemas com o ReCaptcha](#problemas-com-o-recaptcha)

<hr>

# O que é o FanaticGetter

o FanaticGetter tem como propósito dar ao usuario do website StackOverflow a chance de ganhar 2 medalhas:

• **Enthusiast - Prata - Visite o site todos os dias por 30 dias consecutivos.**<br>
• **Fanatic - Ouro -  Visite o site todos os dias por 100 dias consecutivos.**

Sendo o StackOverflow um gigantesco website de Perguntas e Respostas (Q&A) envolvendo inúmeros profissionais a respeito da area da programação, inumeras pessoas que procuram por emprego nessa área constumam inserir os seus perfis do mesmo para adicionar maior credibilidade ao currículo. Empresas que valorizam sites como esses tendem a dar maior disponibilidade a aqueles que possuem um perfil com maior reputação, na qual inclue tantos os pontos, quanto é claro, as medalhas.

Mesmo sendo um perfil com 10, 500 ou 100k de pontos, conseguir uma medalha de ouro é algo complicado, e não tem como negar quanto ao fato de que perfis que contem ao menos 1 medalha de ouro nos oferece maior confianca em suas respostas do que aqueles que nao possuem. Por esse motivo o FanaticGetter foi criado! Pois mesmo sendo um membro ativo de tal comunidade, interagir com ela por 100 dias consecutivos pode ser as vezes impossível.

A medalha de ouro *Fanatic* é uma das medalhas de ouro que mais podem dar reputação ao programador nessas ocasiões, ja que interagir com um site como esses por 100 dias consecutivos demonstra o esforço do usuário de aprender e ajudar ao mesmo tempo a comunidade todos os dias com relação a programação.

O objetivo do script é dar a chance do usuário conquistar a medalha de ouro *Fanatic*, aumentando a credibilidade do perfil e consequentemente a chance de conseguir até mesmo um emprego.

<hr>

# Como o FanaticGetter funciona

O FanaticGetter trabalha puramente com *Python* e em posse do módulo `Selenium` para realizar as seguintes tarefas:

1. Apos alguns segundos de espera para que tudo esteja funcionando corretamente, o Script abre o Geckodriver e o site `https://stackoverflow.com/` no navegador Firefox em uma janela remota e em uma nova sessão. (Em alguns casos, o geckodriver abrirá uma janela CMD e fechará sozinho quando o programa terminar. Se for o caso, por favor nao o feche manualmente)

2. Em seguida, o script acessa automaticamente o botão de login (considerando o fato de que uma janela remota não contem nenhum site logado (cookies)) e realiza o login com base nas credenciais dadas pelo usuário dentro do script em `email` e `password`.

3. Apos a realização do acesso, o script clica no botao de perfil do usuário, informando ao site "Hey StackOverflow, eu estou acessando E interagindo com o site", ja que o site, em vários casos, nao aceita que voce apenas esteja nele.

4. Por fim, o script acessa a sua lista de Medalhas para contar o seu progresso da medalha `Fanatic` e então fecha o navegador sozinho.

O processo todo demora em media 8 segundos para completar.

O script tambem toma a liberdade de trabalhar com o módulo `plyer`, que contem a função capaz de enviar notificações do windows para o usuario, tornando muito mais facil relatar o progresso e qualquer problema sem a necessidade de manter o codigo aberto em um terminal.

Para manter tudo ainda mais facil, também esta disponível o arquivo Batch `StartupInstall.ps1`, que da ao usuário a chance de automaticamente criar um arquivo de inicialização do script na pasta de Inicializador do Windows (shell:startup), fazendo com que o Script abra toda vez que o usuario logar no computador. Dessa forma, ligar o seu computador por 100 dias consecutivos será a sua única preocupação para adquirir a medalha!

<hr>

# Como usar o FanaticGetter

### AVISO: esse script só funciona com *Firefox*, é preciso ter esse navegador instalado em sua maquina para prosseguir [aqui](https://www.mozilla.org/pt-BR/firefox/new/)


1. Baixe todos os arquivos inclusos nesse diretório juntos em qualquer lugar do Windows de sua preferencia.

2. Faça o download do `geckodriver.exe` manualmente [aqui](https://github.com/mozilla/geckodriver/releases), e o insira na mesma pasta que os outros arquivos.

3. Para executar o arquivo python, é necesário ter instalado as suas dependencias (**Selenium** e **Plyer**). Para isso, [instale o pip no sistema](https://pt.stackoverflow.com/questions/239047/como-instalar-o-pip-no-windows-10#answer-240469) e em seguida execute pelo Terminal na pasta do repositorio o seguinte comando: `pip install -r requirements.txt`

4. Para que o programa faça o login em sua conta durante o navegador remoto do Firefox, abra o arquivo `fanaticGetter.pyw` em um editor de texto de sua preferencia e edite as variaveis `email` e `password` para o seu e-mail e senha da sua conta do StackOverflow.

5. Em seguida, clique com o botão direito no arquivo `StartupInstall.ps1` e selecione a opção *Executar com o PowerShell*. Se o PowerShell pedir permissao para a criação de um arquivo, aceite. Dois arquivos serão criados, um inicializador na mesma pasta chamada `FanaticStartup.bat` e um atalho para o mesmo na pasta *Startup* do Windows.
 
6. Execute o arquivo `FanaticStartup.bat` e espere para verificar se tudo está ocorrendo nos conformes. Se uma notificação de erro aparecer, verifique se as credenciais nas variáveis estão corretas.

A partir daí, o FanaticGetter ja está setado para ser executado sempre que o computador inicializar.

<hr>

# Porque o uso do Geckodriver

Para que o programa funcione, é utilizado a biblioteca *Selenium*, na qual trabalha com a navegação remota de um navegador especifico, controlando-o em vez do ser humano. Mas para que isso seja capaz, a biblioteca passa a ser dependente de um driver especifico para cada navegador para que ela consiga estabelecer tal conexao remota, no caso do Firefox, utilizamos o *Geckodriver*.

Para saber mais a respeito de sua utilização, acesse [O que é o GeckoDriver](https://www.softwaretestinghelp.com/geckodriver-selenium-tutorial/#What_is_GeckoDriver).

<hr>

# Depois de concluir a medalha

Após a conclusão da medalha, as notificações dadas pelo programa começarão a avisar que a sua medalha enfim foi concluída, e que não é mais necessário utiliza-lo para tal função. Com isso, está na hora de fazer com que o programa pare de ser executado a cada inicialização

Pra fazer isso, existem duas formas, a forma mais pratica porém não aconselhavel é apenas deletar o diretório e os arquivos, ou então a forma mais pratica seria remove-lo da inicialização. Para isso, basta apertar `Windows + R`, digitar `shell:startup` e excluir o atalho `FanaticStartup`.

<hr>

# Problemas com o ReCaptcha

Apesar de o executável ter a capacidade de originar delays durante a execução remota para que o site não possa detectar tal movimento, em casos extremamente raros ainda á a possibilidade do StackOverflow suspeitar de que um bot esteja o acessando, com isso ele impedirá que voce prossiga até que resolva um ReCaptcha. Caso isso aconteca, não se preocupe, o programa avisará você que algo deu errado e você apenas precisará resolver o Captcha para continuar normalmente com a conta e com o programa.