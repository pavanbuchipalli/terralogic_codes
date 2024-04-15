class Strings():
    variables = input("please provide the string to:----- ")

    def number_of_characters(self):
        chars = 0
        for each_char in Strings.variables:
            if each_char != " ":
                chars += 1
        print("count of char:", chars)

    def number_of_each_characters(self):
        self.number_of_characters()
        strin = Strings.variables.replace(" ", "")
        self.count = {}.fromkeys(strin, 0)
        for char in strin:
            if char in self.count:
                self.count[char] += 1
        print("count of each char:", self.count)

    def number_of_duplicate_Characters(self):
        repeated = []
        self.number_of_each_characters()

        for key, values in self.count.items():
            if values > 1:
                repeated.append(key)
        print("Char which is repeated more than once :---",repeated)

    def number_of_words(self):
        self.number_of_duplicate_Characters()
        self.string2 = Strings.variables.split(" ")
        print("Total number of words in the string  :--",len(self.string2))

    def  number_of_duplicate_words(self):
        self.number_of_words()
        non_dupilicate_words =[]
        duplicate = 0
        for i in self.string2:
            if i not in non_dupilicate_words:
                non_dupilicate_words.append(i)
            else:
                duplicate +=1

        print("total number of duplicate words",duplicate)
        print("string_without_dupilicate_words   :---",non_dupilicate_words)

    def Reverse_the_characters(self):
        self.number_of_duplicate_words()
        reverse_str = ""
        for characters in Strings.variables:
            reverse_str= characters + reverse_str
        print("The reverse of entire string  :---",reverse_str)

    def Reverse_the_words(self):
        self.Reverse_the_characters()
        self.Reverse_the_word = ""

        updated_str = Strings.variables.split(" ")

        for sub in range(len(updated_str)):
            sub_str = updated_str[sub]
            self.Reverse_the_word = self.Reverse_the_word + " " + (sub_str[::-1])

        print("Reverse_of_words_in_the_string:--",self.Reverse_the_word)

    def new_str(self):
        self.Reverse_the_words()
        self.new_string = self.Reverse_the_word
        print("Here is the new_string:---:",self.new_string)

    def duplicate_characters (self):
        self.new_str()
        remove_chars = ""
        for remove in self.new_string:
            if remove not in remove_chars or remove == " ":
                remove_chars = remove_chars + remove
        print("latest string after removing the duplicates:----",remove_chars)


obj = Strings()
obj.duplicate_characters()

