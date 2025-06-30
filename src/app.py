from flask import Flask, render_template, request, url_for
from ultralytics import YOLO
import os

app = Flask(__name__)
model_path = os.path.join('model', 'best.pt')
model = YOLO(model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image_filename = None
    debug_info = ""
    if request.method == 'POST':
        file = request.files['image']
        if file:
            image_filename = file.filename
            static_dir = os.path.join(os.path.dirname(__file__), 'static')
            os.makedirs(static_dir, exist_ok=True)
            save_path = os.path.join(static_dir, image_filename)
            file.save(save_path)
            # 验证图片是否保存成功
            file_exists = os.path.exists(save_path)
            debug_info += f"图片保存路径: {save_path}<br>文件是否存在: {file_exists}<br>"
            # 推理并打印详细信息
            try:
                results = model(save_path)
                debug_info += f"推理结果: {results}<br>"
                if results and results[0].boxes is not None:
                    debug_info += f"boxes: {results[0].boxes}<br>"
                    debug_info += f"cls: {results[0].boxes.cls}<br>"
                    fall_detected = any([int(c) == 0 for c in results[0].boxes.cls])
                    result = '检测到摔倒' if fall_detected else '未检测到摔倒'
                else:
                    result = '未检测到目标'
                    debug_info += "未检测到目标<br>"
            except Exception as e:
                result = '推理出错'
                debug_info += f"推理异常: {e}<br>"
            return render_template('index.html', result=result, image=image_filename, debug_info=debug_info)
    return render_template('index.html', result=result, image=image_filename, debug_info=debug_info)

if __name__ == '__main__':
    app.run(debug=True)