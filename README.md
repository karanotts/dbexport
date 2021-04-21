# dbexport

Simple python script to work with SQLAlchemy

## Install docker 
run ```docker_setup_apt.sh``` for Debian/Ubuntu

run ```docker_setup.yum.sh``` for RedHat/CentOS

## Set up database 
run ```db_setup.sh``` and set postrges username and password when prompted

## Interact with database
Database URI > "postgresql://{username}:{password}@{hostname or hostIP}:{port}/reviews"
Port bindings are :5432 or :6080 and :80 - recommended for public IPs where default Postgres port is not enabled

defautl URI is ```postgresql://user:password@localhost:5432/reviews```
```
(dbexport) $ DB_URL="postgresql://user:password@localhost:5432/reviews" PYTHONPATH=. python
>>> from dbexport.config import Session
>>> session = Session()
>>> session
<sqlalchemy.orm.session.Session object at 0x10c0c6f28>
>>> session.bind
Engine(postgresql://user:***@localhost:5432/reviews)
```