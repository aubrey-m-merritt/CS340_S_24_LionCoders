import pandas as pd
import matplotlib as plt
import seaborn
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='Root\scientificCategory.log', encoding='utf-8', level=logging.DEBUG)

class scientificCategory():
    def __init__(self, config):
        super(config)
        self.category = []
        self.taxonomicGroup = []
        self.taxonomicSubgroup = [] = []
        self.scientificName = []
        self.commonName = []
        self.config = ()
        df = pd.read_csv('YatesBiodiversity.csv', index_col='county') 
        booleanIndex = pd.DataFrame(df, index = [True, False, True, False, True, False, True, False])
    #
    try:
        logger.info('Reading csv file and storing into a dataframe...')
        dataframeCSV = pd.read_csv('Root\Input\YatesBiodiversity.csv',sep=',', index_col=0)
        print(dataframeCSV)
        logger.info('Reading csv file and storing into a dataframe successful!')
    except:
        print('Not loading csv file.')
        logger.debug('Not loading csv file.')
    #
    try:
        logger.info('Reading pickle file and storing into a dataframe...')
        dafaframePickle = pd.read_pickle('Root\Input\AlbanyBiodiversity.pkl',sep=',', index_col=0)
        dataPickle = pd.DataFrame(dafaframePickle)
        logger.info('Reading pickle file and storing into a dataframe successful!')
    except:
        print('Not loading pickle file.')
        logger.debug('Not loading pickle file.')
    #
    
    def violinPlot(data):
        try:
            logger.info('Displaying data as violin plot...')
            seaborn.set(style='whitegrid')
            dataset = seaborn.load_dataset(data)
            #seaborn.violinplot(x="an x-axis value" , y = "an y-axis value" data=dataset) //something is wrong with this line
        #
        except:
            print('Violin plot not working.')
            logger.debug('Violin plot not working.')
        #
    #
 
    def whiskerBoxPlot(dataset):
        try:
            logger.info('Displaying data as whisker-box plot...')
            plt.boxplot(dataset)
            plt.show()
        #
        except:
            print('Whisker-box plot not working.')
            logger.debug('Whisker-box plot not working.')
        #
	#
 
    def scatterPlot(x,y):
        try:
            logger.info('Displaying data as scatter plot...')
            plt.scatter(x,y)
            plt.show()
        #
        except:
            print('Scatter plot not working.')
            logger.debug('Scatter plot not working.')
        #
    #
    
    #calculations section 
    
    def calculateJointCounts(self,holder):
        try:
            logger.info('Calculating the joint counts...')
            ##will calculate joint counts and return result
            return holder
        #
        except:
            print('Not calculating the joint counts.')
            logger.debug('Not calculating the joint counts.')
        #
	#
    
    def calculateJointCounts(self, holder):
        try:
            logger.info('Calculating the joint counts...')
            ##will calculate joint counts and return result
            return holder 
        #
        except:
            print('Not calculating the joint counts.')
            logger.debug('Not calculating the joint counts.')
        #
    #
    
    def calculateJointProbabilities(self, holder):
        try:
            logger.info('Calculating the joint probabilities...')
            ##will calculate joint probabilities and return result
            return holder
        #
        except:
            print('Not calculating the joint probabilities.')
            logger.debug('Not calculating the joint probabilities.')
        #
	#
    
    def calculateConditionalProbabilities(self, holder):
        try:
            logger.info('Calculating the conditional probabilities...')
            ##will calculate conditional probabilities and return result
            return holder
        #
        except:
            print('Not calculating the conditional probabilities.')
            logger.debug('Not calculating the conditional probabilities.')
        #
    #
    
    def calculateMean(self, holder):
        try:
            logger.info('Calculating the mean...')
            ##will calculate mean and return result
            return holder
        #
        except:
            print('Not calculating the mean.')
            logger.debug('Not calculating the mean.')
        #
    #
    
    def calculateMedian(self, holder):
        try:
            logger.info('Calculating the median...')
            ##will calculate median and return result
            return holder
        #
        except:
            print('Not calculating the median.')
            logger.debug('Not calculating the median.')
        #
    #
    
    def calculateSTD(self, holder):
        try:
            logger.info('Calculating the standard deviation...')
            ##will calculate STD and return result
            return holder 
        #
        except:
            print('Not calculating the standard deviation.')
            logger.debug('Not calculating the standard deviation.')
        #
    #

    #categorial attribute section

    def obtainSpecificValue(self, askedValue):
        try:
            logger.info('Obtaining a specific value...')
            ##will return the asked value
            return askedValue
        #
        except:
            print('Not obtaining a specific value.')
            logger.debug('Not obtaining a specific value.')
        #
	#
    
    def generatePermutationsOfNames(self, holder):
        try:
            logger.info('Generating ordered arrangement of names...')
            ##will return an ordered arrangement of names
            return holder
        #
        except:
            print('Not generating ordered arrangement of names.')
            logger.debug('Not generating ordered arrangement of names.')
        #
    #

    def generateCombinationsOfNames(self, holder):
        try:
            logger.info('Generating unordered arrangement of names...')
            ##will return a unordered arrangement of names
            return holder
        #
        except:
            print('Not generating unordered arrangement of names.')
            logger.debug('Not generating unordered arrangement of names.')
        #
	#
    
    def findOrganisim(self, userInput):
        try:
            logger.info('Querying search function...')

            #this function will return an organisim that user wants or will return 'NOT FOUND' if not in dataset
            df = pd.DataFrame(dict, index = [True, False, True, False])

            return userInput 
        #
        except:
            print('Not querying search function.')
            logger.debug('Not querying search function.')
        #
	#
#