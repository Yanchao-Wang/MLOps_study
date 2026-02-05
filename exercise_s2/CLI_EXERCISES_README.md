# CLI 练习文件说明 - Typer 版本

本目录包含使用 **Typer** 构建的 CLI (Command Line Interface) 练习文件，演示了从简单到复杂的命令行工具构建过程。

## 🚀 关于 Typer

Typer 是一个现代化的 Python CLI 框架，基于 Python 类型注解构建，提供：
- ✅ 自动类型验证
- ✅ 自动生成美观的帮助文档
- ✅ Rich UI 支持（彩色输出、表格、进度条）
- ✅ 基于 Click，功能强大且稳定

## 📁 文件列表

### 1. `greetings.py` - 基础练习
**目标**: 创建简单的 Hello World CLI，理解 Typer 基本用法

**使用方法**:
```bash
# 打印一次（默认）
python greetings.py

# 打印 3 次
python greetings.py --count 3

# 查看帮助
python greetings.py --help
```

**输出示例**:
```
Hello World!
Hello World!
Hello World!
```

---

### 2. `iris_classifier.py` - 完整练习：嵌套子命令
**目标**: 构建具有多层嵌套子命令的完整 CLI 应用

**命令结构**:
```
iris_classifier.py
├── train (命令组)
│   ├── svm   --kernel <kernel> -o <output>
│   └── knn   --n-neighbors <n> -o <output>
└── evaluate <checkpoint>
```

**使用方法**:
```bash
# 查看所有命令
python iris_classifier.py --help

# 查看 train 子命令
python iris_classifier.py train --help

# 训练 SVM（线性核）
python iris_classifier.py train svm --kernel linear

# 训练 SVM（RBF 核）
python iris_classifier.py train svm --kernel rbf -o my_svm.ckpt

# 训练 KNN（3 个邻居）
python iris_classifier.py train knn --n-neighbors 3

# 训练 KNN（5 个邻居）
python iris_classifier.py train knn --n-neighbors 5 -o my_knn.ckpt

# 评估保存的模型
python iris_classifier.py evaluate model_svm.ckpt
python iris_classifier.py evaluate model_knn.ckpt

# 查看各子命令的帮助
python iris_classifier.py train svm --help
python iris_classifier.py train knn --help
```

---

## 🧪 完整工作流示例

```bash
# 1. 训练 SVM 模型（线性核）
python iris_classifier.py train svm --kernel linear -o svm_linear.ckpt

# 2. 训练 SVM 模型（RBF 核）
python iris_classifier.py train svm --kernel rbf -o svm_rbf.ckpt

# 3. 训练 KNN 模型（3 个邻居）
python iris_classifier.py train knn --n-neighbors 3 -o knn_3.ckpt

# 4. 训练 KNN 模型（5 个邻居）
python iris_classifier.py train knn --n-neighbors 5 -o knn_5.ckpt

# 5. 比较所有模型
python iris_classifier.py evaluate svm_linear.ckpt
python iris_classifier.py evaluate svm_rbf.ckpt
python iris_classifier.py evaluate knn_3.ckpt
python iris_classifier.py evaluate knn_5.ckpt
```

---

## 📚 Typer 核心概念

### 1. 基本命令 - `typer.run()`
最简单的方式，直接运行一个函数：
```python
import typer

def main(count: int = 1) -> None:
    """Print greeting."""
    for _ in range(count):
        print("Hello!")

if __name__ == "__main__":
    typer.run(main)
```

**特点**:
- Python 类型注解 → CLI 参数类型
- 函数参数名 → 选项名称（`--count`）
- 文档字符串 → 帮助信息

---

### 2. 命令组 - `typer.Typer()`
组织多个命令：
```python
import typer

app = typer.Typer()

@app.command()
def train():
    """Train model."""
    pass

@app.command()
def evaluate():
    """Evaluate model."""
    pass

if __name__ == "__main__":
    app()
```

---

### 3. 嵌套子命令 - `app.add_typer()`
创建多层命令结构：
```python
import typer

app = typer.Typer()
train_app = typer.Typer()
app.add_typer(train_app, name="train")

@train_app.command("svm")
def train_svm():
    """Train SVM."""
    pass

@train_app.command("knn")
def train_knn():
    """Train KNN."""
    pass
```

**命令行**: `python app.py train svm`

---

### 4. 参数类型

#### 选项参数（Optional）
```python
from typing import Annotated

def main(
    kernel: Annotated[str, typer.Option(help="Kernel type")] = "linear",
):
    pass
```
**使用**: `--kernel rbf`

#### 位置参数（Required）
```python
def evaluate(
    checkpoint: Annotated[str, typer.Argument(help="Model path")],
):
    pass
```
**使用**: `evaluate model.ckpt`（必须提供）

---

## 💡 Typer 语法要点

### 参数名转换
- Python: `n_neighbors` (下划线)
- CLI: `--n-neighbors` (短横线)
- Typer 自动转换！

### 类型注解优势
```python
def train(
    epochs: int = 10,        # CLI 会验证必须是整数
    lr: float = 0.001,       # CLI 会验证必须是浮点数
    verbose: bool = False,   # CLI 会转换为 --verbose / --no-verbose
):
    pass
```

### Rich UI 输出
Typer 自动提供美观的帮助文档：
```
╭─ Commands ───────────────────────────────╮
│ evaluate  Evaluate a saved model         │
│ train     Train a model                  │
╰──────────────────────────────────────────╯
```

---

## 🔧 依赖

所有练习需要以下依赖：
```bash
uv add typer scikit-learn
```

或在 `pyproject.toml` 中：
```toml
dependencies = [
    "typer>=0.12.0",
    "scikit-learn>=1.3.0",
]
```

安装：
```bash
uv sync
```

---

## 🎓 学习路径

1. **基础**: `greetings.py`
   - 理解 `typer.run()` 的基本用法
   - 学习参数定义和帮助文档

2. **进阶**: `iris_classifier.py`
   - 学习命令组（`typer.Typer()`）
   - 理解嵌套子命令（`app.add_typer()`）
   - 掌握 `Annotated` 类型提示
   - 组合选项和位置参数

---

## 🆚 Typer vs 其他 CLI 工具

| 特性 | Typer | Click | argparse |
|------|-------|-------|----------|
| 类型注解 | ✅ 原生支持 | ❌ 需手动 | ❌ 需手动 |
| 美观输出 | ✅ Rich UI | ⚠️ 基础 | ❌ 纯文本 |
| 学习曲线 | 低 | 中 | 中 |
| 代码量 | 少 | 中 | 多 |
| 性能 | 快 | 快 | 快 |

---

## 📖 延伸阅读

- [Typer 官方文档](https://typer.tiangolo.com/)
- [命令颜色和样式](https://typer.tiangolo.com/tutorial/printing/)
- [参数验证](https://typer.tiangolo.com/tutorial/parameter-types/number/)
- [进度条和加载动画](https://typer.tiangolo.com/tutorial/progressbar/)

---

## ✨ 最佳实践

1. **使用类型注解**: 让 Typer 自动验证参数
2. **写好文档字符串**: 自动生成帮助信息
3. **使用 `Annotated`**: 提供详细的参数说明
4. **合理组织命令**: 大项目用命令组，小项目用 `typer.run()`
5. **短选项别名**: 为常用选项提供简写（如 `-o` 代替 `--output`）

```python
# 推荐写法
from typing import Annotated

def train(
    output: Annotated[str, typer.Option("--output", "-o", help="Output path")] = "model.ckpt",
    epochs: Annotated[int, typer.Option(help="Number of epochs")] = 10,
) -> None:
    """Train the model with specified parameters."""
    pass
```

---

**版本信息**: Typer 0.21.1+, Python 3.11+
