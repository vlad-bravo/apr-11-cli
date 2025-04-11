python -m venv venv
. venv/scripts/activate
pip install -r requirements.txt

python main.py logs/app1.log logs/app2.log logs/app3.log --report handlers
