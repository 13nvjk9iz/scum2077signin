# SCUM 2077 Auto Checkin

# Scum 2077服务器在线商城 每日签到 action ![SCUM2077](https://github.com/13nvjk9iz/scum2077signin/workflows/Scum2077Checkin/badge.svg)

## 友情链接

[SCUM2077服务器在线商城](http://2077.scumgame.cn:7998)
[每日签到脚本](https://github.com/13nvjk9iz/scum2077signin)

基于 Github Actions 的 [SCUM2077](http://2077.scumgame.cn:7998) 自动签到来增加渣币

## 功能

- 每日凌晨 12 点，18点定时签到
- 支持监控告警，具体配置文档查看[Server 酱](https://sct.ftqq.com/)，消息通道支持以下渠道
  - 企业微信应用消息
  - Android，
  - Bark iOS，
  - 企业微信群机器人
  - 钉钉群机器人
  - 飞书群机器人
  - 自定义微信测试号
  - 方糖服务号

## 使用方式

- Fork 本仓库
- 配置 hao4k 账户信息（由于是敏感信息，所以将其配置到了仓库 `setting/secrets` 下）
  - 找到 [.github/workflows/check-in.yml](https://github.com/13nvjk9iz/scum2077signin/blob/main/.github/workflows/check-in.yml) line 22, 23的两个 secret
    - USER
    - PWD
  - 配置到仓库的 `setting/secrets`
> 如果有多个账户，在USER以及PWD中使用英文半角逗号分隔（`,`），并且一一对应

## 自动同步上游代码

> fork 本项目后，使用下面方法自动同步上游代码

安装 Github App [Pull](https://github.com/apps/pull)， 将 fork 后的项目添加到 Repository access 列表中即可实现自动同步上游代码

## 开发

### 运行环境

- Python 3.9 +

## 欢迎SCUM玩家来2077纯PVE服一起玩！hhh
有新手礼包有各种活动有各种萌新保护，还有会叫欧尼酱的管理
![](https://cdn.jsdelivr.net/gh/13nvjk9iz/scum2077signin@main/img/1.png)
![](https://cdn.jsdelivr.net/gh/13nvjk9iz/scum2077signin@main/img/2.png)
![](https://cdn.jsdelivr.net/gh/13nvjk9iz/scum2077signin@main/img/3.png)
