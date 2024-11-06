#  Nginx steps to deploy static website
```
sudo apt update
sudo apt install nginx
```
test
http://******（Replace with your server ip address）

Next we need to configure Nginx to load our static website. First, take a look at its default configuration file. The default configuration file is in /etc/nginx/conf.d/default.conf. We can use cat /etc/nginx/conf.d/default.conf to take a look at its contents. :

```
server {
    listen       80;
    server_name  localhost;

    #access_log  /var/log/nginx/host.access.log  main;
    
    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }
    
    #error_page  404              /404.html;
    
    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
    
    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}
    
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}
    
    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}

}
```
Can be changed to:
```
server {
    listen       80;
    server_name  watershoesfactory;

    #access_log  /var/log/nginx/host.access.log  main;
    
    location / {
        root   /var/www/html;
        index  index.html;
        try_files $uri $uri/ $uri.html =404;
    }
    gzip on;
    gzip_buffers 4 16k;
    gzip_comp_level 6;
    gzip_vary on;
    gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
    
    #error_page  404              /404.html;
    
    # redirect server error pages to the static page /50x.html
    #
    # error_page   500 502 503 504  /50x.html;
    # location = /50x.html {
    #     root   /usr/share/nginx/html;
    # }
    
    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}
    
    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}
    
    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}

}
```
Redeploy
```
nginx -s reload
```
```
git clone /path
git add .
git commit -m "***"
git push
```
```
cp -r /seoweb/* /var/www/html/
```

