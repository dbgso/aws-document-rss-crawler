# aws document rss link crawler

## usage

### clone repository

```bash
$ git clone https://github.com/dbgso/aws-document-rss-crawler.git
```

### run splash server

```bash
$ cd amazondocs
$ docker-compose up -d
```

### run spider

```bash
$ pipenv install
$ pipenv shell
$ scrapy runspider amazondocs/spiders/amzondocs.py -o result.csv
```