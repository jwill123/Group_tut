FROM ubuntu:precise
MAINTAINER Us

RUN apt-get update \
    && apt-get install -y software-properties-common python-software-properties \
    && add-apt-repository ppa:fkrull/deadsnakes \
    && apt-get update \
    && apt-get install -y python2.7 \
    && alias python=/usr/bin/python2.7

#wget \
#    && apt-get install -y bzip2 \
#    && apt-get install -y tar \
#    && apt-get install -y build-essential \
#    && apt-get install -y zlib1g-dev
ADD ../src/visioner.py /usr/local/src/visioner.py
# this downloads the bwa source, makes it, moves it into place, then removes
# the downloads in one transaction to make sure downloads do not remain
# in the image
CMD python /usr/local/src/visioner.py

# this creates a default command that gets
# run when the container is run without arguments
# it will print the usage + version of bwa and exit
#ENTRYPOINT ["bwa"]
