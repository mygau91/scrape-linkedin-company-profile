from googlesearch import search   
import csv
import main as dataScraper

def main(): 
    links = []
    file = open("linkedins.csv", encoding = "utf8")

    csvreader = csv.reader(file)
    for row in csvreader:
        if len(row) == 0:
            links.append("Blank")
        else:
            links.append(row[0])
        
    
    uncleanedData = dataScraper.main(links)
    industry = []
    country = []
    for item in range(len(uncleanedData)):
        if item % 2 == 0 or item == 0:
            industry.append(uncleanedData[item])
        else:
            country.append(uncleanedData[item])

    write_csv(industry, "industry")
    write_csv(country, "country")

def write_csv(data, filename):
    
    # PreCon: Data must be a list, filename MUST be a string
    with open(filename+".csv", "w", encoding = "utf8") as f:
        for line in data:
            f.write("%s\n"%line)



if __name__ == '__main__':
    html_extract = main()
