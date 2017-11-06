# web-link-tester
Flask App to scrape and validate links

## Usage

```bash
docker run -d --name link-tester -p 80:5000 circa10a/web-link-tester
```

Access via http://localhost

### API Usage

```bash
curl -X POST --data "https://www.github.com" http://localhost/api
```
### Stack
- Utilizes uwsgi/nginx for multiple workers/threading.
- Python 3
- BeautifulSoup4
- Jquery
