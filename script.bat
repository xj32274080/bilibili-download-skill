@echo off
chcp 65001 >nul
set "DOWNLOAD_DIR=D:\bilibili_videos"

echo.
echo ==========================================
echo       B站视频下载工具 (QQ影音兼容版)
echo ==========================================
echo.
echo 下载目录: %DOWNLOAD_DIR%
echo.

if "%~1"=="" (
    set /p url="请输入B站视频链接或播放列表链接: "
) else (
    set url=%~1
)

echo.
echo 正在下载，请稍候...
echo.

REM 检测是否为播放列表并自动添加 --yes-playlist 参数
REM 使用 --yes-playlist 自动下载整个列表
REM 使用 --output 模板添加集数序号
yt-dlp --yes-playlist -f "bestvideo[vcodec^=avc]+bestaudio/best" --merge-output-format mp4 -o "%DOWNLOAD_DIR%\%%(playlist_index)02d_%%(title)s.%%(ext)s" "%url%"

echo.
echo ==========================================
echo 下载完成！视频保存在: %DOWNLOAD_DIR%
echo ==========================================
echo.
