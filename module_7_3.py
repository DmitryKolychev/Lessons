import re


class WordsFinder:
    file_names = []
    all_words = {}

    def __init__(self, *names):
        self.names = names
        for name in names:
            WordsFinder.file_names.extend(name.split(', '))
        print(WordsFinder.file_names)

    def get_all_words(self):
        for name in self.names:
            with open(name, 'r', encoding='utf-8') as file:
                content = file.read().lower()
                content = re.sub(r'[,\.=!?;:\s-]+', ' ', content)  # ищет в строке все совпадения
                # "r перед строкой указывает, что обратные слэши не интерпретируются"
                # "[,\.=!?;:\s-] - что меняем, "+" - в любом сочетании"
                # "content - где ищем"
                words = content.split()
                WordsFinder.all_words[name] = words
        return WordsFinder.all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = f'позиция {words.index(word)+1}'
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = f'количесвто {words.count(word)}'
        return result


tf = WordsFinder('test_file.txt')
tf.get_all_words()
print(WordsFinder.all_words)
print(tf.find('text'))
print(tf.count('text'))


f_list = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
f_list.get_all_words()
print(WordsFinder.all_words)
f = input('Введите искомое слово: ')
print(f_list.find(f))
print(f_list.count(f))
