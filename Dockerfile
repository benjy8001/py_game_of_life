FROM debian:jessie

RUN apt-get -y update && apt-get upgrade -y
RUN apt-get install -y python3 python3-dev python3-pip python-pygame

RUN mkdir /shared

COPY . /shared/

RUN python3 -m pip install pip setuptools virtualenv --upgrade

RUN mkdir -p /mnt/apps/ && \
    virtualenv -p $(which python3) /mnt/apps/game_of_life && \
    echo "source /mnt/apps/game_of_life/bin/activate" >> /root/.bashrc && \
    /mnt/apps/game_of_life/bin/pip install pip setuptools --upgrade

RUN cd /shared && /mnt/apps/game_of_life/bin/pip install --quiet -r requirements.txt
RUN cd /shared && /mnt/apps/game_of_life/bin/python setup.py develop

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT /entrypoint.sh

ENV LANG C.UTF-8
ENV DISPLAY :0

VOLUME ["/shared"]
WORKDIR /shared