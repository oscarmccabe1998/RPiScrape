FROM ubuntu

RUN apt-get update && apt-get install && apt-get install curl -y
RUN apt-get install firefox -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY . . 
RUN pip3 install -r req.txt
RUN curl -s -L curl -s https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz | tar -xz
 
RUN mv geckodriver /usr/local/bin
RUN cd /usr/local/bin && chmod +x geckodriver; cd
RUN export PATH=$PATH:/usr/local/bin/geckodriver
#RUN source .bashrc

ENTRYPOINT [ "python3", "main.py" ]
