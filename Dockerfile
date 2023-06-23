FROM python:3.11-slim-buster

WORKDIR /app

# Gerekli paketleri yükleyin

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    wget \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    libu2f-udev \
    # libcurl3 \
    libcurl3-gnutls \
    libcurl3-nss \
    libcurl4 \
    libvulkan1 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y \
#     wget \
#     fonts-liberation \
#     libasound2 \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN dpkg -i ./google-chrome-stable_current_amd64.deb

COPY . .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Uygulama kodunuzu kopyalayın


# Docker konteynırının nasıl başlatılacağını belirtin
CMD [ "python", "./bot.py" ]
