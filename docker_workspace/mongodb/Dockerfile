FROM centos:centos7

# Set up mongodb yum repo entry
# https://www.liquidweb.com/kb/how-to-install-mongodb-on-centos-6/
RUN echo -e "\
[mongodb]\n\
name=MongoDB Repository\n\
baseurl=https://repo.mongodb.org/yum/redhat/7Server/mongodb-org/3.0/x86_64/\n\
gpgcheck=0\n\
enabled=1\n" >> /etc/yum.repos.d/mongodb.repo

# Install mongodb
RUN yum update -y && yum install -y mongodb-org

# Set up directory requirements
RUN mkdir -p /data/mongodb /var/log/mongodb /var/run/mongodb
VOLUME ["/data/mongodb", "/var/log/mongodb"]

# Expose port 27017 from the container to the host
EXPOSE 27017

# Start mongodb
ENTRYPOINT ["/usr/bin/mongod"]
CMD ["--port", "27017", "--dbpath", "/data/mongodb", "--pidfilepath", "/var/run/mongodb/mongod.pid"]
