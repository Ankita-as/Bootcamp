 Set Up a Virtual Environment
python -m venv venv

#For activation of virtual environment
.\venv\Scripts\activate

Create or update a requirements.txt
pip install -r requirements.txt
fastapi
uvicorn

start Uvicorn
uvicorn dashboard:app --reload

python main.py --trace
http://127.0.0.1:8000/
http://127.0.0.1:8000/stats