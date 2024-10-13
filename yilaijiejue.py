# 导入所需的库
import sys
!{sys.executable} -m pip install --upgrade pip

# 检查当前的 pandas 版本
try:
    import pandas as pd
    print(f'Current pandas version: {pd.__version__}')
except ImportError:
    print('Pandas is not installed.')

# 根据依赖关系确定要安装的 pandas 版本
required_pandas_version = "pandas>=2.1.0,<2.2.3dev0"

# 安装兼容的 pandas 版本
!pip install $required_pandas_version

# 验证 pandas 是否正确安装
import pandas as pd
print(f'Installed pandas version: {pd.__version__}')

# 安装其他依赖项
dependencies = [
    'cudf-cu12==24.6.1',
    'google-colab==1.0.0',
    'mizani==0.11.4',
    'plotnine==0.13.6',
    'xarray==2024.9.0'
]

for dep in dependencies:
    !pip install $dep

# 验证所有依赖项是否正确安装
print('Verifying installations:')
for dep in dependencies:
    package_name = dep.split('==')[0]
    try:
        module = __import__(package_name)
        print(f'{package_name} version: {module.__version__}')
    except Exception as e:
        print(f'Failed to verify {package_name}: {e}')
