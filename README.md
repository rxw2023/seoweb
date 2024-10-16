#  Nginx部署静态网站步骤

添加完 Nginx 的 apt 源之后，更新 apt，然后安装 Nginx：

```
sudo apt update
sudo apt install nginx
```

测试

http://******（替换为你的服务器 ip 地址）

接下来我们需要配置 Nginx，来让它加载我们的静态网站。首先看一下他的默认配置文件，默认配置文件在 /etc/nginx/conf.d/default.conf中，我们可以用 cat /etc/nginx/conf.d/default.conf来看一下它里面的内容：

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

可以改为：

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

重新部署

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

接下来是图片换图床的对应地址

https://p.sda1.dev/19/2192cc8828fd15cf538fd6e1975d0a81/freecompress-background.jpg

https://p.sda1.dev/19/ef28ca2b4702feac6d88e3071675e903/freecompress-background.jpg

https://p.sda1.dev/19/11c4558ab7c00725bc09939619ff5732/01- Child Water Shoes.jpg

https://p.sda1.dev/19/1cb62c25cb30b1cc6dc40b47a39b92ec/02- Child Water Shoes.jpg

https://p.sda1.dev/19/527cd1856be833622cb811f01f94160f/03- Child Water Shoes.jpg

https://p.sda1.dev/19/35a0665039b95eb138fb319be894db07/04- Child Water Shoes.jpg

https://p.sda1.dev/19/7e3704c587968a7234de148d7d175260/05-Child beach shoes.jpg

https://p.sda1.dev/19/a81d705d316297d2841340e34673074c/06- Child beach Shoes.jpg

https://p.sda1.dev/19/bd70963b472c1bb0d5afa880e1de0905/07-Child camp Shoes.jpg

https://p.sda1.dev/19/9d969cd9e0be06edef958c846cfb057d/08-Child Swim Shoes.jpg

https://p.sda1.dev/19/d9b0aa15e2151d46fbb8dcc3c2abdeab/01-Water Shoes.jpg

https://p.sda1.dev/19/a7225a8d1b567216b29689037404c671/02-Water shoes.jpg

https://p.sda1.dev/19/d36c0e9e0e10c58086b63f47ff3479b3/03-Water Shoes.jpg

https://p.sda1.dev/19/feb48069414bff5bfce8292b2d8d4baa/04-Water Shoes.jpg

https://p.sda1.dev/19/6ed7b37c8ac696e1d3bef165e8d4754e/05-Water shoes.jpg

https://p.sda1.dev/19/1ff3e307456948963f70fd6f3ee6a7fb/06-Water shoes.jpg

https://p.sda1.dev/19/a8dab5d91385e5761cedbf4b94cdadec/07-Water Shoes.jpg

https://p.sda1.dev/19/e0efa190050a2989fd6d3fcff9d174cb/08-Swim Shoes.jpg

https://p.sda1.dev/19/556d42fb0340dfb8791c590fea58397c/09- Swim Shoes.jpg

https://p.sda1.dev/19/9c4e15ed15a0a49a850a7bb653832f5f/10-Swim shoes.jpg

https://p.sda1.dev/19/8174d96a3e30dab73ed76999cc8b5927/11-Swim Shoes.jpg

https://p.sda1.dev/19/121fec9366a734aa43a9fb04fe65d19a/12- Camp shoes.jpg

https://p.sda1.dev/19/7fb5e68fc05dca9b55b4d4adfc4bec43/13- Camp Shoes.jpg

https://p.sda1.dev/19/54d09aeaf9565e2d54f1a2690fa121ef/14- Yoga Shoes.jpg

https://p.sda1.dev/19/2bec3bd3be03aad8de7e018356a51955/15- Squat Shoes.jpg

https://p.sda1.dev/19/795cc0e2fef60c0b820e13dedd5ae5c2/16-Sock shoes.jpg

https://p.sda1.dev/19/d805cf946afd6c4d34d746c056998edc/17- Sock Shoes.jpg

https://p.sda1.dev/19/08098b5c54c62d496da8aaaa6f2c0d8c/18- Swim Shoes.jpg

https://p.sda1.dev/19/831db14aaa5c2837f97d14e081ddf853/19-Water shoes.jpg

https://p.sda1.dev/19/f498df69850916b41cee31965011d6bd/20- Water shoes.jpg

https://p.sda1.dev/19/9886bbf77da7b7346afc6aab147f8eca/21- Water Shoes.jpg

