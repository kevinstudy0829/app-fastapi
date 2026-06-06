# 使用官方 Python 基底映像
FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 複製需求檔案並安裝套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式碼
COPY . .

# 指定容器啟動指令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
