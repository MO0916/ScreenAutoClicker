#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows屏幕自动化工具 - 屏幕图像识别自动点击程序
功能：通过截图选择目标图像，自动检测并点击相似图像
"""

import cv2
import numpy as np
import pyautogui
import time
import os
import threading
from pathlib import Path

def capture_screen():
    """捕获整个屏幕"""
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def find_template_on_screen(template_path, threshold=0.8):
    """在屏幕上查找模板图像"""
    # 读取模板图像
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        print(f"❌ 无法读取模板图像: {template_path}")
        return None, 0
    
    # 捕获屏幕
    screen = capture_screen()
    
    # 模板匹配
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= threshold:
        # 计算中心坐标
        h, w = template.shape[:2]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        return (center_x, center_y), max_val
    
    return None, max_val

class ScreenAutoClicker:
    def __init__(self):
        self.running = False
        self.template_path = None
        self.click_interval = 1.0  # 点击间隔(秒)
        self.confidence_threshold = 0.8  # 置信度阈值
        
    def select_template(self, image_path):
        """选择目标模板图像"""
        if os.path.exists(image_path):
            self.template_path = image_path
            print(f"✅ 已选择模板: {image_path}")
            return True
        else:
            print(f"❌ 文件不存在: {image_path}")
            return False
    
    def start_monitoring(self):
        """开始监控和点击"""
        if not self.template_path:
            print("❌ 请先选择模板图像")
            return False
        
        self.running = True
        print("🚀 开始屏幕监控...")
        print(f"📊 配置: 间隔={self.click_interval}s, 阈值={self.confidence_threshold}")
        
        # 启动监控线程
        monitor_thread = threading.Thread(target=self._monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        return True
    
    def stop_monitoring(self):
        """停止监控"""
        self.running = False
        print("⏹️ 停止屏幕监控")
    
    def _monitor_loop(self):
        """监控循环"""
        click_count = 0
        
        while self.running:
            try:
                # 查找模板
                position, confidence = find_template_on_screen(
                    self.template_path, self.confidence_threshold
                )
                
                if position:
                    print(f"🎯 找到目标! 置信度: {confidence:.3f}, 位置: {position}")
                    
                    # 移动鼠标并点击
                    pyautogui.moveTo(position[0], position[1], duration=0.2)
                    pyautogui.click()
                    click_count += 1
                    print(f"🖱️ 点击次数: {click_count}")
                    
                    # 等待图像消失
                    time.sleep(0.5)
                    
                    # 检查图像是否还在
                    position_after, confidence_after = find_template_on_screen(
                        self.template_path, self.confidence_threshold
                    )
                    
                    if not position_after:
                        print("✅ 目标已消失，继续监控...")
                    
                else:
                    print(f"🔍 扫描中... 最高置信度: {confidence:.3f}")
                
                # 等待下一次扫描
                time.sleep(self.click_interval)
                
            except Exception as e:
                print(f"⚠️ 监控错误: {e}")
                time.sleep(1)

# 简单的命令行界面
def main():
    print("=" * 50)
    print("🖥️  Windows屏幕自动化工具")
    print("=" * 50)
    
    clicker = ScreenAutoClicker()
    
    while True:
        print("\n🔧 命令选项:")
        print("1. 选择模板图像")
        print("2. 开始监控")
        print("3. 停止监控")
        print("4. 设置点击间隔")
        print("5. 设置置信度阈值")
        print("6. 退出")
        
        choice = input("请选择操作 (1-6): ").strip()
        
        if choice == "1":
            image_path = input("请输入模板图像路径: ").strip()
            clicker.select_template(image_path)
            
        elif choice == "2":
            if clicker.start_monitoring():
                print("✅ 监控已启动，按回车键停止...")
                input()  # 等待用户停止
                clicker.stop_monitoring()
            
        elif choice == "3":
            clicker.stop_monitoring()
            
        elif choice == "4":
            try:
                interval = float(input("请输入点击间隔(秒): "))
                clicker.click_interval = interval
                print(f"✅ 点击间隔设置为: {interval}秒")
            except ValueError:
                print("❌ 请输入有效数字")
                
        elif choice == "5":
            try:
                threshold = float(input("请输入置信度阈值(0.1-1.0): "))
                if 0.1 <= threshold <= 1.0:
                    clicker.confidence_threshold = threshold
                    print(f"✅ 置信度阈值设置为: {threshold}")
                else:
                    print("❌ 阈值必须在0.1到1.0之间")
            except ValueError:
                print("❌ 请输入有效数字")
                
        elif choice == "6":
            clicker.stop_monitoring()
            print("👋 再见!")
            break
            
        else:
            print("❌ 无效选择")

if __name__ == "__main__":
    main()