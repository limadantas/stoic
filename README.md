# SToIC - Services on Top of Interoperability Components

Bem-vindo ao repositório do SToIC, uma implementação do modelo de camada de portabilidade e interoperabilidade na camada de aplicação de plataformas de IoT proposto por Douglas Lima Dantas em sua dissertação de mestrado pela Engenharia de Computação pela EPUSP, sob a orientação da Prof. Drª Anarosa Alves Franco Brandão e Prof. Drª Lucia Filgueiras Vilela Leite.

A seguir, apresenta-se os arquivos de código-fonte disponíveis e a demonstração dos mesmos.

# Arquivos

**stoic-core**: Projeto que implementa o serviço central do SToIC (Core), contendo os adaptadores para as plataformas-alvo.

**stoic-front**: Projeto que implementa o SToIC Panel, para administração de instâncias de plataformas, dispositivos, entidades, associações, tarefas e gráficos.

**stoic-tangle**: Responsável por criar réplicas de entidades entre diferentes instâncias de plataformas.

**barulhometro**: Aplicação do Barulhômetro integrado ao SToIC.

# Plataformas suportadas

 1. Fiware
 2. IBM Watson IoT Platform

# Demonstração

Os seguintes links permitem observar uma demonstração da implementação:

 - [SToIC Panel](http://34.71.110.167:8000) (Usuário: **admin**, Senha: **admin**).
 - [Barulhômetro](http://34.71.110.167:3002)

Para visualizar dados no Barulhômetro, execute:

 - O script **largo_da_batata_fiware.sh** no shell **bash** para simular envio de dados do Largo da Batata através do Fiware.
 - O script python **ibirapuera_wiotp.py** para simular envio de dados do Ibirapuera através do Watson IoT Platform (utilize Python 3.7 e instale as bilbiotecas paho-mqtt e wiotp-sdk).

Qualquer problema durante a execução ou indisponibilidade do serviço, não hesite em enviar um e-mail.



