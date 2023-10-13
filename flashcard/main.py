import os
import sys
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = files
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create the 'files' directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def index():
    return render_template("main.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        uploaded_file = request.files["file"]

        if uploaded_file.filename != "":
            # Save the uploaded file to the configured UPLOAD_FOLDER
            uploaded_file.save(
                os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
            )

            # You might also want to perform additional processing here

            response_data = {
                "message": "File uploaded successfully",
                # You can include additional data in the response if needed
            }
            return (
                jsonify(response_data),
                200,
            )  # Return JSON response with status code 200
        else:
            response_data = {
                "message": "No file selected",
            }
            return (
                jsonify(response_data),
                400,
            )  # Return JSON response with status code 400
    except Exception as e:
        response_data = {
            "message": f"An error occurred: {str(e)}",
        }
        return jsonify(response_data), 500  # Return JSON response with status code 500


if __name__ == "__main__":
    app.run(debug=True)
