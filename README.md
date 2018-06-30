# yellowscrape
Scrape and save data from German yellowpages (Gelbeseiten)

## Running the Scrapy Spider

To run this spider, download the whole repository into your machine, open your Terminal, navigate to its folder, and then type:

```
scrapy crawl ylp
```
If you rather want to generate an CSV file of the data scraped by Scrapy, type the following:

```
scrapy crawl ylp -o gelbeseiten.csv
```

### Disclaimer

I know, this is not the most elegant method. In a future version I will consider pagination. But for now. It works. Run it, lean back, let scrapy do the work.
