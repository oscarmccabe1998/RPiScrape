FROM fedora:latest

RUN dnf install -y \
        python3 \
        python3-pip \
        firefox \
        Xvfb \
        wget \
        && dnf clean all

RUN wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz \
        && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
        && chmod +x /usr/local/bin/geckodriver \
        && rm /tmp/geckodriver.tar.gz

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r req.txt
ENV DISPLAY=:99
CMD ["python3", "main.py"]