from flask import Flask, render_template

app = Flask(__name__)

DASHBOARD_URL = "https://public.tableau.com/views/EV_Charge_and_Range_Analysis/Dashboard3?:showVizHome=no&:embed=true"
STORY_URL = "https://public.tableau.com/views/EV_Charge_and_Range_Analysis/StoryofElectricCarsinIndia?:showVizHome=no&:embed=true"

@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL
    )

@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        dashboard_url=DASHBOARD_URL
    )

@app.route("/story")
def story():
    return render_template(
        "story.html",
        story_url=STORY_URL
    )

if __name__ == "__main__":
    app.run(debug=True)
