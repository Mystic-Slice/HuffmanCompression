#include "Node.cpp"
#include <string>
#include <map>
#include <stack>
using namespace std;
class HuffmanTree {
    public:
        Node* root;
        HuffmanTree(int data, int freq) {
            this->root = new Node(data, freq);
        }

        HuffmanTree(HuffmanTree left, HuffmanTree right) {
            this->root = new Node('\0', left.root->freq + right.root->freq);
            this->root->left = left.root;
            this->root->right = right.root;

            this->root->left->updateCode("0");
            this->root->right->updateCode("1");
        }
        
        map<char, string> characterCodes() {
            map<char, string> charCodeMap;
            stack<Node*> dfsStack;
            dfsStack.push(this->root);
            while(!dfsStack.empty()) {
                Node* node = dfsStack.top(); dfsStack.pop();
                if(node->isLeaf()) {
                    charCodeMap[node->data] = node->code;
                }else{
                    dfsStack.push(node->left);
                    dfsStack.push(node->right);
                }
            }
            return charCodeMap;
        }
};

class HuffmanTreeCompare {
    public:
        bool operator()(HuffmanTree a, HuffmanTree b){
            return a.root->freq > b.root->freq;
        }
};