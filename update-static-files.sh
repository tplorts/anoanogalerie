echo "~~ Compiling LESS into CSS"
cd galeriehome/static/home/styles
lessc styles.less styles.css

echo "~~ collectstatic"
cd ../../../../
python manage.py collectstatic

echo "~~ uploading new static files"
aws s3 sync staticfiles/ s3://anoanogalerie-static/static    --acl public-read
