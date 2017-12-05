FROM dhlabbasel/webapi-base:latest

MAINTAINER Ivan Subotic "ivan.subotic@unibas.ch"

# Get and build webapi release package, cleanup
RUN git clone https://github.com/dhlab-basel/Knora.git

RUN \
  cd /Knora/webapi && \
  sbt stage && \
  mkdir /webapi && \
  cp -r Knora/webapi/target/universal/stage/* /webapi && \
  rm -rf /Knora

VOLUME ["/localdata"]

# Expose the webapi default port
EXPOSE 3333

CMD ["/webapi/bin/webapi"]