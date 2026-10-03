from flask import Flask, redirect, render_template, request, url_for
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return redirect(url_for("index"))

    uploaded_file = request.files["file"]
    if uploaded_file.filename == "":
        return redirect(url_for("index"))

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
    uploaded_file.save(file_path)

    return render_template(
        "index.html",
        result=f"Image uploaded successfully: {uploaded_file.filename}",
        image_path=f"/{file_path.replace('\\', '/')}"
    )


if __name__ == "__main__":
    app.run(debug=True)
