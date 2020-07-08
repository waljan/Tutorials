# use ubuntu18.04 with CUDA10.1 as base image
FROM nvidia/cuda:10.1-base-ubuntu18.04

# use anaconda3 latest version as base image
#FROM continuumio/anaconda3:latest


# install anaconda3 (dockerfile from continuumio/anaconda3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

# install oracle instant client
#https://www.youtube.com/watch?v=_wab4By7P78

RUN apt-get update && apt-get install -y libaio1 wget
RUN apt-get install -y unzip

WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/19600/instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \
     unzip instantclient-basic-linux.x64-19.6.0.0.0dbru.zip && \
    rm -f instantclient-basic-linux.x64-19.6.0.0.0dbru.zip
RUN cd /opt/oracle/instantclient_19_6 && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci
RUN echo /opt/oracle/instantclient_19_6 > /etc/ld.so.conf.d/oracle-instantclient.conf && ldconfig
#RUN python -m pip install cx_Oracle # already specified in requirements.txt

ENTRYPOINT [ "/usr/bin/tini", "--" ]


# copy requirements file
COPY requirements.txt /project/
# set working directory
WORKDIR /project/


# install dependencies
RUN pip install -r requirements.txt

# copy the project
COPY . /project/

# open jupyter notebook
CMD jupyter-notebook --ip=0.0.0.0 --allow-root

# open bash terminal inside the container
# CMD /bin/bash
                      
