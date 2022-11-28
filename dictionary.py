def main():
    theDictionary = generateDictionary()
    theList = generateDictionaryList(theDictionary)
    printList(theList)

    extractedListFromDictionary = getListFromDictionary("simpleList", theDictionary)
    print("Extracted item is:")
    print( extractedListFromDictionary)

    index = grabValueIndex(theList)
    theValue = grabValueByIndex(theList, index)
    printItem(theValue)


def generateDictionary():
    dictA = {"f": "g", "h": "i"}
    dictB = {"j": "k", "l": "m"}
    simpleList = [dictA, dictB]
    theDictionary = {"number": "one", "letter": "a", "simpleList": simpleList}

    return theDictionary

def getListFromDictionary(key,dictionary):
    return dictionary.get(key)

def generateDictionaryList(dictionary):
    if(isinstance(dictionary, dict)):
        theDictList = list(dictionary.values())
    else:
        return []
    return theDictList

def grabValueIndex(dictList):
    index = dictList.index("a")
    return index

def grabValueByIndex(theList, index):
    return theList[index]

def printList(list):
    for item in list:
        print(item)

def printItem(string):
    print(string)

if __name__ == "__main__":
    main()