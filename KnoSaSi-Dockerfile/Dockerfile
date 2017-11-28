# docker build .
# docker run --rm -p 7200:7200 dhlabbasel/graphdb-free
# docker rm -f $(docker ps -a -q)
# docker rmi $(docker images -q)


FROM nieine/sipi

#
# Install Knora Dependencies - taken from Dockerfile dhlabbasel - webapibase
#

# Silence debconf messages
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install apt https transport needed for bintray needed for sbt.
RUN \
  apt-get update && apt-get -y install apt-transport-https && \
  echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823

RUN \
  apt-get update && apt-get -y install \
  git \
  openjdk-8-jdk \
  sbt \
  sed \
  unzip \
  && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"

RUN git clone https://github.com/dhlab-basel/Knora.git

RUN cd /Knora/webapi && sbt compile

EXPOSE 3333


#
# Install Free GraphDB Dependencies - taken from Dockerfile dhlabbasle - graphdb-free
#

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get -qq update && \
  apt-get -y install \
    byobu curl git htop man vim wget unzip \
    openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"

# Install GraphDB-Free and clean up
RUN \
  curl -sS -o /tmp/graphdb.zip -L http://go.pardot.com/e/45622/7a-graphdb-free-8-3-1-dist-zip/4yxf7s/1143357223 && \
  unzip /tmp/graphdb.zip -d /tmp && \
  mv /tmp/graphdb-free-8.3.1 /graphdb && \
  git clone -b develop --single-branch --depth=1 https://github.com/dhlab-basel/Knora.git /knora && \
  cp /knora/webapi/scripts/KnoraRules.pie /graphdb && \
  rm /tmp/graphdb.zip && \
  rm -rf /knora

#RUN apt-get install expect

# Set GraphDB Max and Min Heap size
ENV GDB_HEAP_SIZE="4g"

EXPOSE 7200


#
# Install Angular Dependencies
#
RUN apt-get install expect -y
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g @angular/cli
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install yarn
RUN git clone https://github.com/dhlab-basel/Salsah.git
RUN cd /Salsah && yarn install --production=false
EXPOSE 4200

CMD ["/graphdb/bin/graphdb"]


#in the end:
#RUN cd /Knora/webapi/scripts && ./graphdb-free-init-knora-test.sh
#RUN cd /Knora/webapi && sbt compile
#RUN cd /Knora/webapi && sbt re-start
#RUN cd /Salsah/ && ng serve --host 0.0.0.0
#docker run --rm -p 7200:7200 -p 4200:4200 -p 3333:3333 -p 1024:1024 knosasi:latest /bin/bash -c "cd /Salsah; ng serve --host 0.0.0.0 "
#docker run --rm -p 7200:7200 -p 4200:4200 -p 3333:3333 -p 1024:1024 f213d851c354 /bin/bash -c "cd /Knora/webapi; sbt compile "~re-start allowResetTriplestoreContentOperationOverHTTP""