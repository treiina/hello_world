import os


class Entry:
    def __init__(self, key, value1, value2=None, value3=None):
        self.hash = None
        self.key = key
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.is_deleted = False


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10
        self.load_factor = .75
        self.current_size = 0
        file_hashes = open('service_files/hashes.txt', 'w')
        file_hashes.close()
        file_output_result_search = open('service_files/output_result_search.txt', 'w')
        file_output_result_search.close()
        file_result_search = open('service_files/result_search.txt', 'w')
        file_result_search.close()

    def repr(self, path='service_files/hashes.txt'):
        out_file = open(path, 'r')
        hashes = out_file.read().splitlines()
        out_file.close()
        output_list = []
        for hash_ in hashes:
            hash_ = int(hash_)
            record = (self.table[int(hash_)].key, self.table[int(hash_)].value1, self.table[int(hash_)].value2,
                      self.table[int(hash_)].value3)
            output_list.append(record)
        return output_list

    def str(self):
        out_file = open('service_files/hashes.txt', 'r')
        hashes = out_file.read().splitlines()
        out_file.close()
        for hash_ in hashes:
            print(self.str_element(int(hash_)))
        return None

    def str_element(self, hash_):
        if self.table[hash_].value2 is None and self.table[hash_].value3 is None:
            item = ['{!r}: {!r}'.format(self.table[hash_].key, self.table[hash_].value1)]
        elif self.table[hash_].value2 is None:
            item = ['{!r}: [{!r}, {!r}]'.format(self.table[hash_].key, self.table[hash_].value1,
                                                self.table[hash_].value3)]
        elif self.table[hash_].value3 is None:
            item = ['{!r}: [{!r}, {!r}]'.format(self.table[hash_].key, self.table[hash_].value1,
                                                self.table[hash_].value2)]
        else:
            item = ['{!r}: [{!r}, {!r}, {!r}]'.format(self.table[hash_].key, self.table[hash_].value1,
                                                      self.table[hash_].value2, self.table[hash_].value3)]
        return '{' + ', '.join(item) + '}'

    def add(self, key, value1=None, value2=None, value3=None):
        entry = Entry(key, value1, value2, value3)
        entry.hash = self.__get_hash_code(key)
        if self.table[entry.hash] is None or self.table[entry.hash].is_deleted:
            self.table[entry.hash] = entry
            in_file = open('service_files/hashes.txt', 'a')
            # print("def add (hashes.txt): ", entry.hash)
            print(entry.hash, sep='\n', file=in_file)
            in_file.close()
            self.current_size += 1
            if float(self.current_size) / len(self.table) >= self.load_factor:
                self.__resize_table()

    def getitem(self, key):
        index = self.__get_hash_code(key)
        if self.table[index] is not None:
            if self.table[index].key == key:
                if self.table[index].is_deleted:
                    raise KeyError('Key is not in the map')
                else:
                    in_file = open('service_files/result_search.txt', 'a')
                    print(self.table[index].hash, sep='\n', file=in_file)
                    in_file.close()
        elif self.table[index] is None:
            raise KeyError('Key is not in the data base')
        else:
            raise KeyError('Hmm something has gone wrong here')

    def getitem_value(self, value1=None, value2=None, value3=None):
        self._binary_search(value1, value2, value3)
        in_file = open('service_files/output_result_search.txt', 'r')
        keys = in_file.read().splitlines()
        in_file.close()
        for key in keys:
            self.getitem(key)

    def _binary_search(self, value1=None, value2=None, value3=None):
        file_result_search = open('service_files/result_search.txt', 'w')
        file_result_search.close()
        in_file = open('service_files/output_result_search.txt', 'w')
        out_file = open('service_files/hashes.txt', 'r')
        hashes = out_file.read().splitlines()
        # print("\ndef _binary_search: ", hashes)
        # print("\ndef _binary_search: ", value1, value2, value3)
        out_file.close()
        if (value1 is not None) and (value2 is None) and (value3 is None):
            for hash_ in hashes:
                if self.table[int(hash_)].value1 == value1:
                    print(self.table[int(hash_)].key, sep='\n', file=in_file)
        elif (value1 is None) and (value2 is not None) and (value3 is None):
            for hash_ in hashes:
                if self.table[int(hash_)].value2 == value2:
                    print(self.table[int(hash_)].key, sep='\n', file=in_file)
        elif (value1 is None) and (value2 is None) and (value3 is not None):
            for hash_ in hashes:
                if self.table[int(hash_)].value3 == value3:
                    print(self.table[int(hash_)].key, sep='\n', file=in_file)
        else:
            return 'Error! Please, chose ONE field of search!'
        in_file.close()

    def __get_hash_code(self, key):
        return hash(key) % len(self.table)

    def __resize_table(self):
        new_table = [None] * (len(self.table) * 2)
        for i in range(len(self.table)):
            new_table[i] = self.table[i]

        self.table = new_table

    def change(self, key, value1=None, value2=None, value3=None):
        entry = Entry(key, value1, value2, value3)
        entry.hash = self.__get_hash_code(key)
        if self.table[entry.hash] is not None:
            self.table[entry.hash] = entry

    def delitem(self, key):
        index = self.__get_hash_code(key)
        if self.table[index] is not None:
            if self.table[index].key == key:
                if self.table[index].is_deleted:
                    raise KeyError('Key is not in the map')
                else:
                    self.table[index].is_deleted = True

                    out_file = open('service_files/hashes.txt', 'r')
                    hashes = out_file.read().splitlines()
                    out_file.close()

                    hashes.remove(str(self.table[index].hash))

                    in_file = open('service_files/hashes.txt', 'w')
                    # print("delitem (hashes.txt, w): ", hashes)
                    for hash_ in hashes:
                        print(hash_, sep='\n', file=in_file)
                    in_file.close()

                    self.current_size -= 1

    def delitem_value(self, value1=None, value2=None, value3=None):
        self._binary_search(value1, value2, value3)
        in_file = open('service_files/output_result_search.txt', 'r')
        keys = in_file.read().splitlines()
        in_file.close()
        for key in keys:
            self.delitem(key)

    def open_data_base(self, name_file):
        if self.table:
            self.clean()
        with open(name_file) as out_file:
            data = out_file.read().splitlines()
        out_file.close()
        for item in data:
            item = item.split(';')
            self.add(item[0], item[1], item[2], item[3])
        return None

    def save_data_base(self, name_file):
        in_file = open(name_file, 'w')
        out_file = open('service_files/hashes.txt', 'r')
        hashes = out_file.read().splitlines()
        out_file.close()
        for hash_ in hashes:
            # print("save_data_base: ", self.table[int(hash_)])
            print(self.table[int(hash_)].key, self.table[int(hash_)].value1, self.table[int(hash_)].value2,
                  self.table[int(hash_)].value3, sep=';', file=in_file)
        in_file.close()

    def clean(self):
        file_hashes = open('service_files/hashes.txt', 'w')
        file_hashes.close()
        file_output_result_search = open('service_files/output_result_search.txt', 'w')
        file_output_result_search.close()
        file_result_search = open('service_files/result_search.txt', 'w')
        file_result_search.close()
        self.table = [None] * 10
        self.current_size = 0

    def __del__(self):
        os.remove('service_files/hashes.txt')
        os.remove('service_files/output_result_search.txt')
        os.remove('service_files/result_search.txt')
        del self.table
        del self.load_factor
        del self.current_size
