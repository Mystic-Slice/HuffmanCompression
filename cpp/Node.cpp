#include <string>
using namespace std;
class Node {
    public:
        int data;
        int freq;
        string code;
        Node* left;
        Node* right;

        Node(int data, int freq) {
            this->data = data;
            this->freq = freq;
            this->code = "";
            this->left = nullptr;
            this->right = nullptr;
        }

        bool isLeaf() {
            return !left && !right;
        }

        void updateCode(string addedChar) {
            this->code = addedChar + this->code;
            if(this->left) this->left->updateCode(addedChar);
            if(this->right) this->right->updateCode(addedChar);
        }
};