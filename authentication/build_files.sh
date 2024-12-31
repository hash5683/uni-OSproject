
echo "BUILD START"
python3.9 -m pip install -r requierements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"

