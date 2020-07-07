import docx2txt
import re
import sys


class ReferenceValidator:

    def __init__(self, word_document, num_references):
        self.file = word_document
        self.num_references = num_references

    def validateReferences(self):
        pass

    def readFile(self):
        result = docx2txt.process(self.file)
        compare = [i for i in range(1, self.num_references)]
        for reference_numbers in re.findall(r"\[(\w+)\]", result):
            reference_numbers = int(reference_numbers)
            if int(reference_numbers) in compare:
                compare.remove(reference_numbers)
        compare = [str(ref) for ref in compare]
        if compare:
            print("References not cited: {}".format(", ".join(compare)))
        else:
            print("All references cited!")


def main():
	if len(sys.argv) > 2: 
		word_document = sys.argv[1]
		num_references = int(sys.argv[2])
		reference_validator = ReferenceValidator(word_document, num_references)
		reference_validator.readFile()
	else:
		print("Please pass arguments to program!")
		print("Sample usage") 
		print("python3 validateReferences.py <word_document> <number_of_references>") 
		exit() 

if __name__ == "__main__":
	main() 
