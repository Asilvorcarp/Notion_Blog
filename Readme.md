# Notion_Blog

本项目用于快捷将Notion中的笔记同步到个人Blog上

目前仅适配Hexo

目前的实现方案：

​	自行用Notion导出md和相关资源的压缩包 "Export-xxxxx.zip" 到_post文件夹

​	在_post文件夹内运行Notion_Blog.py

​	之后的部署中即可自动匹配

​	(Hexo的.config.yaml中需要打开post对应资源文件夹的功能)

存在的问题：

​	Notion导出可能损失部分格式 - 待官方解决

Todo：

- [ ] 解决格式损失问题 改进为爬取Notion方案
- [ ] 自行导出太麻烦 改进为自动导出
- [ ] 目前运行目录在其他位置可能会出问题 待测试与改进