



x = 2


if x != 1:
    print('please try again')

else: 
    print('all ok')


url = 'https://www.waitrose.com/ecom/products/warburtons-toastie-thick-sliced-white-bread/026841-13059-13060'

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

firstPeriod = find_nth(url, '.', 1) + 1
SecondPeriod = find_nth(url, '.', 2)

print(firstPeriod)
print(SecondPeriod)

print(url[firstPeriod:SecondPeriod])


def checkDomain(url, domain): 
    firstPeriod = find_nth(url, '.', 1) + 1
    SecondPeriod = find_nth(url, '.', 2)
    urlDomain = url[firstPeriod:SecondPeriod]

    if urlDomain == domain:
        return True, print('damain looks good')
    else:
        return False, print('url domain does not match required domain')

checkDomain(url, 'waitrose')
