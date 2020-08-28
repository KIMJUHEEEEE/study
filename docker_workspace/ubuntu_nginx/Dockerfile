FROM ubuntu:19.10

RUN apt-get update && apt-get install -y -q nginx

COPY index.html /usr/share/nginx/html/

CMD [ "nginx","-g","daemon off;" ]