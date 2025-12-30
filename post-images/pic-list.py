import os

folder = os.getcwd()  # 当前目录
files = sorted(os.listdir(folder))

# 支持的图片扩展，如果不想筛选就去掉 endswith()
exts = ('.jpg', '.jpeg', '.png')
for f in files:
    if f.lower().endswith(exts):
        print(f"![]({os.path.join(folder, f)})")
