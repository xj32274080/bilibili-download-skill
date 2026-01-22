#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B站视频下载工具 - Python版本
支持自动清理文件名、播放列表下载和跨平台使用
"""

import subprocess
import sys
import re
from pathlib import Path

# 配置
DOWNLOAD_DIR = Path("D:/bilibili_videos")
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


def download_video(url, playlist_items=None):
    """下载B站视频或播放列表"""
    print("=" * 50)
    print("B站视频下载工具 (QQ影音兼容版)")
    print("=" * 50)
    print(f"下载目录: {DOWNLOAD_DIR}")
    print()

    # 构建yt-dlp命令
    # 对于播放列表，使用 playlist_index 序号，对于单个视频则忽略
    output_template = str(DOWNLOAD_DIR / "%(playlist_index)s%(title)s.%(ext)s")

    cmd = [
        "yt-dlp",
        "--yes-playlist",  # 自动下载播放列表
        "-f", "bestvideo[vcodec^=avc]+bestaudio/best",
        "--merge-output-format", "mp4",
        "-o", output_template,
    ]

    # 如果指定了播放列表范围（如 "1-5", "1,3,5"）
    if playlist_items:
        cmd.extend(["--playlist-items", playlist_items])

    cmd.append(url)

    print("正在下载，请稍候...")
    print()

    try:
        # 执行下载
        result = subprocess.run(cmd, check=True, capture_output=False)

        print()
        print("=" * 50)
        print(f"下载完成！视频保存在: {DOWNLOAD_DIR}")
        print("=" * 50)
        return True

    except subprocess.CalledProcessError as e:
        print(f"下载失败: {e}")
        return False
    except FileNotFoundError:
        print("错误: 未找到 yt-dlp 命令")
        print("请先安装 yt-dlp: pip install yt-dlp")
        return False


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("错误: 未提供视频链接")
        print("使用方法:")
        print("  python download.py \"B站视频链接\"")
        print("  python download.py \"播放列表链接\"           # 下载整个列表")
        print("  python download.py \"播放列表链接\" 1-5      # 下载第1-5集")
        print("  python download.py \"播放列表链接\" 1,3,5    # 下载第1、3、5集")
        sys.exit(1)

    url = sys.argv[1]
    playlist_items = sys.argv[2] if len(sys.argv) > 2 else None

    download_video(url, playlist_items)


if __name__ == "__main__":
    main()
