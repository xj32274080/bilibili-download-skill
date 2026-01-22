# B站视频下载工具

> 一个简单易用的B站视频下载工具，支持单个视频和播放列表批量下载，自动转换为H.264格式，兼容QQ影音等主流播放器。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.3.0-blue.svg)](https://github.com/xj32274080/bilibili-download-skill)

## ✨ 功能特性

- 🎥 **单个视频下载** - 支持下载任意B站视频
- 📚 **播放列表批量下载** - 一键下载整个系列视频
- 🔢 **自动集数序号** - 文件名自动添加序号（01_、02_、03_...），便于排序
- 🎯 **指定下载范围** - 支持下载指定集数（如第1-5集、第1,3,5集）
- 🎬 **H.264编码** - 自动转换为H.264格式，兼容QQ影音、VLC等主流播放器
- 🚀 **完全自动化** - 无需用户在场确认，支持后台运行
- 💻 **跨平台支持** - 提供 Windows 脚本和 Python 脚本

## 📦 安装

### 前置要求

1. **安装 Python**（可选，如使用 Python 脚本）
   - 访问 https://www.python.org/downloads/
   - 下载并安装 Python 3.7+

2. **安装 yt-dlp**（必需）
   ```bash
   pip install yt-dlp
   ```

### 安装步骤

#### 方式1：克隆仓库（推荐）
```bash
git clone https://github.com/xj32274080/bilibili-download-skill.git
cd bilibili-download-skill
```

#### 方式2：下载压缩包
1. 访问 https://github.com/xj32274080/bilibili-download-skill
2. 点击 "Code" → "Download ZIP"
3. 解压到任意目录

## 🚀 使用方法

### 方式1：Windows 双击运行（最简单）

1. 双击 `script.bat`
2. 粘贴B站视频链接
3. 按回车开始下载

### 方式2：Windows 命令行

```cmd
REM 下载单个视频
script.bat "https://www.bilibili.com/video/BV1oH8Uz4Evu"

REM 下载播放列表（自动添加序号）
script.bat "https://www.bilibili.com/video/BV1oH8Uz4Evu?p=1"
```

### 方式3：Python 脚本（跨平台）

```bash
# 下载单个视频
python download.py "https://www.bilibili.com/video/BV1oH8Uz4Evu"

# 下载整个播放列表
python download.py "https://www.bilibili.com/video/BV1oH8Uz4Evu"

# 下载播放列表的第1-5集
python download.py "https://www.bilibili.com/video/BV1oH8Uz4Evu" 1-5

# 下载播放列表的第1、3、5集
python download.py "https://www.bilibili.com/video/BV1oH8Uz4Evu" 1,3,5
```

### 方式4：yt-dlp 直接调用

```bash
# 下载单个视频
yt-dlp --yes-playlist -f "bestvideo[vcodec^=avc]+bestaudio/best" \
  --merge-output-format mp4 \
  -o "D:/bilibili_videos/%%(playlist_index)02d_%%(title)s.%%(ext)s" \
  "视频链接"

# 下载播放列表的第1-5集
yt-dlp --yes-playlist --playlist-items 1-5 \
  -f "bestvideo[vcodec^=avc]+bestaudio/best" \
  --merge-output-format mp4 \
  -o "D:/bilibili_videos/%%(playlist_index)02d_%%(title)s.%%(ext)s" \
  "播放列表链接"
```

## 📝 使用示例

### 示例1：下载单个视频
```bash
python download.py "https://www.bilibili.com/video/BV1oH8Uz4Evu"
```
输出文件：`D:\bilibili_videos\视频标题.mp4`

### 示例2：下载整个系列
```bash
python download.py "https://www.bilibili.com/video/BV1oH8Uz4Evu"
```
输出文件：
```
D:\bilibili_videos\01_第一集标题.mp4
D:\bilibili_videos\02_第二集标题.mp4
D:\bilibili_videos\03_第三集标题.mp4
...
```

### 示例3：下载指定集数
```bash
python download.py "https://www.bilibili.com/video/BV1oH8Uz4Evu" 1-3
```
输出文件：
```
D:\bilibili_videos\01_第一集标题.mp4
D:\bilibili_videos\02_第二集标题.mp4
D:\bilibili_videos\03_第三集标题.mp4
```

## ⚙️ 配置说明

### 默认配置

- **下载目录**：`D:\bilibili_videos`
- **视频编码**：H.264（兼容性最好）
- **音频编码**：AAC
- **容器格式**：MP4

### 修改下载目录

#### Windows 修改 `script.bat`
```bat
set "DOWNLOAD_DIR=D:\你的下载目录"
```

#### Python 修改 `download.py`
```python
DOWNLOAD_DIR = Path("D:/你的下载目录")
```

## 🔧 高级功能

### 处理需要登录的视频

某些B站视频需要登录才能下载：

1. **使用浏览器 Cookies**
   ```bash
   yt-dlp --cookies-from-browser chrome -o "输出路径" "视频链接"
   ```

2. **使用 Cookie 文件**
   ```bash
   yt-dlp --cookies cookies.txt -o "输出路径" "视频链接"
   ```

### 下载最高画质

如果需要下载会员专享的高清画质，需要配置cookies：

```bash
yt-dlp --cookies-from-browser chrome \
  -f "bestvideo+bestaudio/best" \
  --merge-output-format mp4 \
  -o "D:/bilibili_videos/%%(title)s.%%(ext)s" \
  "视频链接"
```

## 📋 文件说明

```
bilibili-download-skill/
├── script.bat          # Windows 批处理脚本
├── download.py         # Python 脚本（跨平台）
├── skill.json          # Claude Code Skill 配置
├── README.md           # 使用说明
└── LICENSE             # MIT 开源协议
```

## 📸 截图示例

### 下载单个视频
```
==================================================
B站视频下载工具 (QQ影音兼容版)
==================================================
下载目录: D:\bilibili_videos

正在下载，请稍候...

[BiliBili] Downloading webpage
[download] 100% of 95.04MiB in 00:06
[Merger] Merging formats into "视频标题.mp4"

==================================================
下载完成！视频保存在: D:\bilibili_videos
==================================================
```

### 下载播放列表
```
正在下载，请稍候...

[BiliBili] Downloading playlist 36计
[download] Downloading video 1 of 36
[download] 100% of 57.67MiB
[download] Downloading video 2 of 36
[download] 100% of 62.31MiB
...
[download] Downloading video 36 of 36
[download] 100% of 48.95MiB

==================================================
下载完成！视频保存在: D:\bilibili_videos
==================================================
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 强大的视频下载工具
- [Claude Code](https://claude.ai/code) - AI 驱动的开发工具

## 📮 联系方式

- GitHub: [@xj32274080](https://github.com/xj32274080)

## ⭐ 如果这个项目对你有帮助，请给个 Star！

## 📊 更新日志

### v1.3.0 (2025-01-22)
- ✨ 新增播放列表/系列视频批量下载功能
- 🔢 自动添加集数序号（01_、02_、03_...）
- 🎯 支持指定下载范围（如1-5集、1,3,5集）
- 🔍 自动识别单个视频或播放列表
- 📁 优化文件名格式，便于排序和管理

### v1.2.0 (2025-01-22)
- ❌ 移除所有交互式确认（pause、input等）
- 🚀 支持完全自动化下载，无需用户在场
- ⚡ 优化为非阻塞式执行

### v1.1.0 (2025-01-22)
- 🐛 修复文件名输出模板语法错误
- 🔧 统一使用英文路径避免编码问题
- ⚙️ 更新全局配置文件 config.txt
- 📂 优化下载目录结构

### v1.0.0 (2025-01-21)
- 🎉 初始版本发布
- ✅ 支持B站视频下载
- 🎬 自动转换为H.264格式
