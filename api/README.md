Analytics Engine API
=============

uwsgi --pidfile uwsgi_serv.pid -d file.log -p 2 --socket 0.0.0.0:8888 --enable-threads --protocol=http -w wsgi

uwsgi -p 2 --socket 0.0.0.0:5555 --enable-threads --protocol=http -w wsgi

tail file.log
