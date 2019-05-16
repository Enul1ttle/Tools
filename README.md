## 渗透小工具
### windows
```
nc.exe                 #是kali linux里复制出来的。试了几个版本就这个能兼容反弹shell给linux的主机
lcx.exe                #端口转发工具
TV_getpass.exe         #TeamViewer密码获取
superdic-cr.exe        #字典生成
cmd.reg                #右键选择文件夹或文件，在该处打开cmd
```

### linux 
```
lcx                    #Linux 版本的lcx，已经编译好了，`chmod +x lcx `
lbd                    #从kaki 复制出来的，检测目标是否负载均衡
```


### 跨平台
```
portscanner.py         #扫描常见的危险端口，可配合proxychains 扫内网端口
```

### PHP
当PHP禁用命令函数时（php.ini 中用 disable_functions），把下面的两个文件上传到服务器，再访问bypass_disablefunc.php会有详细的使用介绍
```
bypass_disablefunc.php      
bypass_disablefunc_x64.so
```
