# Odometria Visual

# Requisitos
instalar bibliotecas:   
numpy,  
cv2,  
urllib,  
python 2.7,  
App Android - IP Webcam

# Codigo Python

 O codigo da odometria visual nada mais é que ma forma de localização de um determinado objeto ou qualquer equipamento que utilza câmera para se orientar. Nesse trabaho foi utilizado em um aplicativo anfroid chamado IP Webcam, onde ele tem acesso a câmera do celular  e por meio de um IP fornecido pelo app é possivel ver a movimentação da do equipamento e traçar coordenadas por onde passa. É necessario que tanto o celular como PC que estiver a programação estejam na mesma rede de internet para funcionar.

Apos instalação executar:

Teste1.py
![ Image ](https://user-images.githubusercontent.com/33470576/59888472-4e57bf00-939e-11e9-9a9e-cb5313140856.jpeg)

No codigo Teste 1.2, o codigo armazena as cordenadas x, y e z mostradas no visual odometrico e armazena em um arquivo txt.

![WhatsApp Image 2019-06-20 at 21 45 32](https://user-images.githubusercontent.com/33470576/59889906-ff615800-93a4-11e9-8158-b13efb488933.jpeg)
# Requisitos
instalar bibliotecas:

math
# Codigo Controle do dorne
O codigo de controle do drone tem como função dar a angulação e o quanto do drone deve avançar. Sendo os dois primeiros ifs, as primeiras duas coordenadas,responsaveis por da a angulação, considerando que sempre partirar do ponto (0,0) e os restantes dos ifs responsaveis por calcular as distancias entre os tres pontos, formando um triangulo, calulando assim o angulo menos 180 de tres pontos da corrdenada ate a ultima. Traçando toda a trajetória do drone. 
Apos instalação executar:

CONTROLEdrone.py
