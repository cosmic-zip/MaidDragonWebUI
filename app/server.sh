echo && echo "### Install dependencies" 
virtualenv -p python3 maid_dragon
source maid_dragon/bin/activate
pip install -r requirements.txt

echo && echo "### Starting server" 
uvicorn main:app --reload