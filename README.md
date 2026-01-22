# B站视频下载 Skill

## 功能
- 下载B站单个视频或整个播放列表/系列视频
- 自动添加集数序号（如：`01_视频标题.mp4`）
- 下载到 `D:\bilibili_videos` 目录
- 自动选择H.264编码格式（兼容QQ影音等主流播放器）
- 自动合并视频和音频
- 支持指定下载范围（如第1-5集、第1,3,5集）
- 完全自动化，无需用户在场确认

## 使用方法

### 方式1：直接运行脚本（Windows）
双击 `script.bat`，粘贴B站视频链接

### 方式2：命令行调用（Windows CMD）
```bash
# 下载单个视频
script.bat "https://www.bilibili.com/video/BVxxxxxx"

# 下载整个播放列表（自动添加序号）
script.bat "https://www.bilibili.com/video/BVxxxxxx?p=1"
```

### 方式3：Python 脚本（跨平台）
```bash
# 下载单个视频
python download.py "https://www.bilibili.com/video/BVxxxxxx"

# 下载整个播放列表
python download.py "https://www.bilibili.com/video/BVxxxxxx"

# 下载播放列表的第1-5集
python download.py "https://www.bilibili.com/video/BVxxxxxx" 1-5

# 下载播放列表的第1、3、5集
python download.py "https://www.bilibili.com/video/BVxxxxxx" 1,3,5
```

### 方式4：通过yt-dlp直接下载（Git Bash / Linux）
```bash
# 下载单个视频
yt-dlp --yes-playlist -f "bestvideo[vcodec^=avc]+bestaudio/best" --merge-output-format mp4 -o "D:/bilibili_videos/%%(playlist_index)02d_%%(title)s.%%(ext)s" "视频链接"

# 下载播放列表的第1-5集
yt-dlp --yes-playlist --playlist-items 1-5 -f "bestvideo[vcodec^=avc]+bestaudio/best" --merge-output-format mp4 -o "D:/bilibili_videos/%%(playlist_index)02d_%%(title)s.%%(ext)s" "播放列表链接"
```

### 方式5：通过 Claude Code 调用
在 Claude Code 中直接说：
- "下载这个B站视频 [链接]"
- "下载这个播放列表的所有视频 [链接]"
- "下载这个播放列表的第3到10集 [链接]"

## 配置
- 下载目录：`D:\bilibili_videos`
- 视频编码：H.264（兼容性最好）
- 音频编码：AAC
- 容器格式：MP4

## 更新日志
### v1.3.0
- 新增播放列表/系列视频批量下载功能
- 自动添加集数序号（01_、02_、03_...）
- 支持指定下载范围（如1-5集、1,3,5集）
- 自动识别单个视频或播放列表
- 优化文件名格式，便于排序和管理

### v1.2.0
- 移除所有交互式确认（pause、input等）
- 支持完全自动化下载，无需用户在场
- 优化为非阻塞式执行

### v1.1.0
- 修复文件名输出模板语法错误
- 统一使用英文路径避免编码问题
- 更新全局配置文件 config.txt
- 优化下载目录结构

### v1.0.0
- 初始版本
- 支持B站视频下载
- 自动转换为H.264格式

## 注意事项
- 需要安装 yt-dlp
- 如遇B站需要登录的视频，可能需要配置cookies
- 推荐使用 QQ影音、VLC 等播放器播放
