# OneBot v11 集成

## 用途

本插件优先支持 OneBot v11 适配器，用于接收群消息事件、解析 `Message` / `MessageSegment`、读取 `GroupMessageEvent.reply`，并发送查询结果。

## 关键输入

- 群消息事件：`GroupMessageEvent`
- 原始消息：`event.message` / `event.get_message()`
- `@` 段：`MessageSegment` 类型为 `at`
- 回复消息：`event.reply`
- 发送者信息：`event.sender.card` / `event.sender.nickname`
- 群与用户标识：`event.group_id` / `event.user_id`

## 输出路径

后续实现可能使用：

- 普通群消息：作为最稳回退。
- 合并转发：用于多条记录展示，但不能作为唯一可靠展示语义。
- 伪造转发节点：需要注意协议端是否支持用户头像、昵称和节点内容字段。

## 已知风险

- 部分协议端或客户端不稳定展示合并转发中的 `reply` 段。
- `@all` 不应被当成普通 QQ 号查询成员信息。
- 伪造转发节点字段名和展示能力在协议端之间可能有差异。
- 私聊合并转发 API 在部分协议端不可用，需要回退策略。

## 待设计

- `@all` 是展开为所有群成员，还是记录为单独目标并在查询时特殊展示。
- 合并转发失败后的回退输出格式。
- 图片、表情、文件、转发消息等复杂消息段如何摘要化。
