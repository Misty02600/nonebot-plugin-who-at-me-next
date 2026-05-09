# 技术上下文

## 技术栈

- Python `>=3.11`：插件运行目标。
- NoneBot2 `>=2.4.2,<3.0.0`：机器人框架。
- OneBot v11 adapter：当前模板测试依赖，后续业务优先支持 OneBot v11。
- `uv` / `uv_build`：依赖管理与构建。
- `ruff`：格式化与 lint。
- `basedpyright`：类型检查。
- `pytest` / `nonebug`：单元测试与 NoneBot 行为测试。

## 开发设置

- 本地仓库：`E:\Dev\Projects\MigutBot\nonebot-plugin-who-at-me-next`
- GitHub 仓库：`https://github.com/Misty02600/nonebot-plugin-who-at-me-next`
- 插件包名：`nonebot-plugin-who-at-me-next`
- Python 包模块：`nonebot_plugin_who_at_me_next`
- 当前模板测试命令：`uv run pytest`

## 依赖

当前 `pyproject.toml` 仅保留基础依赖：

- `nonebot2>=2.4.2,<3.0.0`

后续可能引入：

- `nonebot-adapter-onebot`：作为运行依赖还是测试依赖需在实现前确认。
- `nonebot-plugin-localstore`：用于插件数据目录。
- SQLite / `msgspec` / `pydantic`：用于结构化持久化和配置，待设计时确认。
- `nonebot-plugin-alconna`：若采用更严格且可扩展的命令注册。

## 约束

- 不复用旧插件把 `Message` 直接写入文本字段的做法。
- 不依赖协议端一定能正确渲染嵌套 `reply` 段。
- 不在插件入口文件中堆叠业务逻辑。
- 优先使用 adapter 原生 `Message` / `MessageSegment` 对象和 API payload。
- 测试应避免在 NoneBot 初始化前导入会注册 matcher 的插件包。

## 环境

- 当前初始化使用 Windows / PowerShell。
- 模板初始化 workflow 已在 GitHub Actions 成功完成。
- 本地 `uv run pytest` 已通过：`5 passed, 1 warning`。

## 已查阅知识

- `bot-docs/index.md`
- `bot-docs/notes/recipes/nonebot/command-registration.md`
- `nonebot-plugin-architecture` skill：用于后续轻量分层设计。
- `bootstrap-nonebot-plugin-repo` skill：用于仓库创建流程。
- `memory-bank` skill：用于当前记忆库结构初始化。
