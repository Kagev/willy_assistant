from flask import Flask, render_template, request
from threading import Timer, Thread, RLock
import logging
from time import time, sleep

lock = RLock()

app = Flask(
    __name__,
    template_folder="../willy_assistant/templates",
    static_url_path="/static",
    static_folder="../willy_assistant/static",
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/button_click", methods=["POST"])
def button_click():
    if request.method == "POST":
        button_clicked = request.form.get("submit_button")

        if button_clicked == "signin":
            return render_template("/signin.html")
        elif button_clicked == "register":
            return render_template("/registration.html")

    # Если кнопка не определена или произошла ошибка, возвращаем шаблон index.html
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

    logging.basicConfig(
        filename="log/app.log",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s",
    )
    first = Timer(0.5, home)
    first.name = "First thread"
    second = Timer(0.7, home)
    second.name = "Second thread"
    logging.debug("Start timers")
    first.start()
    second.start()
    sleep(0.6)
    second.cancel()

    logging.debug("End program")
