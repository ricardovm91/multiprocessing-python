import pandas as pd
import pickle
import multiprocessing
import datetime
import math
import logging
logging.getLogger().setLevel(logging.INFO)

def processChunk(dataChunk, fileId, agentId):
    startTime = datetime.datetime.now()
    logging.info(f'Started process: {fileId} at {startTime}')

    for i in dataChunk.itertuples():
        #Your very very long loop over dataChunk
        pass

    #Log when the job is done.
    endTime = datetime.datetime.now()
    logging.info(f'Finished process: {fileId} at {endTime}, took {endTime - startTime}.')

if __name__ == '__main__':
    Process = multiprocessing.Process
    
    totalSwarm = 3 #the number of machines executing the task
    agentId = 3 #the index of this machine

    fullDataSource = pd.read_csv(f'PATH-TO-YOUR-DATA-SOURCE')

    #Select the piece of dictionary for this agent
    divisionSize = math.ceil(len(fullDataSource['A-COLUMN']) / totalSwarm)
    
    lowerLimit = (agentId - 1) * divisionSize
    if(agentId != totalSwarm):
        #every agent
        upperLimit = lowerLimit + divisionSize - 1
    else:
        #last agent
        upperLimit = len(fullDataSource['A-COLUMN']) - 1

    agentDivision = fullDataSource.loc[lowerLimit:upperLimit]
    logging.info(f'lower: {lowerLimit}, upper: {upperLimit}')

    #Run resulting dictionary divided in every core.
    availableCores = multiprocessing.cpu_count()
    logging.info (f'cores: {availableCores}')

    divisionLength = len(agentDivision['A-COLUMN'])
    chunkSize = math.ceil(divisionLength / availableCores)

    processList = []
    for core in range(0,availableCores):
        # logging.info (core)
        factor = core + 1 #this works as an ID of the core.
        lowerBound = core * chunkSize + divisionSize * (agentId-1)

        if (core != (availableCores - 1)):
            #every core
            upperBound = lowerBound + chunkSize - 1 
        else:
            #last core
            upperBound = upperLimit
        
        logging.info(f'lower: {lowerBound}, upper: {upperBound}')
        dataChunk = agentDivision.loc[lowerBound:upperBound]

        #trigger new process
        newProcess = multiprocessing.Process(target=processChunk, args=(dataChunk, factor, agentId,))
        processList.append(newProcess)
        newProcess.start()
        
    for process in processList:
        process.join()
