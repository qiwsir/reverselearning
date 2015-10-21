#练习英语听写能力的小型网站

##功能

1. 用户注册/登录
2. 发布自己要练习的听力材料
>创建第一层级
>创建第二层级，并在该层级上发布音频和音频原文
>音频资料上传到七牛云上，文本保存在本地服务器的数据库中，并从七牛云反馈存储的URL保存到数据库

##数据库

users table

ID: user ID
username
password
logintime

firstclass table

ID
userid
classname

secondclass table

ID
userid
firstclassid
publishdatetime
audiourl
audiotext

result table

ID
userid
secondclassid
usertext

