FROM google/cloud-sdk:268.0.0

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get clean
RUN pip3 install -Iv slackclient==2.2.1
RUN pip3 install Flask

RUN apt-get -y install curl software-properties-common
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get -y install nodejs
RUN npm install -g newman

ADD devops_bot /devops_bot
ADD docker /docker

ENV BOT_ID="UJ01BKFA9"
ENV BOT_USER_OAUTH_ACCESS_TOKEN="xoxb-552755831923-612045661349-sR3LyonkWvm4I518Z3QNyn3e"

WORKDIR /devops_bot

CMD ["python3", "-u", "app.py"]