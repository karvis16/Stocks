"""
Test file to pull some financial and maps API information and process them in any meaningful way
"""
def PullCompanyInfo(yearsBack = 1, Companies=['GOOG']):
    from urllib2 import Request, urlopen, URLError
    YahooPullRequestStr = "http://ichart.finance.yahoo.com/table.csv?"
    """
    s symbol of the stock
    a is start month
    b is start day
    c is start year
    d is end month
    e is end day
    f is end year
    g is interval type (d is daily)
    
    """
    
    #keep this format to later allow for custom tracking
    startmon = 0
    startday = 1
    startyear = 2014 - (yearsBack -1)
    endmon = 11
    endday = 31
    endyear = 2014
    
    
    RequestStrings = []
    
    for i in Companies:
        reqString = YahooPullRequestStr + "s={}&a={}&b={}&c={}&d={}&e={}&f={}&g=d&ignore=.csv".format(i, startmon, startday, startyear, endmon, endday, endyear)
        RequestStrings.append(reqString)
    
    pulledInfo = []
    
    for j in range(len(RequestStrings)):
        request = Request(RequestStrings[j])
        try:
            print "Pulling {} data".format(Companies[j])
            response = urlopen(request)
            data = response.read()
            pulledInfo.append( (Companies[j], data) )
            print "Information pulled successfully"
        except URLError, e:
            print "no info for you", e
    
    return pulledInfo    
# now we have an array of company name and raw data tuples. Let's deal with this raw data:

def CleanPulledInfo(pulledInfo):
    print "Cleaning data"
    finalData = []
    for i in pulledInfo:
        name = i[0]
        data = i[1].split("\n")
        clean = []
        data.reverse()          # the data is retrieved started from the last day back to the first day.
        for j in data[1:-1]:   # this is because the first and last lines are useless to us
            x = j.split(',')
            clean.append(float(x[-1]))
        finalData.append( (name, clean))
    print "Data cleaned"
    return finalData
    
def PlotInfo(finalData,  canvas = current, index = 0, labelIt = True, subbed = True):
    import pylab
    if index == 0:
        n = len(finalData)
        for i in range(n):
            x = range(len(finalData[i][1])) # just in case we're dealing with a leapyear ;)
            y = finalData[i][1]
            if subbed:
                pylab.subplot(n,1,i+1)
            print "plotting data for " + finalData[i][0]
            pylab.plot(x,y, label= finalData[i][0])
            if labelIt:
                pylab.legend()
    else:
        x = range(len(finalData[index-1][1]))
        y = finalData[index-1][1]
        pylab.plot(x,y, label= finalData[index][0])
    if labelIt:
        pylab.legend()
    pylab.show()

a = PullCompanyInfo()
b = CleanPulledInfo(a)
PlotInfo(b)