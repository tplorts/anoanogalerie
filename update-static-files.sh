echo "~(^_^)~ Compiling LESS into CSS"
cd galeriehome/static/home/styles
lessc styles.less styles.css
lessc multilingual.less multilingual.css
lessc pages/access.less pages/access.css

echo "~(^_^)~ Beginning upload of new static files"
cd ../..
aws s3 sync . s3://anoanogalerie-static/static    --acl public-read
