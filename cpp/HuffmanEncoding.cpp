#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <time.h>
#include "HuffmanTree.cpp"
using namespace std;
int main() {

    clock_t tStart, tEnd;
    tStart = clock();

    cout<<"Reading input text"<<endl;
    string text = "", s;
    ifstream plainTextFile("sample.txt");
    ofstream encodedTextFile("sampleEncoded.txt");
    ofstream metaData("metadata.txt");
    for(string line; getline(plainTextFile, line);){
        text += line + '\n';
    }
    text = text.substr(0, text.size()-1);

    cout<<"Calculating character frequencies"<<endl;
    map<char, int> charFreqMap;
    for(auto c: text) {
        charFreqMap[c]++;
    }

    cout<<"Creating character-frequency heap"<<endl;
    priority_queue<HuffmanTree, vector<HuffmanTree>, HuffmanTreeCompare> treeQueue;
    for(auto p: charFreqMap) {
        HuffmanTree tree(p.first, p.second);
        treeQueue.push(tree);
    }

    cout<<"Creating Huffman Tree"<<endl;
    while(treeQueue.size() != 1) {
        HuffmanTree left = treeQueue.top(); treeQueue.pop();
        HuffmanTree right = treeQueue.top(); treeQueue.pop();
        treeQueue.push(HuffmanTree(left, right));
    }

    cout<<"Obtaining character codes"<<endl;
    HuffmanTree encodedTree = treeQueue.top(); treeQueue.pop();
    map<char, string> charCodeMap = encodedTree.characterCodes();

    metaData<<"Character Codes: "<<endl;
    for(auto p: charCodeMap) {
        if(p.first == '\n') {
            metaData<<"NL "<<p.second<<endl;
            continue;
        }
        metaData<<p.first<<" "<<p.second<<endl;
    }

    cout<<"Creating encoded text"<<endl;
    string encodedText = "";
    for(auto c: text) {
        encodedText += charCodeMap[c];
    }
    encodedTextFile<<encodedText;

    cout<<"Encoding complete"<<endl;

    tEnd = clock();

    int sizeBeforeEncoding = text.size()*8;
    int sizeAfterEncoding = encodedText.size();
    double compressionRatio = (double)sizeBeforeEncoding/(double)sizeAfterEncoding;
    double timeTaken = double(tEnd-tStart)/CLOCKS_PER_SEC;
    metaData<<endl<<"Metrics"<<endl;
    metaData<<setw(25)<<left<<"Number of characters: "<<text.size()<<endl;
    metaData<<setw(25)<<left<<"Size Before Encoding: "<<sizeBeforeEncoding<<endl;
    metaData<<setw(25)<<left<<"Size After Encoding: "<<sizeAfterEncoding<<endl;
    metaData<<setw(25)<<left<<"Compression Ratio: "<<compressionRatio<<endl;
    metaData<<setw(25)<<left<<"Time Taken: "<<timeTaken<<"s"<<endl;
    metaData<<"The encoded text is "<<100.0/compressionRatio<<"% the size of plain text.";

    return 0;
}