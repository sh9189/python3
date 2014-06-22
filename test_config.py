
try:
    import configparser
except:
    import ConfigParser as configparser    
    
import sys

def testConfig(inputFile,outputFile):
    config = configparser.ConfigParser()
    config.read(inputFile);

    with open(outputFile, 'w') as configfile:
	    config.write(configfile)


def main():
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]
	print("InputFile is ",inputFileName)
	print("OutputFile is ",outputFileName)
	testConfig(inputFileName,outputFileName)


if(__name__ == "__main__"):
    main()


