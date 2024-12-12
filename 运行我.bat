@echo off
chcp 65001

:begin
cls
echo ***************************************
echo * JSON与PNG文件检测脚本（循环运行） *
echo * 退出请手动关闭窗口                *
echo ***************************************
echo.

:: 输入 JSON 文件
echo 请拖入json文件并按回车：
set /p dummy=
if "%dummy%"=="" (
    echo [错误] 未输入任何内容，请重新输入。
    pause
    goto begin
)
set "f=%dummy:~-5%"
if /i not "%f%"==".json" (
    echo [错误] 输入的不是有效的json文件，请重新输入。
    pause
    goto begin
)

:: 输入 PNG 文件
echo 请拖入png图片并按回车9：(改后缀就行)
set /p png=
if "%png%"=="" (
    echo [错误] 未输入任何内容，请重新输入。
    pause
    goto begin
)
set "d=%png:~-4%"
if /i not "%d%"==".png" (
    echo [错误] 输入的不是有效的png图片，请重新输入。
    pause
    goto begin
)

:: 文件验证成功，传递给Python脚本
echo.
echo [成功] 文件验证通过！
echo JSON 文件路径：%dummy%
echo PNG 图片路径：%png%

:: 调用 Python 脚本并传递文件路径参数
python AtlasSplit.py "%dummy%" "%png%"

pause
cls
goto begin
