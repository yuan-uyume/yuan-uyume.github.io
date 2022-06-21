---
title: Yuan u Yume的垃圾桶
date: 2022-06-17 14:51:17
---
# 这里是垃圾桶
- [x] 存放垃圾
- [x] 不要生气（生气寿命-1s）
## 垃圾桶的诞生~duang!
在很久很久以前，22年的6月17日。卑劣的垃圾桶之主窃取了[Ruri Shimotsuki @優萌初華](https://shoka.lostyu.me/about/yume) 的hexo主题！！！垃圾桶诞生了！！！
## 垃圾桶在哪里？
- [github](https://github.com/yuan-uyume/yuan-uyume.github.io)
# 垃圾桶怎麼建？
- 安裝hexo
- 安裝主題shoka
- 配置hexo和shoka
- 准备github仓库配置page
- 生成网页发布到github
## 环境准备
- **如果未安装node.js请前往 http://nodejs.cn/download/ 下载安装node**
- **如果未安装git请前往 https://git-scm.com/download 下载安装git**
## 安裝hexo
在心怡的目录下打开cmd
```bash
# 创建安装目录,dirName为目录名称
md dirName
# 加快安装过程
npm i cnpm -g
# 安装hexo
cnpm i hexo-cli -g
# hexo初始化
hexo init
# 安装组件
cnpm install
```
## 安裝主題shoka
> shoka主题项目地址 https://github.com/amehime/hexo-theme-shoka
```bash
# 镜像 git clone https://hub.fastgit.xyz/amehime/hexo-theme-shoka.git ./themes/shoka
git clone https://github.com/amehime/hexo-theme-shoka.git ./themes/shoka
```
## 配置hexo和shoka
> shoka配置文档 https://shoka.lostyu.me/categories/computer-science/note/theme-shoka-doc/
- [Hexo主题Shoka & multi-markdown-it渲染器使用说明](https://shoka.lostyu.me/computer-science/note/theme-shoka-doc/)
- [Step.1 依赖插件](https://shoka.lostyu.me/computer-science/note/theme-shoka-doc/dependents/)
- [Step.2 基本配置](https://shoka.lostyu.me/computer-science/note/theme-shoka-doc/config/)
- [Step.3 界面显示](https://shoka.lostyu.me/computer-science/note/theme-shoka-doc/display/)
- [Step.4 主题特殊功能](https://shoka.lostyu.me/computer-science/note/theme-shoka-doc/special/)
### 目录结构
  ![目录结构](https://s2.loli.net/2022/06/17/gH5e1CkMZnt9SmW.jpg)
### 插件安装
内容整合于[Step.1 依赖插件](https://shoka.lostyu.me/computer-science/note/theme-shoka-doc/dependents/)
```bash
cnpm un hexo-renderer-marked --save
cnpm i hexo-renderer-multi-markdown-it --save
cnpm i hexo-autoprefixer --save
cnpm i hexo-algoliasearch --save
cnpm i hexo-symbols-count-time --save
cnpm i hexo-feed --save-dev
```
### 特殊问题说明
1. 邮箱hash值？
> 在线md5哈希 https://tool.ip138.com/hash/

32位md5哈希算法，小写字母

2. hexo git报错
安装hexo-deployer-git
```bash
cnpm i hexo-deployer-git --save
```
### 参考配置文件
配置中用到其他网站api，需要去获取相应的appID和appKey
- [LeanCloud](https://console.leancloud.cn/login) 用于数据储存
- [Algolia](https://www.algolia.com/account/api-keys) 用于文章搜索

hexo参考配置
```yaml
# Hexo Configuration
## Docs: https://hexo.io/docs/configuration.html
## Source: https://github.com/hexojs/hexo/

# Site
title: 嗨~垃圾桶在哪？
subtitle: '舒服的家'
description: 'uyume a i shi te ru'
#站点关键词，用 “,” 分隔
keywords: anime,draw,uyume
author: Yuan u Yume
language: zh-CN
timezone: 'Asia/Shanghai'

# URL
## Set your site url here. For example, if you use GitHub Page, set url as 'https://username.github.io/project'
url: 
permalink: :year/:month/:day/:title/
permalink_defaults:
pretty_urls:
  trailing_index: true # Set to false to remove trailing 'index.html' from permalinks
  trailing_html: true # Set to false to remove trailing '.html' from permalinks

# Directory
source_dir: source
public_dir: public
tag_dir: tags
archive_dir: archives
category_dir: categories
code_dir: downloads/code
i18n_dir: :lang
skip_render:

# Writing
new_post_name: :title.md # File name of new posts
default_layout: post
titlecase: false # Transform title into titlecase
external_link:
  enable: true # Open external links in new tab
  field: site # Apply to the whole site
  exclude: ''
filename_case: 0
render_drafts: false
post_asset_folder: false
relative_link: false
future: true
#  停用默认代码高亮功能，否则代码块的 mac 样式不能正常显示。
#  找到 highlight 和 prismjs ，把 enable 改成 false 。
highlight:
  enable: false
  line_number: true
  auto_detect: false
  tab_replace: ''
  wrap: true
  hljs: false
prismjs:
  enable: false
  preprocess: true
  line_number: true
  tab_replace: ''

# Home page setting
# path: Root path for your blogs index page. (default = '')
# per_page: Posts displayed per page. (0 = disable pagination)
# order_by: Posts order. (Order by date descending by default)
index_generator:
  path: ''
  per_page: 10
  order_by: -date

# Category & Tag
default_category: uncategorized
category_map:
#  垃圾桶: about
tag_map:
#  垃圾桶: about
# Metadata elements
## https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta
meta_generator: true

# Date / Time format
## Hexo uses Moment.js to parse and display date
## You can customize the date format as defined in
## http://momentjs.com/docs/#/displaying/format/
date_format: YYYY-MM-DD
time_format: HH:mm:ss
## updated_option supports 'mtime', 'date', 'empty'
updated_option: 'mtime'

# Pagination
## Set per_page to 0 to disable pagination
per_page: 10
pagination_dir: page

# Include / Exclude file(s)
## include:/exclude: options only apply to the 'source/' folder
include:
exclude:
ignore:

# Extensions
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: shoka

# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  - type: git
    repo: 
    branch: master
#  - type: git
#    repo: 
#    branch: master

#加入 markdown 配置，用来渲染 md 文件
markdown:
  render: # 渲染器设置
    html: false # 过滤 HTML 标签
    xhtmlOut: true # 使用 '/' 来闭合单标签 （比如 <br />）。
    breaks: true # 转换段落里的 '\n' 到 <br>。
    linkify: true # 将类似 URL 的文本自动转换为链接。
    typographer:
    quotes: '“”‘’'
  plugins: # markdown-it 插件设置
    - plugin:
        name: markdown-it-toc-and-anchor
        enable: true
        options: # 文章目录以及锚点应用的 class 名称，shoka 主题必须设置成这样
          tocClassName: 'toc'
          anchorClassName: 'anchor'
    - plugin:
        name: markdown-it-multimd-table
        enable: true
        options:
          multiline: true
          rowspan: true
          headerless: true
    - plugin:
        name: ./markdown-it-furigana
        enable: true
        options:
          fallbackParens: "()"
    - plugin:
        name: ./markdown-it-spoiler
        enable: true
        options:
          title: "你知道得太多了"

#加入 minify 配置，压缩 css/js/html
minify:
  html:
    enable: true
    exclude: # 排除 hexo-feed 用到的模板文件
      - '**/json.ejs'
      - '**/atom.ejs'
      - '**/rss.ejs'
  css:
    enable: true
    exclude:
      - '**/*.min.css'
  js:
    enable: true
    mangle:
      toplevel: true
    output:
    compress:
    exclude:
      - '**/*.min.js'
      -

#缺少这个插件，首页卡片翻转效果在部分浏览器中无法正确显示。
autoprefixer:
  exclude:
    - '*.min.css'

# algolia 配置建议
algolia:
  appId: 
  apiKey: 
  adminApiKey: 
  chunkSize: 5000
  indexName: 
  fields:
    - title #必须配置
    - path #必须配置
    - categories #推荐配置
    - content:strip:truncate,0,2000
    - gallery
    - photos
    - tags

#feed 配置建议
feed:
  limit: 20
  order_by: "-date"
  tag_dir: false
  category_dir: false
  rss:
    enable: true
    template: "themes/shoka/layout/_alternate/rss.ejs"
    output: "rss.xml"
  atom:
    enable: true
    template: "themes/shoka/layout/_alternate/atom.ejs"
    output: "atom.xml"
  jsonFeed:
    enable: true
    template: "themes/shoka/layout/_alternate/json.ejs"
    output: "feed.json"

#symbols_count_time:
#  symbols: true
#  time: true
#  total_symbols: true
#  total_time: true
#  exclude_codeblock: false
#  awl: 4
#  wpm: 275
#  suffix: "mins."
```
shoka配置
```yaml
alternate: Yuan u Yume
statics: / #//cdn.jsdelivr.net/gh/amehime/shoka@latest/
css: css
js: js
images: images
loader:
  start: true # 当初次打开页面时，显示加载动画
  switch: false # tab 切换到其他页面时，显示加载动画
fireworks:
  enable: true # 是否启用
  color: # 烟花颜色
    - "rgba(255,182,185,.9)"
    - "rgba(250,227,217,.9)"
    - "rgba(187,222,214,.9)"
    - "rgba(138,198,209,.9)"
font:
  enable: true
  family: ic
  global:
    external: true
    family: Mulish
    size:
  # Font settings for alternate title.
  logo:
    external: true
    family: Fredericka the Great
    size: 3.5
  # Font settings for site title.
  title:
    external: true
    family: Noto Serif JP
    size: 2.5
  # Font settings for headlines (<h1> to <h6>).
  headings:
    external: true
    family: Noto Serif SC
    size:
  # Font settings for posts.
  posts:
    external: true
    family:
  # Font settings for <code> and code blocks.
  codes:
    external: true
    family: Inconsolata
#iconfont: "1832207_c8i9n1ulxlt"
menu:
  home: / || home
  about: /about/ || user
  posts:
    default: / || feather
    archives: /archives/ || list-alt
    categories: /categories/ || th
    tags: /tags/ || tags
  # friends: /friends/ || heart
  # links: /links/ || magic

social:
  github: #https://github.com/yuan-uyume || github || "#191717"
  bilibili: #https://space.bilibili.com/140490285 || sakura || "#1e88e5"
  music: #https://music.163.com/#/user/home?id=1288901248 || cloud-music || "#e60026"
  about: #https://yuan-uyume.github.io//2022/06/17/Yuan-u-Yume/ || address-card || "#3b5998"
  email: #mailto:dakerj@qq.com || envelope || "#55acd5"


sidebar:
  # Sidebar Position.
  position: right
  #position: right
  # Replace the default avatar image and set the url here.
  avatar: avatar.jpg

widgets:
  random_posts: true # 显示随机文章
  recent_comments: true # 显示最近评论

# 页尾全站统计
footer:
  since: 2022
  count: true
# 文章界面统计
post:
  count: true

# 评论系统
valine:
  appId: 
  appKey: 
  placeholder: ヽ(○´∀`)ﾉ♪ # Comment box placeholder
  avatar: mp # Gravatar style : mp, identicon, monsterid, wavatar, robohash, retro
  pageSize: 10 # Pagination size
  lang: zh-CN
  visitor: true # 文章访问量统计
  NoRecordIP: false # 不记录 IP
  serverURLs: # When the custom domain name is enabled, fill it in here (it will be detected automatically by default, no need to fill in)
  powerMode: true # 默认打开评论框输入特效
  tagMeta:
    visitor: 一般路过吃瓜群众
    master: 垃圾桶之主
    friend: 正义的伙伴
    investor: 环保局长
  tagColor:
#    visitor: "#855194"
#    master: "#a77c59"
#    investor: "#ed6ea0"
    master: "var(--color-orange)"
    friend: "var(--color-aqua)"
    investor: "var(--color-pink)"
  tagMember:
    master:
      #- 58a34de1858595ed1524017dc7fafac3
    friend:
    # - hash of friend@email.com
    investor:
    # - hash of investor1@email.com

# 页面音乐
audio:
  - title: #灯呦丶2021
    list:
      #- https://music.163.com/#/playlist?id=7175381197
  - title: #灯呦丶2020
    list:
      #- https://music.163.com/#/playlist?id=5437015204
```
## 准备github仓库配置page
创建一个名为 XXX.github.io 的仓库， XXX为你的github用户名

将仓库地址填入hexo配置文件中去

可参考 https://zhuanlan.zhihu.com/p/76063614
## 生成网页发布到github
发布命令流程
```bash
# 清除生成的静态页面,可以不用
hexo clean
# 生成静态页面
hexo g
# 将静态页面推送到配置的远程仓库
hexo d
```
本地服务
```bash
hexo s
```