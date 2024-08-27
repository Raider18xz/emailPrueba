from flask import Flask, request, render_template, jsonify
import smtplib 
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite CORS en todas las rutas de la aplicación

@app.route("/email", methods=['POST'])
def email():
    if request.method == "POST":
        data = request.json
        print("gola4")
        asunto = data.get("asunto")
        correo = data.get("correo")
        mensaje = data.get("mensaje")
        print(asunto)
        print(correo)
        print(mensaje)

        # Configurar servidor SMTP
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login('rdraider30@gmail.com', 'b s c o k y b y c l g q h f n z')
        print("gola2")
        msg = MIMEText(f"Asunto:{asunto}\n mensaje: {mensaje}")
        msg["From"] = 'rdraider30@gmail.com'
        msg["To"] = correo
        msg["Subject"] = asunto
        print("gola")
        # Enviar el correo
        servidor.sendmail("rdraider30@gmail.com",correo,msg.as_string())
        servidor.quit()
        return jsonify({"message": "Mensaje de correo enviado"}), 200
    else:
        return render_template("email.html")

if __name__ == '__main__':
    app.run(debug=True)
