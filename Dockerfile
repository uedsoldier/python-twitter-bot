FROM python:3.13-slim

# Instala cron y dos2unix, elimina exim4
RUN apt-get update && apt-get install -y cron dos2unix --no-install-recommends && \
    apt-get remove -y exim4 exim4-base && \
    apt-get clean && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Establece directorio de trabajo
WORKDIR /app

# Copia requirements y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

COPY entrypoint.sh entrypoint.sh
COPY run_bot.sh run_bot.sh

# Convierte todos los archivos en /app a formato UNIX
RUN find /app -type f -exec dos2unix {} \;

# Asegura permisos del script principal y del entrypoint
RUN chmod +x /app/run_bot.sh
RUN chmod +x /app/entrypoint.sh

# Copia el archivo de cron y asegura formato correcto
COPY crontab.txt /etc/cron.d/bot-cron
RUN dos2unix /etc/cron.d/bot-cron && \
    echo "" >> /etc/cron.d/bot-cron && \  
    chmod 644 /etc/cron.d/bot-cron && \
    crontab /etc/cron.d/bot-cron

# Healthcheck docker
HEALTHCHECK --interval=1h --timeout=10s --start-period=5s --retries=3 \
  CMD python3 /app/src/twitter_healthcheck.py || exit 1

# Entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
