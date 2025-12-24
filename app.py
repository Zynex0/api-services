from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "online",
        "developer": "zynex00"
    }

@app.route("/adsoyad")
def adsoyad():
    tc = request.args.get("tc")

    if not tc:
        return {"error": "tc girilmedi"}, 400

    # ŞİMDİLİK DUMMY DATA
    data = {
        "tc": tc,
        "ad": "AHMET",
        "soyad": "YILMAZ"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run()
