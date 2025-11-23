# import re
import regex as re
import sys
from pathlib import Path

def convert_commas(text: str) -> str:
    """
    将中文上下文中的半角逗号替换为全角逗号。
    英文、数字、LaTeX 命令中的逗号保持不变。
    """
    # 匹配汉字或中文标点后面的半角逗号
    # \u4e00-\u9fff 表示汉字，\u3000-\u303f 表示部分中文标点
    # pattern = re.compile(r'(?<=[\u4e00-\u9fff\u3000-\u303f])\,')
    # pattern = re.compile(r'(?<=[\p{Han}])\,\s')
    pattern = re.compile(r',(?=\s*\p{Han})')
    return pattern.sub('，', text)

def process_file(filepath: Path):
    """
    读取文件，替换逗号，并写回。
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = convert_commas(content)

    # 输出到新文件，避免覆盖原始文件
    output_path = filepath #.with_name(filepath.)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"处理完成：{filepath} → {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python     py <tex文件路径>")
        sys.exit(1)

    tex_file = Path(sys.argv[1])
    if not tex_file.exists():
        print(f"文件不存在: {tex_file}")
        sys.exit(1)

    process_file(tex_file)
