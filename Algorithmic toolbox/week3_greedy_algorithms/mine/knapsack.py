# Uses python3

def looting(n, w, listValues, listWeights):
    value = 0
    ratios = list()
    for i in range(0, n):
        ratios.append(listValues[i] / listWeights[i])
    if len(ratios) == 1:
        value = listValues[0]
    else:
        while w > 0 and len(ratios) > 0:
            best = max(ratios)
            index = ratios.index(best)
            if listWeights[index] <= w:
                w -= listWeights[index]
            else:
                we = w / listWeights[index]
                value += we * ratios[index]
                w = 0
            value += listValues[index]
            ratios.remove(best)
            listWeights.remove(listWeights[index])
            listValues.remove(listValues[index])
    return value

firstdata = input()
tokens = firstdata.split()
n = int(tokens[0])
weight = int(tokens[1])
itemsValue = list()
itemsWeight = list()
for i in range(0,n):
    loot = input()
    items = loot.split()
    itemsValue.append(int(items[0]))
    itemsWeight.append(int(items[1]))

print("%.4f" % looting(n, weight, itemsValue, itemsWeight))
