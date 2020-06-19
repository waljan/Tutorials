# use anaconda3 latest version as base image
FROM continuumio/anaconda3:latest

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
