# web-link-tester
Flask App to scrape and validate links

## Usage

```bash
docker run -d --name link-tester -p 80:80 circa10a/web-link-tester
```

Access via http://localhost

### API Usage

```bash
curl -X POST -d "https://www.github.com" http://localhost/api
```
