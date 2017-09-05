import datetime
import os
import logging
import logging.handlers
from datetime import timedelta

def Epoch_file_rename(path):
                                 
            if os.path.exists(path) :
                        Count=0
                        for filename in os.listdir(path):
                                    if filename.startswith("auto-"):
                                                Count = Count+1
                                                a=os.path.join(filename)
                                                x=a.split('-')
                                                z=int(x[1])
                                                #print(z)
                                                y=datetime.datetime.fromtimestamp(z).strftime('%Y-%m-%dT%H-%M')
                                                os.rename(os.path.join(path, filename), os.path.join(path, filename.replace("auto-"+str(z),str(y))))
                                                logger.info('Rename:%s->%s',filename,filename.replace("auto-"+str(z),str(y)))
                                                                                    
                        if Count == 0:
                                    logger.info('File not found with Epoch time')
                                    
                        logger.info('Total number of file renamed : %d',Count)
            else:
                        logger.info('Folder does not exist:%s', path)
                        
            return;

print ('Start Date: YYYY-MN-DD')
tmp_date = input()
start = datetime.datetime.strptime(tmp_date, "%Y-%m-%d")
print ('End Date: YYYY-MM-DD')
tmp_date = input()
end = datetime.datetime.strptime(tmp_date, "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
            print (date.strftime("%Y-%m-%d"))
            C_date=date.strftime("%Y-%m-%d")
            
            #Change Path
            log_loc = 'C:app/log/'+ C_date + '.log'
            
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            
            handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE", log_loc))
            formatter = logging.Formatter('%(asctime)s : %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
           
            #Change Path
            path = 'C:app/'+C_date+'/monitor_local'
            
            logger.info('Rename file from current date folder: %s', path)
            Epoch_file_rename(path)
            handler.close()
            logger.removeHandler(handler)
