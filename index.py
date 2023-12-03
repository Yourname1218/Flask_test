from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# 主頁面
@app.route('/')
def index():
    return render_template('index.html')

# 更新主機名稱的功能
@app.route('/update_hostname', methods=['POST'])
def update_hostname():
    if request.method == 'POST':
        new_hostname = request.form['new_hostname']
        
        # 執行命令更新主機名稱
        subprocess.call(['hostnamectl', 'set-hostname', new_hostname])
        
        return f'主機名稱已更新為 {new_hostname}'
    else:
        return '只允許 POST 請求'

if __name__ == '__main__':
    app.run(debug=True)
