#!/usr/bin/python

#need to do: compound words
#also: if no box data on occupation/nationality exists... add more value to head and title
#

#file = 'michael'
#keyword = "Dancer"
#keyword2 = ["Voice Actor", "Singer-songwriter", "Screenwriter"]
#keyword =  keyword.lower() #searches lowercase files

#shortened words must match from the same point of a word

def exactWordStart(start, end, count, keyword, lines):
    value = 0
    for i in range(1,count):
        ##print(lines[lines.find(keyword)-1], end = "")
        ##print(lines[lines.find(keyword)])
        if(lines[lines.find(keyword)-1] == ' '):
            value = value + 1
        start = lines.find(keyword)
    return value

def calculateScore( lines, keyword, repeat=0):
    
    if(keyword == "United States of America"):
        keyword = "American"
    if(keyword == "United Kingdom"):
        list1 = [calculateScore(lines,"Britain"), calculateScore(lines,"England"), calculateScore(lines,"Scotland"), calculateScore(lines,"Wales"), calculateScore(lines,"Ireland")]
        return round(max(list1))


    ##print("----------")
    ##print(keyword)
    value2 = -1
    value3 = -1
    
    if(keyword.find(' ') >= 0): ## assuming only 2
        if(repeat==0):
            value2 = calculateScore(lines,keyword[0:keyword.find(' ')])
            value3 = calculateScore(lines,keyword[keyword.find(' ')+1:len(keyword)])
    if(keyword.find('-') >= 0): ## assuming only 2
        if(repeat==0):
            value2 = calculateScore(lines,keyword[0:keyword.find('-')])
            value3 = calculateScore(lines,keyword[keyword.find('-')+1:len(keyword)])

    start = lines.find('vcard')
    end = lines.find('</table>')
    rules = [start == -1, end == -1]
    if all(rules): # case of no box
        start = 1
        end = 2
    occsearch = lines.count("Occupation", start, end)
    ##print(occsearch)
    box = lines.count(keyword, start, end)
    box = box + lines.count(keyword.lower(), start, end)
        #if(repeat == 1):
        #box = exactWordStart(start, end, box, keyword, lines)
    ##print("vcard search", end="")
    ##print(start, end=" ")
    ##print(end, end=" ")

    #for i in range(start,end): ##print(lines[i] , end="")
    ##print(box)

    start = end
    #end = lines.find('".', start)
    end = lines.find('</p>', start)
    if(end - start > 1000):
        end = start + 1000
    head = lines.count(keyword, start, end)
    head = head + lines.count(keyword.lower(), start, end)
        #if(repeat == 1):
#head = exactWordStart(start, end, head, keyword, lines)
    ##print("head search", end="") ## MAKE SURE TO REMOVE
    ##print(start, end=" ")
    ##print(end, end=" ")
    #for i in range(start,end): ##print(lines[i] , end="")
    ##print(head)

    start = end
    end = lines.find('<h2>', start)
    title = lines.count(keyword, start, end)
    title = title + lines.count(keyword.lower(), start, end)
        # if(repeat == 1):
#title = exactWordStart(start, end, title, keyword, lines)
    ##print("title search", end="") ## MAKE SURE TO REMOVE
    ##print(start, end=" ")
    ##print(end, end=" ")
    #for i in range(start,end): ##print(lines[i] , end="")
    ##print(title)

    start = end
    end = lines.find('"reflist', start)
    body = lines.count(keyword, start, end)
    body = body + lines.count(keyword.lower(), start, end)
        #if(repeat == 1):
#body = exactWordStart(start, end, body, keyword, lines)
    ##print("body search", end="") ## MAKE SURE TO REMOVE
    ##print(start, end=" ")
    ##print(end, end=" ")
    ##print(body)

    start = end
    ref = lines.count(keyword, start)
    ref = ref + lines.count(keyword.lower(), start, end)
        #if(repeat == 1):
#ref = exactWordStart(start, end, ref, keyword, lines)
    ##print("reference search", end="") ##MAKE SURE TO REMOVE
    ##print(start, end=" ")
    ##print(end, end=" ")
    ##print(ref)

    value = 0

    rules = [ref >= 1]
    if all(rules):
        value = value + 1

    rules = [body >= 1,
             body <= 4]
    if all(rules):
        value = value + 1
    rules = [body >= 5]
    if all(rules):
        value = value + 2

    if (title >= 1):
        value = value + 2

    if (head >= 1):
        value = value + 4

    if (box >=1):
        value = value + 4
    rules = [occsearch == 0, value > 0]
    if all(rules):
        value = value + 2


    rules = [value == 0, repeat == 0]
    if all(rules):
        ##print("repeat required")
        ## try a partial keyword Physicist -> Physi
        if (len(keyword[0:len(keyword)//2]) >= 4):
            value = calculateScore(lines, keyword[0:len(keyword)//2], 1)
        else:
            value = calculateScore(lines, keyword[0:4], 1)
        ##print("new value is ", end="")
        ##print(value)
        if(value > 10):
            ##print("overfitting")
            value = 0
        if (value > 6):
            value = 5
        elif (value > 3):
            value = value - 2
        elif (value > 0):
            value = 1
        else:
            value = 0
    
    if (value2 == -1):
        ##print("finvalue is ", end="")
        ##print(value)
        return round(value)
    else:
        ##print(value2)
        ##print(value3)
        return round((6*(value + value2 + value3)/30)) #5,6,7



## comment out

#print("---Ezra---")
#print(calculateScore(open('names/ezra', 'r').read(), "Screenwriter"), "2")
#print(calculateScore(open('names/ezra', 'r').read(), "Production designer"), "2")
#print(calculateScore(open('names/ezra', 'r').read(), "Film Producer"), "6")
#print(calculateScore(open('names/ezra', 'r').read(), "Film Editor"), "5")
#print(calculateScore(open('names/ezra', 'r').read(), "Film Director"), "6")
#print(calculateScore(open('names/ezra', 'r').read(), "Film Art Director"), "3")
#print("---Arnold---")
#print(calculateScore(open('names/arnold', 'r').read(), "Writer"), "0")
#print(calculateScore(open('names/arnold', 'r').read(), "Television director"), "1")
#print(calculateScore(open('names/arnold', 'r').read(), "Politician"), "7")
#print(calculateScore(open('names/arnold', 'r').read(), "Investor"), "2")
#print(calculateScore(open('names/arnold', 'r').read(), "Film Producer"), "2")
#print(calculateScore(open('names/arnold', 'r').read(), "Businessperson"), "1")
#print(calculateScore(open('names/arnold', 'r').read(), "Bodybuilder"), "5")
#print(calculateScore(open('names/arnold', 'r').read(), "United States of America"), "7")
#print("---Dr.Dre---")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Songwriter"), "4")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Record producer"), "6")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Rapper"), "7")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Film Producer"), "0")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Film Director"), "0")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Entrepreneur"), "5")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Disc jockey"), "0")
#print(calculateScore(open('names/Dr._Dre', 'r').read(), "Actor"), "0")
#print("---H.W.Bush---")
#print(calculateScore(open('names/hwbush', 'r').read(), "Politician"), "7")
#print(calculateScore(open('names/hwbush', 'r').read(), "Military advisor"), "2")
#print(calculateScore(open('names/hwbush', 'r').read(), "Entrepreneur"), "1")
#print(calculateScore(open('names/hwbush', 'r').read(), "Businessperson"), "3")
#print("---Johann---")
#print(calculateScore(open('names/johann', 'r').read(), "Poet"), "6")
#print(calculateScore(open('names/johann', 'r').read(), "Playwright"), "6")
#print(calculateScore(open('names/johann', 'r').read(), "Philosopher"), "4")
#print(calculateScore(open('names/johann', 'r').read(), "Novelist"), "6")
#print(calculateScore(open('names/johann', 'r').read(), "Lawyer"), "0")
#print(calculateScore(open('names/johann', 'r').read(), "Diplomat"), "2")
#print(calculateScore(open('names/johann', 'r').read(), "Civil servant"), "2")
#print("---LilWayne---")
#print(calculateScore(open('names/lilwayne', 'r').read(), "Songwriter"), "6")
#print(calculateScore(open('names/lilwayne', 'r').read(), "Record producer"), "4")
#print(calculateScore(open('names/lilwayne', 'r').read(), "Rapper"), "7")
#print(calculateScore(open('names/lilwayne', 'r').read(), "Businessperson"), "1")
#print(calculateScore(open('names/lilwayne', 'r').read(), "Actor"), "0")
#print("---AdamSandler---")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Voice Actor"), "3")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Television Producer"), "1")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Songwriter"), "1")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Screenwriter"), "3")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Film Producer"), "4")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Comedian"), "7")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Actor"), "7")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Sailor"), "0")
#print(calculateScore(open('names/Adam_Sandler', 'r').read(), "Artist"), "7")
#print("---KylieMinogue---")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Songwriter"), "7")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Singer"), "7")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Showgirl"), "2")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Screenwriter"), "0")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Record producer"), "3")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Film Score Composer"), "0")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Film Producer"), "2")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Fashion Designed"), "1")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Entrepreneur"), "0")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Author"), "0")
#print(calculateScore(open('names/Kylie_Minogue', 'r').read(), "Actor"), "3")
#print("---Ben Stein---")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Voice Actor"), "2")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Teacher"), "2")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Speechwriter"), "3")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Screenwriter"), "0")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Professor"), "1")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Lawyer"), "3")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Humorist"), "4")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Game Show Host"), "4")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Financial Advisor"), "2")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Economist"), "3")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Commentator"), "6")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Comedian"), "4")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Author"), "4")
#print(calculateScore(open('names/Ben_Stein', 'r').read(), "Actor"), "7")
#print("---Jesus---")
#print(calculateScore(open('names/Jesus', 'r').read(), "Prophet"), "6")
#print(calculateScore(open('names/Jesus', 'r').read(), "Preacher"), "5")
#print(calculateScore(open('names/Jesus', 'r').read(), "Carpenter"), "2")
#print("---Paul---")
#print(calculateScore(open('names/Paul_the_Apostle', 'r').read(), "Writer"), "6")
#print(calculateScore(open('names/Paul_the_Apostle', 'r').read(), "Tentmaker"), "3")
#print(calculateScore(open('names/Paul_the_Apostle', 'r').read(), "Writer"), "3")
#print(calculateScore(open('names/Paul_the_Apostle', 'r').read(), "Writer"), "5")
#print("---Hitler---")
#print(calculateScore(open('names/Adolf_Hitler', 'r').read(), "Writer"), "1")
#print(calculateScore(open('names/Adolf_Hitler', 'r').read(), "Soldier"), "4")
#print(calculateScore(open('names/Adolf_Hitler', 'r').read(), "Politician"), "7")
#print(calculateScore(open('names/Adolf_Hitler', 'r').read(), "Artist"), "0")
#print("---Peter---")
#print(calculateScore(open('names/Saint_Peter', 'r').read(), "Fisherman"), "1")
#print(calculateScore(open('names/Saint_Peter', 'r').read(), "Bishop"), "6")
#print("---Madonna---")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Singer-songwriter"), "7")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Screenwriter"), "0")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Philanthropist"), "1")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Film Producer"), "0")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Film Director"), "1")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Entrepreneur"), "1")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Dancer"), "5")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Composer"), "2")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Author"), "2")
#print(calculateScore(open('names/Madonna_entertainer', 'r').read(), "Actor"), "4")
#print("---Washington---")
#print(calculateScore(open('names/George_Washington', 'r').read(), "Surveyor"), "2")
#print(calculateScore(open('names/George_Washington', 'r').read(), "Soldier"), "2")
#print(calculateScore(open('names/George_Washington', 'r').read(), "Politician"), "7")
#print(calculateScore(open('names/George_Washington', 'r').read(), "Military Officer"), "6")
#print(calculateScore(open('names/George_Washington', 'r').read(), "Farmer"), "0")
#print("---Nolan---")
#print(calculateScore(open('Christopher_Nolan', 'r').read(), "United Kingdom"), "7")
#print(calculateScore(open('Christopher_Nolan', 'r').read(), "United States of America"), "4")
