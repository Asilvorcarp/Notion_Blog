# Notion_Blog

<a href="http://choosealicense.com/licenses/mit/" rel="nofollow" one-link-mark="yes"><img src="https://camo.githubusercontent.com/dd1c858e94a371529a0a4c359bc95f18f09ba4a5fc0e658950bcb1383ea40fc9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d626c75652e7376673f7374796c653d666c6174" alt="MIT License" data-canonical-src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat" style="max-width:100%;"></a>

本项目用于快捷将Notion中的笔记同步到个人Blog上

## 适用Blog框架

目前仅适配Hexo (Hexo的.config.yaml中需要打开post对应资源文件夹的功能)

## 目前的实现方案

1. Hexo的.config.yaml中需要打开post对应资源文件夹的功能
2. 自行用Notion导出md和相关资源的压缩包 "Export-xxxxx.zip" 到_post文件夹_
3. 在_post文件夹内运行Notion_Blog.py
4. 之后的部署中即可自动匹配

## 存在的问题

Notion导出可能损失部分格式 - 待官方解决

## Todo

- [ ] 解决格式损失问题 改进为爬取Notion方案
- [ ] 自行导出太麻烦 改进为自动导出
- [ ] 目前运行目录在其他位置可能会出问题 待测试改进