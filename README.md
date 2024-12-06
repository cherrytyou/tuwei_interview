# tuwei_interview
容器化：使用 Docker 创建你的测试工具镜像，确保包含所有运行自动化测试所需的依赖项。
在测试机上安装docker:https://docs.docker.com/desktop/setup/install/windows-install/#install-docker-desktop-on-windows
在docker启动的情况下:然后执行如下命令启动selenium执行服务端docker容器,运行 docker run -d --name selenium-standalone-chrome -h selenium-standalone-chrome --memory 1g --memory-swap -1 -p 4444:4444 selenium/standalone-chrome

1. 打开命令提示符
确保在 Windows 中打开命令提示符或 PowerShell，并导航到您的工作目录：
cd C:\Users\Abby\Downloads\tuwei\tuwei_interview

2. 构建 Docker 镜像
运行以下命令来构建 Docker 镜像，命名为 my-selenium-app：
docker build -t my-selenium-app .

3. 启动 Docker 容器
运行以下命令来启动 Docker 容器并执行 Selenium 脚本：
docker run --privileged my-selenium-app

请将：GameTestSelenium.py 文件中的ip192.168.137.1 地址改成脚本需要运行在的虚拟机ip地址