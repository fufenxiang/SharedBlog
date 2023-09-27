# 使用nginx代理实现静态资源访问

## Nginx 简介

nginx作为一款高性能的服务器，用途很多，除了可以做后端服务器的代理，负载均衡之外你，还有一个用途就是做静态资源的缓存服务器，比如在前后端分离的项目中，为了加速前端页面的响应速度，我们可以将前端的相关资源，例如html，js,css或者图片等放到nginx指定的目录下，访问的时候只需要通过IP加路径就可以实现高效快速的访问.

接下来介绍如何在windows下使用nginx作为静态资源服务器。

## 1. Nginx 安装

先去官网[https://nginx.org/en/download.html](https://nginx.org/en/download.html) 下载 Nginx 压缩包：

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-1.png" width="85%">

下载完成后，解压缩，运行cmd，使用命令进行操作，重要的事情说三遍，**不要直接双击nginx.exe，不要直接双击nginx.exe，不要直接双击nginx.exe**，一定要在dos窗口启动，不要直接双击nginx.exe，这样会导致修改配置后重启、停止nginx无效，需要手动关闭任务管理器内的所有nginx进程，再启动才可以。

使用命令到达nginx的解压缩后的目录：

```
cd c:\nginx-1.24.0
```

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-2.png" width="85%">

启动nginx服务，启动时会一闪而过是正常的

```
start nginx
```

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-3.png" width="60%">

查看任务进程是否存在，dos或打开任务管理器都行:

**dos:**

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-4.png" width="80%">

**任务管理器:**

打开任务管理器在进程中看不到nginx.exe的进程（双击nginx.exe时会显示在这里），需要打开详细信息里面能看到隐藏的nginx.exe进程

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-5.png" width="80%">

如果都没有可能是启动报错了查看一下日志，在nginx目录中的logs文件夹下error.log是日志文件

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-6.png" width="80%">


**常见错误**

(1) 端口号被占

(2) nginx文件夹路径含中文


## 2. Nginx 配置

修改配置文件，进入解压缩目录，直接文件夹点击进去即可，不需要从d

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-7.png" width="80%">

在conf目录下找到 nginx.conf 使用文本编辑器打开即可，找到 server 这个节点，修改端口号，如果有需求可以修改主页目录没有就不用修改

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-8.png" width="80%">

修改完成后保存，使用以下命令检查一下配置文件是否正确，后面是nginx.conf文件的路径，successful就说明正确了

```
nginx -t -c /nginx-1.24.0/conf/nginx.conf
```

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-9.png" width="80%">

如果程序没启动就直接start nginx启动，如果已经启动了就使用以下命令重新加载配置文件并重启

```
nginx -s reload 
```

之后就打开浏览器访问刚才的域名及端口http://localhost:80：

<img alt="Download Nginx" src="../../_static/imgs/nginx/install-nginx-10.png" width="80%">


## 3. Nginx 停止

关闭nginx服务使用以下命令，同样也是一闪而过是正常的，看一下是否进程已消失即可 

**快速停止**

```
nginx -s stop
```

**完整有序的关闭**

```
nginx -s quit
```


## 4. 优化配置

打开nginx.conf按照自己需求进行配置，下面列出简单的一些常规调优配置

```bash
#user  nobody;
 
#==工作进程数，一般设置为cpu核心数
worker_processes  1;
 
#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;
 
#pid        logs/nginx.pid;
 
 
events {
 
    #==最大连接数，一般设置为cpu*2048
    worker_connections  1024;
}
 
 
http {
    include       mime.types;
    default_type  application/octet-stream;
 
    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';
 
    #access_log  logs/access.log  main;
 
    sendfile        on;
    #tcp_nopush     on;
 
    #keepalive_timeout  0;
    
    #==客户端链接超时时间
    keepalive_timeout  65;
 
    #gzip  on;
 
    #当配置多个server节点时，默认server names的缓存区大小就不够了，需要手动设置大一点
    server_names_hash_bucket_size 512;
 
    #server表示虚拟主机可以理解为一个站点，可以配置多个server节点搭建多个站点
    #每一个请求进来确定使用哪个server由server_name确定
    server {
        #站点监听端口
        listen       8800;
        #站点访问域名
        server_name  localhost;
        
        #编码格式，避免url参数乱码
        charset utf-8;
 
        #access_log  logs/host.access.log  main;
 
        #location用来匹配同一域名下多个URI的访问规则
        #比如动态资源如何跳转，静态资源如何跳转等
        #location后面跟着的/代表匹配规则
        location / {
            #站点根目录，可以是相对路径，也可以使绝对路径
            root   html;
            #默认主页
            index  index.html index.htm;
            
            #转发后端站点地址，一般用于做软负载，轮询后端服务器
            #proxy_pass http://10.11.12.237:8080;
 
            #拒绝请求，返回403，一般用于某些目录禁止访问
            #deny all;
            
            #允许请求
            #allow all;
            
            #重新定义或者添加发往后端服务器的请求头
            add_header 'Access-Control-Allow-Origin' '*';
            add_header 'Access-Control-Allow-Credentials' 'true';
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
            add_header 'Access-Control-Allow-Headers' 'DNT, X-CustomHeader, Keep-Alive, User-Agent, 
            X-Requested-With, If-Modified-Since, Cache-Control, Content-Type';
            
            #给请求头中添加客户请求主机名
            proxy_set_header Host $host;

            #给请求头中添加客户端IP
            proxy_set_header X-Real-IP $remote_addr;
            #将$remote_addr变量值添加在客户端“X-Forwarded-For”请求头的后面，并以逗号分隔。 
            #如果客户端请求未携带 “X-Forwarded-For” 请求头，$proxy_add_x_forwarded_for 
            #变量值将与 $remote_addr 变量相同  
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            #给请求头中添加客户端的Cookie
            proxy_set_header Cookie $http_cookie;
            #将使用代理服务器的主域名和端口号来替换。如果端口是80，可以不加。
            proxy_redirect off;
            
            #浏览器对 Cookie 有很多限制，如果 Cookie 的 Domain 部分与当前页面的 Domain 不匹配就无法写入。
            #所以如果请求 A 域名，服务器 proxy_pass 到 B 域名，然后 B 服务器输出 Domian=B 的 Cookie，
            #前端的页面依然停留在 A 域名上，于是浏览器就无法将 Cookie 写入。
            
　　        #不仅是域名，浏览器对 Path 也有限制。我们经常会 proxy_pass 到目标服务器的
            #某个 Path 下，不把这个 Path 暴露给浏览器。这时候如果目标服务器的 Cookie 
            #写死了 Path 也会出现 Cookie 无法写入的问题。
            
            #设置“Set-Cookie”响应头中的domain属性的替换文本，其值可以为一个字符串、
            #正则表达式的模式或一个引用的变量
            #转发后端服务器如果需要Cookie则需要将cookie domain也进行转换，否则前端
            #域名与后端域名不一致cookie就会无法存取
　　　　　　 #配置规则：proxy_cookie_domain serverDomain(后端服务器域) nginxDomain(nginx服务器域)
            proxy_cookie_domain localhost .testcaigou800.com;
            
            #取消当前配置级别的所有proxy_cookie_domain指令
            #proxy_cookie_domain off;
            #与后端服务器建立连接的超时时间。一般不可能大于75秒；
            proxy_connect_timeout 30;
        }
 
        #error_page  404              /404.html;
 
        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
 
    }
    
　　#当需要对同一端口监听多个域名时，使用如下配置，端口相同域名不同，server_name也可以使用正则进行配置
　　#但要注意server过多需要手动扩大server_names_hash_bucket_size缓存区大小
　　server {
　　　　listen 80;
　　　　server_name www.abc.com;
　　　　charset utf-8;
　　　　location / {
　　　　　　proxy_pass http://localhost:10001;
　　　　}
　　}
　　server {
　　　　listen 80;
　　　　server_name aaa.abc.com;
　　　　charset utf-8;
　　　　location / {
　　　　　　proxy_pass http://localhost:20002;
　　　　}
　　}
}

```



## 参考

   [1] [Windows详细安装nginx部署教程](https://blog.csdn.net/wufaqidong1/article/details/131072120)

   [2] [怎么使用nginx代理实现静态资源访问](https://www.php.cn/faq/549298.html)

   [3] [使用ReadtheDocs搭建属于自己的博客](https://i4t.com/3587.html)

