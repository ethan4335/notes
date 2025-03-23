import ffmpeg

def compress_video_with_ffmpeg(input_path, output_path, crf=23, preset='medium', resolution='1280x720'):
    """
    使用FFmpeg进行视频压缩
    :param input_path: 输入视频文件路径
    :param output_path: 输出视频文件路径
    :param crf: 常用范围是18-28，数值越小质量越高，文件越大
    :param preset: 压缩速度与质量的平衡，可选值有ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
    :param resolution: 输出视频的分辨率
    """
    stream = ffmpeg.input(input_path)
    stream = ffmpeg.filter_(stream, 'scale', resolution)
    ffmpeg.output(stream, output_path, crf=crf, preset=preset).run()

# 示例用法
compress_video_with_ffmpeg('/Users/ethan/Downloads/我的影片.mp4', '/Users/ethan/Downloads/我的影片_c.mp4', crf=23, preset='medium', resolution='640x360')