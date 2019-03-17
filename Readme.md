# 说明
项目的目的是提供一个图库功能, 所有的图片使用 http 进行访问. 方便在 linux 编写文档使用. 特别是 markdown 或 tex.

对于保存到指定的目录的图片(截图或复制)可以自动上传到 upyun 存储. 并生成 URL, 并把 URL 复制到 clipboard.
并产生系统提示.

在设计上有 public 与 private 两个目录. 分别保存公开与私有的图处. private 的图片在本地保存, 使用本地的 web
服务提供访问. public 使用上面的方案自动同步到去端.


# 配置

配置文件在 ~/.httppic.json 下面.


```
{
	"private": "/Pictures/Private",
	"public": "/Pictures/Public",
        "upyun":{
            "user": "",
            "password": "",
            "bucket": ""
        },
        "domain": "domain"
}
```


