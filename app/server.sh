echo "### Update deps"
pip install -r requirements.txt > /dev/null
echo "### Starting server" 
uvicorn main:app --reload --log-level debug