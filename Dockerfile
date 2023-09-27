# 使用官方的 Python 基本映像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 和安装依赖
# 假设 requirements.txt 也在 ntu2023iam 目录下
# 如果不在该目录下，请根据实际路径调整
COPY ntu2023iam/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 复制 ntu2023iam 目录下的所有文件和目录到容器的 /app
COPY ntu2023iam/ /app/

# 暴露你的应用程序在这个端口运行
EXPOSE 5000

# 设置环境变量，例如如果您使用 Flask，您可能需要设置 FLASK_APP 环境变量
ENV FLASK_APP=app.py

# 运行你的应用程序
CMD ["flask", "run", "--host=0.0.0.0"]
