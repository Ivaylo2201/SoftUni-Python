budget = float(input())
gpuCount = int(input())
cpuCount = int(input())
ramCount = int(input())

gpuPrice = 250 * gpuCount
cpuPrice = (0.35 * gpuPrice) * cpuCount
ramPrice = (0.10 * gpuPrice) * ramCount
grandTotal = gpuPrice + cpuPrice + ramPrice

if gpuCount > cpuCount:
    grandTotal = grandTotal - 0.15 * grandTotal

if grandTotal <= budget:
    print(f"You have {format(budget - grandTotal, '.2f')} leva left!")
elif grandTotal > budget:
    print(f"Not enough money! You need {format(grandTotal - budget, '.2f')} leva more!")
