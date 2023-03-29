# Python_semaforos
### Francisco Ogando (2021-0160)
[Link a mi explicación](https://miucateciedu-my.sharepoint.com/personal/20210160_miucateci_edu_do/_layouts/15/onedrive.aspx?login_hint=20210160%40miucateci%2Eedu%2Edo&id=%2Fpersonal%2F20210160%5Fmiucateci%5Fedu%5Fdo%2FDocuments%2FLab%20sist%20operativo%2FExplicaci%C3%B3n%5FSem%C3%A1foros%2Eavi&parent=%2Fpersonal%2F20210160%5Fmiucateci%5Fedu%5Fdo%2FDocuments%2FLab%20sist%20operativo)

*Esta es mi documentación sobre el código en Python que usted compartió maestro Lizandro, en primer lugar utiliza la biblioteca de subprocesos (threads) para crear varios hilos que ejecutan un bloque de código simultáneamente. El objetivo es ilustrar el uso del objeto Semaphore para sincronizar el acceso a un recurso compartido (en este caso, la lista 'd').¨*

*Además se importa la biblioteca threading y el método sleep de la biblioteca time. Luego se crea un objeto Semaphore con un valor inicial de 2, lo que significa que sólo dos hilos pueden acceder al recurso compartido al mismo tiempo.*

*A continuación se define una clase 'hilo' que hereda de threading.Thread y se sobrescribe su método 'run'. Este método es el que se ejecuta cuando se inicia el hilo, y en este caso, cada hilo adquiere el semáforo antes de esperar un número de segundos (calculado como 3 menos el identificador del hilo) y añade su identificador a la lista 'd' antes de liberar el semáforo.*

*Después se crea una lista de tres hilos con identificadores 1, 2 y 3, y se inicia cada uno de ellos con el método 'start'. Luego se espera durante 4 segundos antes de adquirir el semáforo, imprimir la lista 'd' y liberar el semáforo.*

*En resumen, este código crea tres hilos que acceden a un recurso compartido de manera sincronizada utilizando un objeto Semaphore. Cada hilo espera un tiempo diferente antes de añadir su identificador a la lista compartida, y se garantiza que sólo dos hilos puedan acceder al recurso compartido al mismo tiempo.*
