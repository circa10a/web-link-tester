# web-link-tester
[![Build Status](https://travis-ci.org/circa10a/web-link-tester.svg?branch=master)](https://travis-ci.org/circa10a/web-link-tester)
[![Docker Repository on Quay](https://quay.io/repository/circa10a/web-link-tester/status "Docker Repository on Quay")](https://quay.io/repository/circa10a/web-link-tester)
![Docker Automated buil](https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg)
[![](https://images.microbadger.com/badges/image/circa10a/web-link-tester.svg)](https://microbadger.com/images/circa10a/web-link-tester "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/circa10a/web-link-tester.svg)](https://microbadger.com/images/circa10a/web-link-tester "Get your own version badge on microbadger.com")

Asynchronous Flask App to scrape and validate links via GUI or REST API

## Usage
Why use the web-link-tester?

1) Test your production site via GUI or programmatically to ensure no bad page routes or forgotten references.
2) It's free.

## To deploy the Web App/API
---

### Docker

```bash
docker run -d --name link-tester -p 8080:8080 circa10a/web-link-tester
```

Access via http://localhost:8080

### Python

```bash
python main.py
```

Access via http://localhost:8080

> Set environment variable `PORT` locally to change listening port from `8080`

### API Usage

```bash
curl -X POST --data '{"url": "https://www.github.com"}' http://localhost:8080/api
```

### Example JSON Output

```bash
$ curl -s -X POST -H "content-type: application/json" --data '{"url": "https://caleblemoine.dev"}' http://localhost:8080/api

{
  "links": [
    {
      "code": 999,
      "url": "https://www.linkedin.com/in/caleblemoine/"
    },
    {
      "code": 200,
      "url": "https://github.com/circa10a"
    },
    {
      "code": 200,
      "url": "https://github.com/circa10a/express-jwt"
    },
    {
      "code": 200,
      "url": "https://github.com/pyouroboros/ouroboros"
    },
    {
      "code": 200,
      "url": "https://github.com/circa10a/filter-object-array"
    },
    {
      "code": 200,
      "url": "https://github.com/circa10a/easy-soap-request"
    },
    {
      "code": 200,
      "url": "https://medium.com/better-programming/how-to-perform-soap-requests-with-node-js-4a9627070eb6"
    },
    {
      "code": 200,
      "url": "https://github.com/circa10a/web-link-tester"
    },
    {
      "code": 200,
      "url": "https://github.com/circa10a/Device-Monitor-Dashboard"
    },
    {
      "code": 200,
      "url": "https://caleblemoine.dev/monitor/"
    },
    {
      "code": 200,
      "url": "https://hub.docker.com/u/circa10a"
    },
    {
      "code": 200,
      "url": "https://caleblemoine.dev/gitfolio/"
    },
    {
      "code": 999,
      "url": "https://www.linkedin.com/in/caleblemoine/"
    },
  ]
}
```

### Stack
- Utilizes gunicorn for multiple workers/threading.
- Python 3
- BeautifulSoup4
- Jquery

## Screenshots

![alt text](https://i.imgur.com/cwC8HcK.png)
![alt text](https://i.imgur.com/9l6OHDX.png)
