# **Twitter-bot**

Ejercicio de programación en Python cuya finalidad (además de aprender y practicar) es publicar en Twitter/X **críticas ácidas, irracionales y 100% necesarias** a la gestión de **Santiago Baños** en el Club América 💛💙

## 🧠 **¿Por qué?**

Porque programar también es una forma de protesta. Este bot representa una mezcla de frustración, código limpio (a veces), y libertad de expresión vía API.  
Además, ¿quién no quiere automatizar su odio deportivo?

## 🔧 **¿Cómo funciona?**

Cada cierto tiempo —específicamente cuatro veces al día—, el bot se despierta, escoge una frase prearmada (o genera una nueva si se le acaban), y publica un tuit bien dirigido a la cabeza del América.  
Y si nadie lo detiene, lo seguirá haciendo... **para siempre**.

- Las frases se gestionan desde Redis ([otro contenedor](https://github.com/uedsoldier/redis-twitter-bot.git))
- El historial de publicaciones evita repeticiones (porque la creatividad también es digna)
- Corre dentro de un contenedor Docker, con `cron` como despertador fiel
- Todos los errores se imprimen (con odio) en logs

## 🗃️ **Variables de entorno**

Los datos necesarios tanto para la API de Twitter como para acceder a la instancia de Redis se colocan en un archivo `.env`, cuyos valores se trasladan automáticamente al contenedor Docker. Ejemplo:

#### Variables de entorno para el bot de Twitter
TWITTER_CONSUMER_KEY=TU_TWITTER_CONSUMER_KEY
TWITTER_CONSUMER_SECRET=TU_TWITTER_CONSUMER_SECRET
TWITTER_ACCESS_TOKEN=TU_TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET=TU_TWITTER_ACCESS_TOKEN_SECRET
TWITTER_BOT_LOGFILE=/var/log/twitter_bot.log

#### Variables de entorno para Redis
REDIS_HOST=redis-stack (nombre del [otro contenedor](https://github.com/uedsoldier/redis-twitter-bot.git))
REDIS_HOST_PORT=6379
REDIS_CONTAINER_PORT=6379
REDIS_ADMIN_USER=TU_REDIS_ADMIN_USER
REDIS_ADMIN_PASSWORD=TU_REDIS_ADMIN_PASSWORD

REDIS_INSIGHT_HOST_PORT=8001
REDIS_INSIGHT_CONTAINER_PORT=8001

#### Zona horaria del contenedor
TZ=America/Mexico_City


Sí, el `.env` es privado. **No se lo muestres a Santiago Baños.**

## 🐳 **Docker**

Todo el proyecto se ejecuta dentro de un contenedor Debian slim con Python 3.13, un contenedor Redis y tareas programadas con `cron`.

## ⏰ **Tareas programadas**

Cada 2 horas se publica un tweet.

Cada 30 minutos: el bot efectúa un healthcheck confirmar que sigue vivo.

Si el bot no publica por error o si Redis se cae, todo queda registrado.

## 📋 **Frases**
Las frases están en Redis y se rotan constantemente. Algunas son simples. Otras, groseras. Todas absolutamente necesarias.

## **🛠️ En desarrollo**
Francamente creo que cumple y hasta ahí se quedará el veneno. 🐍. Falta un poco de documentación que poco a poco irá apareciendo.

📚 **Tutorial básico**
Si quieres entender cómo montar esto desde cero (o estás aprendiendo), puedes ver este [tutorial básico en YouTube](https://www.youtube.com/watch?v=xsSXL5iuzDg)

## 🤖 **Créditos**

Las bases de este proyecto fueron realizadas en **un solo día** con la asistencia de inteligencia artificial (ChatGPT), lo cual permitió acelerar la escritura del código, automatización y documentación. Posteriormente me di a la tarea de optimizar y mejorar el código para poder reutilizar algunas cosas en futuros proyectos.

Sí, lo odio tanto (SB) como para automatizarlo en tiempo récord.

## 🐦 Autor

Sígueme (o mientame la madre) en [Twitter/X](https://x.com/uedsoldier)

## ⚠️ Disclaimer

Este proyecto es de naturaleza satírica y tiene fines educativos, de aprendizaje y humorísticos.  
No busca incitar al odio, acoso o violencia contra ninguna persona o institución.

Todo el contenido generado y publicado por el bot representa una forma de crítica subjetiva y libre expresión sobre temas deportivos.  
**Este repositorio no está afiliado, respaldado ni aprobado por el Club América, Twitter/X ni ninguna figura pública mencionada.**

Si alguien se siente ofendido por el contenido, se recomienda respirar profundo, reírse un poco y seguir con su día.

## ☠️ **Mensaje final**

CHTPM, Santiago Baños.
(Frase institucional del proyecto. No discutimos esta parte.)
