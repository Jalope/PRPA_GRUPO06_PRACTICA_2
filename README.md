# PRPA_GRUPO06_PRACTICA_2
<b> MOTIVACIÓN </b><br>
Este repositorio se crea para la entrega de las práctica 2 en grupo, en el contexto de la asigantura de 4º Curso del Grado en Matemáticas: Programación Paralela, en la Universidad Complutense de Madrid.

<b> INTEGRANTES </b><br> 
  Blanco Martín, Raul
  
  López Gismeros, Javier
  
  Saiz Bautista, Daniel 

<hr>
<b> PROPUESTA </b><br>
<B> Programa elegido </b><br> 
En nuestro grupo hemos tomado la decisión de utilizar la librería pygame. Debido a que el
juego requiere de concurrencia hemos descartado cualquier juego por turnos. Por ello, vamos
a implementar un juego de disparos entre dos naves. El jugador que primero alcance a su
rival ganaría la partida.

<b> Paralelismo </b><br>
Dentro de la implementación usaremos la librería multiprocessing para poder encerrar
todas las acciones atómicas que puedan generar problemas.

<b> Concurrencia </b><br>
Implementaremos, como en el ejemplo que vimos en clase, un cliente/servidor de forma
que el juego pueda usarse bajo los principios de la programación concurrente, por dos ju-
gadores en la misma red. Para ello utilizaremos, de nuevo, la librería multiprocessing en
concreto de Listener y Client.
Posteriormente, una vez alcanzado el objetivo de la práctica con cliente/servidor, intenta-
remos hacer uso de la tecnología mqtt. Para ello haremos uso de paho.mqtt.publish como
se ha visto en clase.
<hr/>

<b>CARPETAS</b><br>
  juego_2_jugadores_local --> Primer intento para implementar la práctica. Se ha creado un juego de disparos entre dos naves con meteoritos que sirven para reguardarse del rival. Cada jugador tiene 3 vidas. Se generan pantallas de inicio y final. El juego continua una vez acabada cada partidia presionando cualquier tecla. 
  
  G2P_simplified --> Segunda intento de implementar la práctica. Simplificamos nuestro juego quitando algunas características, con el fin de que sea más sencillo generar los archivos sala.py y player.py. 
