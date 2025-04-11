#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import hashlib
import shutil

# 定义图片目录路径
IMAGE_DIR = 'icons'
# 备份目录
BACKUP_DIR = 'icons_backup'

def calculate_md5(file_path):
    """计算文件的MD5值"""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5.update(chunk)
    return md5.hexdigest()

def modify_file_md5(file_path):
    """修改文件的MD5值"""
    # 获取原始MD5值
    original_md5 = calculate_md5(file_path)
    
    # 打开文件，添加随机字节
    with open(file_path, 'ab') as f:
        # 添加一个随机字节到文件末尾
        f.write(bytes([random.randint(0, 255)]))
    
    # 获取新的MD5值
    new_md5 = calculate_md5(file_path)
    
    return original_md5, new_md5

def backup_directory(src_dir, dst_dir):
    """备份目录"""
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir)
    print(f"已备份目录 {src_dir} 到 {dst_dir}")

def process_images():
    """处理目录下的所有图片文件"""
    # 先备份目录
    backup_directory(IMAGE_DIR, BACKUP_DIR)
    
    # 图片文件扩展名列表
    image_extensions = ['.png', '.jpg', '.jpeg', '.webp', '.gif']
    
    # 遍历目录下的所有文件
    modified_count = 0
    for root, _, files in os.walk(IMAGE_DIR):
        for file in files:
            # 跳过.DS_Store文件
            if file == '.DS_Store':
                continue
                
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()
            
            # 只处理图片文件
            if file_extension in image_extensions:
                try:
                    original_md5, new_md5 = modify_file_md5(file_path)
                    print(f"已修改: {file_path}")
                    print(f"  原MD5: {original_md5}")
                    print(f"  新MD5: {new_md5}")
                    modified_count += 1
                except Exception as e:
                    print(f"处理 {file_path} 时出错: {e}")
    
    print(f"\n总共修改了 {modified_count} 个文件")

if __name__ == "__main__":
    print("开始修改资源文件MD5值...")
    process_images()
    print("修改完成！")
