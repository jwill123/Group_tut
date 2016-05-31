FROM ubuntu:precise
MAINTAINER Us

RUN apt-get update \
    && apt-get install -y software-properties-common python-software-properties \
    && add-apt-repository ppa:fkrull/deadsnakes \
    && apt-get update \
    && apt-get install -y python2.7 \
    && alias python=/usr/bin/python2.7


# This adds the python script from the host to the Docker image
# Any folders/files being added must be added from within the build
# context or it subdirectories because "the first step of docker build
# is to send the context directory/subdirectories to the docker daemon.
ADD visioner.py /usr/local/src/visioner.py

# This creates a default command that is
# run when the container is run without arguments
# It will call the python interpreter so we can run some script
ENTRYPOINT ["python"]

# This will be the default argument to the ENTRYPOINT
# If we type   $ docker run -ti <image_name>
# with no arguments, it will run this script by default.
# If we add other scripts here we can simply type
#   $ docker run -ti <image_name> <other_script.py>
CMD ["/usr/local/src/visioner.py"]
