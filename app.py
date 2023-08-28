from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    folder_path = "C:\\Users\\alan.marchi\\Desktop\\Alan\\spese_mediche_quas\\05_23"
  # Inserisci il percorso della cartella desiderata
    files = os.listdir(folder_path)
    print(files)
    return render_template('index.html', files=files)



@app.route('/download/<filename>')
def download_file(filename):
    folder_path = "C:\\Users\\alan.marchi\\Desktop\\Alan\\spese_mediche_quas\\05_23"
  # Inserisci il percorso della cartella desiderata
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    app.run(debug=True)