penPackets = int(input())
markerPackets = int(input())
litresChemical = int(input())
percentDiscount = int(input())
discount = percentDiscount / 100
sumBefore = ((penPackets * 5.80) + (markerPackets * 7.20) + (litresChemical * 1.20))
sumAfter = sumBefore - sumBefore * discount
print(sumAfter)
