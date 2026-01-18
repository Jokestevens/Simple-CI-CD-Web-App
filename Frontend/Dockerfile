FROM nginx:alpine

# Copy static site
COPY index.html /usr/share/nginx/html/index.html
COPY styles.css /usr/share/nginx/html/styles.css
COPY app.js /usr/share/nginx/html/app.js

# Nginx config with reverse proxy for /api -> backend
COPY nginx.conf /etc/nginx/conf.d/default.conf
