```python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from .backend_development import loginUser, updateLegislation, updateConstituent, updateCampaign, updateEvent
from .database_development import UserSchema, LegislationSchema, ConstituentSchema, CampaignSchema, EventSchema

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = loginUser(username, password)
        if user:
            login_user(User(user.id))
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password'
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/legislation', methods=['GET', 'POST'])
@login_required
def legislation():
    if request.method == 'POST':
        legislation_data = request.form.to_dict()
        updateLegislation(legislation_data)
    legislations = LegislationSchema.query.all()
    return render_template('legislation.html', legislations=legislations)

@app.route('/constituent', methods=['GET', 'POST'])
@login_required
def constituent():
    if request.method == 'POST':
        constituent_data = request.form.to_dict()
        updateConstituent(constituent_data)
    constituents = ConstituentSchema.query.all()
    return render_template('constituent.html', constituents=constituents)

@app.route('/campaign', methods=['GET', 'POST'])
@login_required
def campaign():
    if request.method == 'POST':
        campaign_data = request.form.to_dict()
        updateCampaign(campaign_data)
    campaigns = CampaignSchema.query.all()
    return render_template('campaign.html', campaigns=campaigns)

@app.route('/event', methods=['GET', 'POST'])
@login_required
def event():
    if request.method == 'POST':
        event_data = request.form.to_dict()
        updateEvent(event_data)
    events = EventSchema.query.all()
    return render_template('event.html', events=events)

if __name__ == "__main__":
    app.run(debug=True)
```