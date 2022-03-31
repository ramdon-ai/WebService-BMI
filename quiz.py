from flask import Flask, request

app = Flask(__name__)

@app.route('/hasil', methods=['POST'])
def bmi():
    tinggi = float(request.form.get("tinggi"))
    berat = float(request.form.get("berat"))

    bmi = berat / (tinggi/100)**2
    if bmi <= 18.5:
        hasil = "Kurus"
    elif bmi <= 25:
        hasil = "Normal"
    elif bmi <= 40:
        hasil = "Berlebihan"
    else:
        hasil = "Bahaya"
    data = {'Hasil BMI': bmi,'Tergolong': hasil}
    return data

if __name__ == '__main__':
    app.run(debug=True)