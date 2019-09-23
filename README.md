# resttest
docker build -t <img_name> .

docker run -d --rm -p 8000:8000 <img_name>

makemigrations **not** built in:

docker exec -ti <container> bash

# important
token method forces pw to be in code. This may be avoided, but only by a lot of hassle. There is simply no data here to protect. Feel free to "crack" away.

# the example model
_Example_

field1,field2: charfield

field3: booleanfield

field4: intergerfield

field5: TextField

created: timestamp
