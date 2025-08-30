import re
import os
import sys
from pathlib import Path

def update_version_files(new_version):
    """Update version in all version.py files and configuration files"""
    
    # لیست تمام فایل‌هایی که باید نسخه در آن‌ها به روز شود
    version_files = [
        "projectA/version.py",
        "projectB/version.py", 
        "pyproject.toml",
        "setup.py"
    ]
    
    print(f"Updating version to: {new_version}")
    
    for file_path in version_files:
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} not found, skipping...")
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            updated_content = content
            
            # بروزرسانی فایل‌های پایتون
            if file_path.endswith('.py'):
                updated_content = re.sub(
                    r'__version__\s*=\s*[\'"][^\'"]*[\'"]',
                    f'__version__ = "{new_version}"',
                    content
                )
            
            # بروزرسانی pyproject.toml
            elif file_path == 'pyproject.toml':
                updated_content = re.sub(
                    r'version\s*=\s*[\'"][^\'"]*[\'"]',
                    f'version = "{new_version}"',
                    content
                )
            
            # بروزرسانی setup.py
            elif file_path == 'setup.py':
                updated_content = re.sub(
                    r'version\s*=\s*[\'"][^\'"]*[\'"]',
                    f'version = "{new_version}"',
                    content
                )
            
            # اگر تغییری ایجاد شد، فایل را ذخیره کن
            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✓ Updated {file_path}")
            else:
                print(f"✗ No version pattern found in {file_path}")
                
        except Exception as e:
            print(f"Error updating {file_path}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_version.py <new_version>")
        sys.exit(1)
    
    new_version = sys.argv[1]
    update_version_files(new_version)