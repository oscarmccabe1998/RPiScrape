FROM debian

RUN apt-get update && apt-get install && apt-get install curl -y
RUN apt-get install firefox-esr -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY . . 
RUN pip3 install -r req.txt --break-system-packages
RUN curl -s -L curl -s https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux-aarch64.tar.gz | tar -xz
 
RUN mv geckodriver /usr/local/bin
RUN cd /usr/local/bin && chmod +x geckodriver; cd


ENTRYPOINT [ "python3", "main.py" ]