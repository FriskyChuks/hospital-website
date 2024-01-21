# build_files.sh
echo "building project packages..."
pip install -r requirements.txt

# make migrations
echo "migrating databases..."
python3.9 manage.py migrate --noinpu

echo "collecting static files..."
python3.9 manage.py collectstatic --noinpu
