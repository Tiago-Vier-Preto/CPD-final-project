import os
import struct

class BNode:
    def __init__(self, order, is_leaf=False):
        self.order = order
        self.keys = []
        self.values = []
        self.is_leaf = is_leaf
        self.children = []

    def split(self, parent, index):
        new_node = BNode(self.order, self.is_leaf)
        split_index = self.order - 1

        # move as maiores chaves e valores para o novo nó
        new_node.keys = self.keys[split_index + 1:]
        new_node.values = self.values[split_index + 1:]
        if not self.is_leaf:
            new_node.children = self.children[split_index + 1:]
            self.children = self.children[:split_index + 1]

        # insere a chave e valor médios no nó pai
        if parent is None:
            parent = BNode(self.order, False)
            parent.children.append(self)
            self.parent = parent
        new_node.parent = parent
        if parent.children:
            parent.keys.insert(index, self.keys[split_index])
            parent.values.insert(index, self.values[split_index])
            if index >= len(parent.keys):
                parent.keys.append(new_node.keys[0])
            else:
                parent.keys.insert(index+1, new_node.keys[0])
        else:
            self.is_leaf = True

        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.is_leaf = False


    def is_full(self):
        return len(self.keys) == self.order
    

    def insert_non_full(self, key, value):
        i = len(self.keys) - 1
        if self.is_leaf:
            # se o nó é uma folha, insere a nova chave e valor na posição correta da lista de chaves e valores
            if i + 1 < len(self.keys):
                while i >= 0 and self.keys[i] > key:
                    self.keys[i + 1] = self.keys[i]
                    self.values[i + 1] = self.values[i]
                    i -= 1
            else:
                i = len(self.keys) - 1
            if i < 0:
                self.keys.insert(0, key)
                self.values.insert(0, value)
            else:
                self.keys.insert(i + 1, key)
                self.values.insert(i + 1, value)
        else:
            # se o nó não é uma folha, encontra o filho apropriado e verifica se ele está cheio
            while i >= 0 and self.keys[i] > key:
                i -= 1
            if len(self.children[i + 1].keys) == 2 * self.order - 1:
                # se o filho está cheio, divide-o antes de inserir a nova chave e valor
                self.split(self.children[i], i)
                if i + 1 < len(self.keys):
                    if self.keys[i + 1] < key:
                        i += 1
                else:
                    i = len(self.keys) - 1
            self.children[i + 1].insert_non_full(key, value)


    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and key == self.keys[i]:
            return self.values[i]
        elif self.is_leaf:
            return None
        else:
            return self.children[i].search(key)

class BTree:
    def __init__(self, order, file_name):
        self.order = order
        self.file_name = file_name
        self.root = None
        if os.path.exists(self.file_name):
            self.load()
        else:
            self.create()

    def create(self):
        self.root = BNode(self.order, True)
        self.save()

    def insert(self, key, value):
        if self.root.is_full():
            new_root = BNode(self.order, False)
            new_root.children.append(self.root)
            new_root.split(self.root, 0)
            self.root = new_root
        self.root.insert_non_full(key, value)
        self.save()

    def search(self, key):
        return self.root.search(key)
    
    def save(self):
        with open(self.file_name, 'wb') as f:
            self._save_node(f, self.root)

    def _save_node(self, f, node):
        f.write(struct.pack('i', node.order))
        f.write(struct.pack('i', int(node.is_leaf)))
        f.write(struct.pack('i', len(node.keys)))
        for key, value in zip(node.keys, node.values):
            f.write(struct.pack('i', key))
            f.write(struct.pack('i', value))
        if not node.is_leaf:
            for child in node.children:
                self._save_node(f, child)

    def load(self):
        with open(self.file_name, 'rb') as f:
            self.root = self._load_node(f)

    def _load_node(self, f):
        order = struct.unpack('i', f.read(4))[0]
        is_leaf = bool(struct.unpack('i', f.read(4))[0])
        num_keys = struct.unpack('i', f.read(4))[0]
        keys = []
        values = []
        for i in range(num_keys):
            key = struct.unpack('i', f.read(4))[0]
            value = struct.unpack('i', f.read(4))[0]
            keys.append(key)
            values.append(value)
        node = BNode(order, is_leaf)
        node.keys = keys
        node.values = values
        if not is_leaf:
            for i in range(num_keys + 1):
                child = self._load_node(f)
                node.children.append(child)
        return node
        
