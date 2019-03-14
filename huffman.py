'''Implement Huffman’s greedy algorithm for encoding symbols. Take as input a list of n
symbols and their corresponding frequencies. After constructing the optimal tree, your algorithm
should print the encoding of each of the symbols. Also print the size of the encoded file.'''


# Huffman Encoding and Decoding....!!!

import heapq

class Node:
    def __init__(self,sym,freq):
        self.sym=sym
        self.freq=freq
        self.left=None
        self.right=None

    def __lt__(self,other):
        if self is None or other is None:
            return
        if self.freq<other.freq:
            return True
        return False

    def __eq__(self,other):
        if self is None or other is None:
            return 
        if self.freq==other.freq:
            return True
        return False

class Huffman:
    def __init__(self,text):
        self.heap=[]
        self.dictionary={}
        self.codes={}
        self.reverse_codes={}
        self.text=text

    def add_sym_freq(self):

        for i in self.text:
            if not i in self.dictionary:
                self.dictionary[i]=0
            self.dictionary[i]+=1
        return self.dictionary

    def make_heap(self):
        for key in self.dictionary:
            node=Node(key,self.dictionary[key])
            heapq.heappush(self.heap,node)

    def merge_nodes(self):
        while len(self.heap)>1:
            node1=heapq.heappop(self.heap)
            node2=heapq.heappop(self.heap)

            merged=Node(None,node1.freq+node2.freq)
            merged.left=node1
            merged.right=node2

            heapq.heappush(self.heap,merged)

    def get_codes(self):
        root=heapq.heappop(self.heap)
        curr_code=""
        self.get_codes_recurse(root,curr_code)

    def get_codes_recurse(self,root,curr_code):
        if root is None:
            return 
        if root.sym != None:
            self.codes[root.sym]=curr_code
            self.reverse_codes[curr_code]=root.sym
            return
        self.get_codes_recurse(root.left,curr_code+"0")
        self.get_codes_recurse(root.right,curr_code+"1")

    def get_encoded_code(self):
        text_encoded=""
        for j in self.text:
            text_encoded+=self.codes[j]
        return text_encoded

    def get_decoded_text(self,text):
        res = ""
        while text:
            for k in self.reverse_codes:
                if text.startswith(k):
                    res += self.reverse_codes[k]
                    text = text[len(k):]
        return res



    def compression(self):
        sum_original=0
        sum_encoded=0
        for j in self.text:
            sum_original+=len(str("{0:b}".format(ord(j))))

        for s in self.text:
            sum_encoded+=len(str(self.codes[s]))

        print("Encoded File Size:",sum_encoded,"bits ||","Original File Size:",sum_original,"bits")

        return (sum_encoded/sum_original)*100


p=input("-> Enter string to be encoded: ")
H=Huffman(p)
H.add_sym_freq()
H.make_heap()
H.merge_nodes()
H.get_codes()
encoded_text=H.get_encoded_code()
print(encoded_text)
print("%Compression =",H.compression())

q=input("->Enter string to be decoded: ")
print(H.get_decoded_text(q))

