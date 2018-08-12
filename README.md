# web-link-tester
[![Build Status](https://travis-ci.org/circa10a/web-link-tester.svg?branch=master)](https://travis-ci.org/circa10a/web-link-tester)
[![Docker Repository on Quay](https://quay.io/repository/circa10a/web-link-tester/status "Docker Repository on Quay")](https://quay.io/repository/circa10a/web-link-tester)
![Docker Automated buil](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)
[![](https://images.microbadger.com/badges/image/circa10a/web-link-tester.svg)](https://microbadger.com/images/circa10a/web-link-tester "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/circa10a/web-link-tester.svg)](https://microbadger.com/images/circa10a/web-link-tester "Get your own version badge on microbadger.com")

Flask App to scrape and validate links via GUI or API

## Usage
Why use the web-link-tester?

1) Test your production site via GUI or programmatically to ensure no bad page routes or forgotten references.
2) It's free.

## To deploy the Web App/API
---

### Docker

```bash
docker run -d --name link-tester -p 80:80 circa10a/web-link-tester
```

Access via http://localhost

### Python

```bash
python main.py
```
**Note** This method may require to run as root unless you change the port number in `main.py`

Access via http://localhost

### API Usage

```bash
curl -X POST --data "https://www.github.com" http://localhost/api
```

### Example JSON Output

```bash
$ curl -X POST --data "http://caleblemoine.me" http://localhost/api
{
  "links": [
    {
      "code": 200,
      "url": "https://github.com/circa10a/"
    },
    {
      "code": 200,
      "url": "https://hub.docker.com/r/circa10a/"
    },
    {
      "code": 200,
      "url": "https://circa10a.github.io/monitor/"
    },
    {
      "code": 200,
      "url": "https://circa10a.github.io/smart-mirror/"
    },
    {
      "code": 200,
      "url": "http://scrapeyour.site"
    }
  ]
}
```

### Bonus CLI utility
Can be found in my [python-fun](https://github.com/circa10a/python-fun) repo.

### Stack
- Utilizes gunicorn for multiple workers/threading.
- Python 3
- BeautifulSoup4
- Jquery

## Screenshots

![alt text](https://i.imgur.com/cwC8HcK.png)
![alt text](https://i.imgur.com/9l6OHDX.png)
