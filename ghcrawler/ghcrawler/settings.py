# Scrapy settings for ghcrawler project

BOT_NAME = 'ghcrawler'

SPIDER_MODULES = ['ghcrawler.spiders']
NEWSPIDER_MODULE = 'ghcrawler.spiders'

# crawl in breadth-first order
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

ITEM_PIPELINES = {
    'ghcrawler.pipelines.GitHubItemStoragePipeline': 800,
}

DOWNLOADER_MIDDLEWARES = {
    'ghcrawler.middlewares.pagination.PaginationMiddleware': 101,
    'ghcrawler.middlewares.filter.DuplicateRequestFilter': 102,
    'ghcrawler.middlewares.logger.LoggerMiddleware': 103,
    'ghcrawler.middlewares.pagination.PaginationAwareShutdownMiddleware': 999,
}

SPIDER_MIDDLEWARES = {
    # switch to custom `DepthMiddleware` to handle pagination properly
    'ghcrawler.middlewares.depth.DepthMiddleware': 900,
    'scrapy.contrib.spidermiddleware.depth.DepthMiddleware': None,
}

USER_AGENT = 'GitHub Crawler (+https://github.com/linhr/dighub)'

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
}

DOWNLOAD_DELAY = 0.75
COOKIES_ENABLED = False