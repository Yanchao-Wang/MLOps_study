#!/bin/bash

# 设置 Jupyter 内核的脚本
# 用法: bash setup_kernel.sh [环境名]

ENV_NAME=${1:-exercises}

echo "正在为虚拟环境 '$ENV_NAME' 安装 Jupyter 内核..."

# 同步依赖
echo "同步依赖..."
uv sync

# 注册内核
echo "注册内核..."
uv run python -m ipykernel install --user --name "$ENV_NAME" --display-name "Python ($ENV_NAME)"

echo "✓ 完成！内核已注册为 '$ENV_NAME'"
echo "你现在可以在 VS Code 的 Notebook 中选择这个内核了"
