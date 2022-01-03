import heapq
import time
from HuffmanTree import HuffmanTree

start = time.time()

print("Reading input text")
with open("sample.txt", "r") as plainTextFile:
    # text = "\n".join([line.strip() for line in plainTextFile])
    text = plainTextFile.read()

print("Calculating character frequencies")
charFreqMap = {}
for c in text:
    if c in charFreqMap:
        charFreqMap[c] += 1
    else:
        charFreqMap[c] = 1
        
print("Creating character-frequency heap")
treeQueue = []
heapq.heapify(treeQueue)
for key, value in charFreqMap.items():
    tree = HuffmanTree.fromData(key, value)
    heapq.heappush(treeQueue, tree)

print("Creating Huffman Tree")
while len(treeQueue) != 1:
    left = heapq.heappop(treeQueue)
    right = heapq.heappop(treeQueue)
    heapq.heappush(treeQueue, HuffmanTree.fromTrees(left, right))

print("Obtaining character codes")
encodedTree = heapq.heappop(treeQueue)
charCodeMap = encodedTree.characterCodes()

with open("metadata.txt", "w") as metadataFile:
    print("Character Codes: ", file=metadataFile)
    for key, value in charCodeMap.items():
        if key == '\n':
            print("NL", value, file=metadataFile)
        else:
            print(key, value, file=metadataFile)

print("Creating encoded text")
encodedText = ""
for c in text:
    encodedText += charCodeMap[c]
with open("sampleEncoded.txt", "w") as ofile:
    print(encodedText, file=ofile)

print("Encoding complete")

end = time.time()

sizeBeforeEncoding = len(text)
sizeAfterEncoding = len(encodedText)//8
compressionRatio = round(sizeBeforeEncoding/sizeAfterEncoding, 2)
timeTaken = round(end-start, 3)

with open("metadata.txt", "a") as metadataFile:
    print(file=metadataFile)
    print("Metrics", file=metadataFile)
    print("Number of characters: ", len(text), file=metadataFile)
    print("Size Before Encoding: ", sizeBeforeEncoding, file=metadataFile)
    print("Size After Encoding:  ", sizeAfterEncoding, file=metadataFile)
    print("Compression Ratio:    ", compressionRatio, file=metadataFile)
    print(f'Time Taken:            {timeTaken}s', file=metadataFile)
    print(f'The encoded text is {round(100/compressionRatio, 3)}% the size of plain text', file=metadataFile)
