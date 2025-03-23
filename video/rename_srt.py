import os
import re

def rename_subtitles(video_folder):
    # 获取文件夹中的所有文件
    files = os.listdir(video_folder)
    
    # 筛选出视频文件和字幕文件
    video_files = [f for f in files if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]
    subtitle_files = [f for f in files if f.endswith(('.srt', '.ass', '.sub'))]
    
    # 按集数排序
    video_files.sort()
    subtitle_files.sort()
    
    # 确保视频文件和字幕文件的数量一致
    if len(video_files) != len(subtitle_files):
        print("视频文件和字幕文件数量不匹配！")
        return
    
    # 重命名字幕文件
    for video, subtitle in zip(video_files, subtitle_files):
        # 获取视频文件名（不含扩展名）
        video_name = os.path.splitext(video)[0]
        
        # 获取字幕文件的扩展名
        subtitle_ext = os.path.splitext(subtitle)[1]
        
        # 新的字幕文件名
        new_subtitle_name = f"{video_name}{subtitle_ext}"
        
        # 重命名字幕文件
        os.rename(os.path.join(video_folder, subtitle), os.path.join(video_folder, new_subtitle_name))
        print(f"重命名: {subtitle} -> {new_subtitle_name}")

if __name__ == "__main__":
    # 替换为你的美剧文件夹路径
    video_folder = "/path/to/your/video/folder"
    rename_subtitles(video_folder)