# CLI 练习快速入门 🚀

基于 **Typer** 的现代化 CLI 工具练习项目。

## 📦 文件结构

```
exercise_s2/
├── greetings.py              # 基础练习：Hello World CLI
├── iris_classifier.py        # 进阶练习：完整的 ML CLI 工具
└── CLI_EXERCISES_README.md   # 详细教程和文档
```

## ⚡ 快速开始

### 1. 安装依赖
```bash
uv sync
```

### 2. 基础练习
```bash
# 运行 greetings
python greetings.py --count 3

# 查看帮助
python greetings.py --help
```

### 3. 进阶练习
```bash
# 查看所有命令
python iris_classifier.py --help

# 训练模型
python iris_classifier.py train svm --kernel linear
python iris_classifier.py train knn --n-neighbors 3

# 评估模型
python iris_classifier.py evaluate model_svm.ckpt
```

## 🎯 学习目标

- ✅ 掌握 Typer 基本用法（类型注解、自动帮助）
- ✅ 理解命令组和嵌套子命令
- ✅ 学习选项参数和位置参数
- ✅ 实践完整的 CLI 工具开发流程

## 📖 详细文档

查看 [CLI_EXERCISES_README.md](CLI_EXERCISES_README.md) 获取完整的教程和 API 参考。

## 🔧 技术栈

- **Typer 0.21.1+**: 现代化 CLI 框架
- **scikit-learn**: 机器学习库（用于示例）
- **Python 3.11+**: 支持最新类型注解

## 💡 核心概念速查

```python
# 1. 简单命令
import typer
def main(count: int = 1):
    pass
typer.run(main)

# 2. 命令组
app = typer.Typer()
@app.command()
def train(): pass

# 3. 嵌套子命令
train_app = typer.Typer()
app.add_typer(train_app, name="train")
@train_app.command("svm")
def train_svm(): pass
```

---

**开始学习**: 先看 `greetings.py`，再挑战 `iris_classifier.py` 🎓
