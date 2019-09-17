FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
#copy only needed here to cacheable
COPY ./requirements.txt /code/
RUN pip install -r /code/requirements.txt
# EXPOSE port 8000 to allow communication to/from server
# this is more info than effect; ports still need to be mapped in docker run
EXPOSE 8000
# copy all the rest here ; above commands in cache 99.9%
COPY . /code/
# CMD specifcies the command to execute to start the server running.
CMD ["/code/start.sh"]
# done!
