# 测试体系说明

本目录用于承载 `ruyiPage` 的正式回归测试基线。

设计目标：

- 稳定可重复：优先使用本地 server、本地 HTML 页面和可控输入
- 分层清晰：按 smoke / feature / integration / release 组织
- 低侵入扩展：不替代 `examples/`，而是把回归断言沉淀在 `tests/`
- 服务 release：为后续版本发布、CI 和平台矩阵打基础

目录约定：

- `support/`：测试支撑代码，如本地 server、通用 helper、路径工具
- `fixtures/`：测试专用静态资源，如 HTML 页面
- `smoke/`：最核心的启动 / 导航 / 点击 / 输入能力
- `features/`：按模块划分的功能回归
- `integration/`：多模块串联后的工作流验证
- `release/`：发版前的最小通过集合

当前第一版基线已覆盖：

- 启动
- 导航
- 点击 / 输入
- 请求拦截
- 响应拦截与 response body
- DataCollector
- Cookie
- localStorage / sessionStorage
- Cookie + Storage 同会话联动流
- private mode
- attach 已有浏览器基础路径

运行方式：

```bash
python -m pytest tests
```

常用筛选：

```bash
python -m pytest tests -m smoke
python -m pytest tests -m feature
python -m pytest tests -m integration
python -m pytest tests/release
```

说明：

- 第一阶段优先覆盖启动、导航、点击、输入、拦截、collector、Cookie、private mode 等核心路径。
- 现有 `examples/` 继续承担演示用途，不与 `tests/` 互相替代。

## Release Matrix

当前仓库已提供基础 CI 矩阵定义：`.github/workflows/tests.yml`

第一阶段矩阵策略：

- Python：3.9 / 3.10 / 3.11 / 3.12 / 3.13
- OS：Windows
- Firefox：151
- 浏览器模式：普通 Firefox 启动路径

CI 会通过环境变量 `RUYIPAGE_TEST_FIREFOX_PATH` 把指定 Firefox 路径注入到
`tests/conftest.py` 中的浏览器工厂，确保测试用例使用固定浏览器版本。

当前策略说明：

- CI 中默认使用官方 Firefox 151，原因是来源稳定、安装方式标准、最适合作为第一阶段回归基线。
- 如果做手工发版验证，推荐优先使用配套项目 `firefox-fingerprintBrowser` 的 151 版本 release：
  `https://github.com/LoseNine/firefox-fingerprintBrowser`
- 本地手工验证时，可以通过环境变量 `RUYIPAGE_TEST_FIREFOX_PATH` 指向该浏览器的可执行文件，
  让同一套 `tests/` 基线直接跑在指纹浏览器上。

之所以先从这个范围起步，是为了优先建立稳定、可持续、可发版的最小质量门禁。

后续建议逐步扩展到：

- macOS / Linux
- `existing_only(True)` attach 模式的专门矩阵
- 指纹浏览器接管模式
- 特定 Firefox 版本分层验证

## 当前边界

这套基线已经能支撑“本地可重复 + release gate”目标，但还没有完全做到：

- 指纹浏览器接管矩阵自动化
- 多平台实机矩阵报告自动汇总
- Firefox 多版本并行验证
- `user_dir` 跨进程重启后的 localStorage 持久化，目前未纳入 release gate 硬断言

这些属于第二阶段稳定性建设内容。
