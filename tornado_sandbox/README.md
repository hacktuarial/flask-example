# Tornado

Tornado is its own Python web framework, and supports asynchonous operations.

# Running in one process

```{python}
python tornado_sandbox/app.py --port=8000
```

Then, to get a prediction, `curl -XPOST http://localhost:8000/api/v0/house_value -d @sample_request.json`


# Running in more than one process using nginx
First, install nginx and start it. I did this on a Mac:

```
brew install nginx
nginx
```

Now, start multiple python servers:

## non-docker
Simply run, in separate terminal windows,

```
python tornado_sandbox/app.py --port=8000
python tornado_sandbox/app.py --port=8001
```

## docker version
First, train the model. From the root directory of this repository:

```
mkdir artifacts
docker run --rm -w /flask-example -v `pwd`:/flask-example tsweetser/tornado:v0 python train.py
```

Run the docker containers. The arguments mean:
  * `-v`: mounting volumes for artifacts (the trained model) and the current working directory (our server code)
  * `--rm`: don't keep this container (to make an object-oriented analogy, docker image : docker container :: class : instance) after we stop it
  * `-p`: bind ports between host and container
  * `-m`: limit how much memory the container gets. This is important if you want to run a bunch of containers on one machine.

```
docker run -v ~/git/flask-example/artifacts:/artifacts -v `pwd`:/tornado_sandbox -w /tornado_sandbox --rm -p 8000:8000 -m 1g tsweetser/tornado:v0 python tornado_sandbox/app.py --port=8000
docker run -v ~/git/flask-example/artifacts:/artifacts -v `pwd`:/tornado_sandbox -w /tornado_sandbox --rm -p 8001:8001 -m 1g tsweetser/tornado:v0 python tornado_sandbox/app.py --port=8001
```

My nginx conf, at `/usr/local/etc/nginx`, looks as follows. It's based on the
[tornado example](https://www.tornadoweb.org/en/stable/guide/running.html?highlight=nginx)

```
user  nginx;
worker_processes  1;

events {
    worker_connections  1024;
}


http {
    upstream frontends {
        server 127.0.0.1:8000;
        server 127.0.0.1:8001;
    }
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    tcp_nopush     on;

    keepalive_timeout  65;

    gzip  on;

    server {
        listen       80;

        # / = route all traffic to...
        location / {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://frontends;
        }
    }
}
```

Now, to get predictions, you can run
`curl -XPOST http://localhost:80/api/v0/house_value -d @sample_request.json`
and nginx will route the requests to the different python servers. Amazing!

To stop nginx, run `nginx -s stop`
