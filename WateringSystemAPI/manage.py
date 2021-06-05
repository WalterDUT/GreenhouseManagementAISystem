from app import app
# from waitress import serve


if __name__ == "__main__":
    # serve(app, host="192.168.1.12", port=5000)
    # app.run(debug=True, host="116.105.18.206", port=6969)
    app.run(debug=True, host="0.0.0.0", port=5000) # doi thanh dia chi mang local cua ban

