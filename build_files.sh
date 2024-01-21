# build_files.sh
echo "building project packages..."
pip install -r requirements.txt

# make migrations
echo "migrating databases..."
python3.10 manage.py migrate --noinpu

echo "collecting static files..."
python3.10 manage.py collectstatic --noinpu
