from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
            verify_token = "midemo123"  # tu token
                    token = request.args.get("hub.verify_token")
                            challenge = request.args.get("hub.challenge")
                                    if token == verify_token:
                                                return challenge
                                                        return "Token inválido", 403
                                                            elif request.method == "POST":
                                                                    data = request.get_json()
                                                                            print("Mensaje recibido:", data)
                                                                                    return "Evento recibido", 200

                                                                                    if __name__ == "__main__":
                                                                                        app.run(host="0.0.0.0", port=10000)
