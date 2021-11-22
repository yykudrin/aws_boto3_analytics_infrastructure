sudo apt -y update
sudo apt -y install build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev
sudo apt install -y python3-venv
python3 -m venv env
source env/bin/activate
pip install --upgrade setuptools pip
pip install apache-superset
superset db upgrade
export FLASK_APP=superset
flask fab create-admin --username admin --firstname admin --lastname user --password User1234 --email admin@gd.com
superset init
pip install psycopg2-binary
superset run -h 0.0.0.0 -p 8088 --with-threads --reload --debugger
