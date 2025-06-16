# Bilibili UID 扫描工具

一个基于 Python + Playwright 的小工具，用于批量访问 Bilibili 用户主页，筛选出满足以下条件的 UID 并导出：

- 用户等级为 0（`sic-BDC_svg-user_level_0`）
- 用户昵称仅由大小写英文字母组成（不含中文、数字或其他符号）
- 可导出 UID 和昵称（格式为：`UID - 昵称`）

---

## ✨ 功能特性

- 📌 扫描 Bilibili 用户 UID：从 `500XXXX` 到 `599XXXX`，后四位自定义
- 🧠 智能判断等级为 0 用户（通过页面 class 检查）
- 🧼 筛选昵称为纯英文字母的用户
- 📄 导出匹配结果到 `uid.txt`，格式为：`5011234 - Alice`

---

## 📦 安装依赖

### 1. 安装 Python 依赖

```bash
pip install playwright
playwright install
```

---

## ▶️ 使用方法

### 克隆或下载本项目：

```bash
git clone https://github.com/你的用户名/bilibili-uid-scanner.git
cd bilibili-uid-scanner
```

### 运行脚本：

```bash
python main.py
```

### 按提示输入 4 位数字后缀：

```
请输入四位数后缀（如1234）：1234
```

### 扫描结果将保存在当前目录下的 `uid.txt` 中，每行格式如下：

```
5011234 - Alice
5041234 - David
```

---

## 💡 示例输出

### 终端输出示例：

```
✔ 5011234：昵称 Alice
✘ 5021234：昵称不合规：陌染芄烛
✘ 5031234：非零级
✔ 5041234：昵称 David
```

### 文件 uid.txt 内容示例：

```
5011234 - Alice
5041234 - David
```

---

## 🔍 技术细节

- 使用 **Playwright** 实现 Chromium 无头浏览器访问，速度快、稳定性强
- 使用正则表达式匹配昵称格式（仅允许 A-Z, a-z）
- 自动跳过非零级账号或不符合昵称规则的用户

---

## 🧰 技术栈

- Python 3.7+
- Playwright (Chromium)
- 正则表达式（re）
- asyncio 异步框架

---

## 📁 文件结构

```
bilibili-uid-scanner/
├── main.py        # 主程序
├── uid.txt        # 输出结果（运行后生成）
└── README.md      # 项目说明文件
```

---

## 📜 License

本项目基于 MIT 协议开源，欢迎学习、使用与修改，但请勿用于任何违法用途。
