# Checkpoint-5-Edge

ALUNOS:

Otho Oliveira Cândido RM557054
Lucas Rodrigues de Queiroz RM556323
Felipe Men dos Santos RM557571

README: Arquitetura Inicial de uma Aplicação IoT
Introdução
A Internet das Coisas (IoT) é uma tecnologia que permite a interconexão de dispositivos físicos à internet, permitindo que eles coletem, compartilhem e transmitam dados. Esses dispositivos podem variar desde sensores ambientais, dispositivos domésticos inteligentes até veículos autônomos. A IoT possibilita que os dispositivos se comuniquem entre si e com servidores remotos, melhorando a automação, análise de dados e eficiência em vários setores.

Conceitos Fundamentais da IoT
Dispositivos Conectados (End Nodes): São os sensores, atuadores e dispositivos que coletam ou respondem a dados. Exemplos incluem sensores de temperatura, umidade, luminosidade, câmeras de segurança e lâmpadas inteligentes.

Protocolos de Comunicação: A comunicação entre dispositivos IoT geralmente acontece por protocolos como MQTT (Message Queuing Telemetry Transport), HTTP, ou CoAP (Constrained Application Protocol). Esses protocolos garantem que os dados sejam transmitidos de maneira eficiente e segura.

Gateway: O gateway é responsável por conectar os dispositivos IoT à internet, retransmitindo dados coletados dos dispositivos para uma plataforma de processamento ou armazenamento.

Plataforma de IoT (Backend): A plataforma é onde os dados coletados pelos dispositivos são processados, armazenados e visualizados. Exemplos de plataformas incluem o FIWARE, Azure IoT Hub, e AWS IoT Core. Essas plataformas permitem a configuração de dispositivos, armazenamento de dados, análise, e gerenciamento de comunicações.

Dashboard ou Aplicações de Visualização: Essas são interfaces que permitem visualizar os dados coletados pelos dispositivos de IoT, geralmente de forma gráfica, permitindo a análise e o controle dos dispositivos.

Arquitetura Adotada para a Aplicação IoT
A arquitetura de uma aplicação IoT normalmente segue a estrutura abaixo:

Dispositivos IoT (Sensores/Atuadores): São os dispositivos que coletam dados (como temperatura e umidade) e transmitem essas informações. Eles podem ser conectados diretamente à internet ou por meio de gateways.

Gateway IoT: Esse componente serve como intermediário entre os dispositivos e a plataforma de IoT. O gateway coleta dados dos sensores e os envia para a plataforma de IoT por meio de protocolos de comunicação (como MQTT).

Plataforma de IoT (Servidor ou Cloud IoT): É onde os dados enviados pelos gateways ou dispositivos IoT são recebidos, processados, armazenados e analisados. Plataformas como o Azure IoT Hub ou FIWARE fornecem APIs para coleta e envio de dados, permitindo a integração fácil com outros serviços ou dashboards.

Armazenamento e Análise de Dados: Os dados coletados são armazenados em bancos de dados ou repositórios, onde podem ser processados e analisados. Ferramentas de análise permitem extrair insights dos dados coletados e detectar padrões.

Dashboard ou Interface do Usuário: Este é o ponto de contato final onde os usuários podem visualizar os dados coletados de seus dispositivos IoT. Isso é feito normalmente através de dashboards web, como o Dash do Python, que permite visualizações interativas e atualizações em tempo real.

Passos para Configurar uma Aplicação IoT
1. Configuração de Dispositivos IoT
Selecionar Hardware: Escolha o hardware apropriado (por exemplo, ESP32, Arduino, ou Raspberry Pi).
Conectar Sensores/Atuadores: Conecte sensores ao hardware, como sensores de temperatura (DHT-22), luminosidade (LDR), ou outros.
Programar Dispositivos: Escreva o código necessário para coletar dados dos sensores e configurar a comunicação com a plataforma IoT. Esse código geralmente inclui bibliotecas específicas para comunicação (como WiFi.h, PubSubClient.h para MQTT).
2. Configurar a Plataforma de IoT (Ex: Azure IoT Hub)
Criar um Hub IoT: No painel de controle da sua plataforma (ex: Azure, AWS, FIWARE), crie um novo hub de IoT, que atuará como o centro de comunicação para os dispositivos.
Registrar Dispositivos: Adicione dispositivos (como ESP32) ao hub para permitir que eles se comuniquem com a plataforma. Isso geralmente envolve gerar connection strings ou tokens de autenticação (como SAS Token no Azure).
Definir Protocolos de Comunicação: Configure o protocolo que será usado pelos dispositivos para enviar dados ao hub (ex: MQTT ou HTTP).
3. Comunicação e Envio de Dados
Configurar Conexão Wi-Fi e MQTT: Nos dispositivos, configure a conexão com a internet (Wi-Fi) e a comunicação MQTT para enviar dados ao hub. Isso é feito através de bibliotecas de software (PubSubClient para MQTT).
Enviar Dados para a Plataforma: Programe os dispositivos para ler dados dos sensores periodicamente e enviá-los para a plataforma IoT usando os protocolos definidos.
4. Processamento e Armazenamento de Dados
Receber e Armazenar Dados: Na plataforma IoT, os dados são recebidos e armazenados em tempo real. Eles podem ser armazenados em um banco de dados para análise posterior.
Análise e Processamento de Dados: Ferramentas de análise (ex: Pandas para Python) podem ser usadas para processar os dados, gerar alertas ou insights úteis para os usuários.
5. Desenvolvimento de Dashboard para Visualização
Configurar Dashboard: Utilize uma ferramenta como Dash para criar visualizações dos dados coletados. Isso pode incluir gráficos de linha para dados ao longo do tempo, medidores de valores em tempo real, ou outras visualizações.
Atualização em Tempo Real: Programe o dashboard para buscar dados atualizados da plataforma IoT em intervalos regulares, mantendo a visualização sempre atualizada.
