def build_pte(is_vaild, frame_number,arrival_timestamp,last_access_timestamp,reference_count):
    pte={}
    pte["frame_number"]= frame_number
    pte["is_valid"]=is_vaild
    pte["arrival_timestamp"]=arrival_timestamp
    pte["late_access_timestamp"]=last_access_timestamp
    pte["reference_count"]=reference_count

def process_page_access_fifo(page_table, page_number, frame_pool, current_timestamp):
    if page_table[page_number]["is_valid"]==True:
        page_table[page_number]["late_access_timestamp"]=current_timestamp
        page_table[page_number]["reference_count"]=page_table[page_number]["reference_count"]+1
    elif len(frame_pool)>0:
        page_table[page_number]["frame_number"]=frame_pool.pop()
        page_table[page_number]["is_valid"]=True
        page_table[page_number]["arrival_timestamp"]=current_timestamp
        page_table[page_number]["late_access_timestamp"]=current_timestamp
        page_table[page_number]["reference_count"]=1
    else:
        old_page={}
        min_arrival_timestamp=999999
        for page in page_table:
            if page["is_valid"]== True and min_arrival_timestamp> page["arrival_timestamp"]:
                min_arrival_timestamp=page["arrival_timestamp"]
                old_page=page
        page_table[page_number]["is_valid"]=True
        page_table[page_number]["frame_number"]=old_page["frame_number"]
        page_table[page_number]["arrival_timestamp"]=current_timestamp
        page_table[page_number]["last_access_timestamp"]=current_timestamp
        page_table[page_number]["reference_count"]=1
        old_page["frame_number"]=-1
        old_page["is_valid"]=False
        old_page["arrival_timestamp"]=-1
        old_page["last_access_timestamp"]=-1
        old_page["reference_count"]=-1
        
        return page_table[page_number]["frame_number"]

def count_page_faults_fifo(page_table, page_references, frame_pool):
  pass

def process_page_access_lru(page_table, page_number, frame_pool, current_timestamp):
  pass
 
def count_page_faults_lru(page_table, page_references, frame_pool):
  pass

def process_page_access_lfu(page_table, page_number, frame_pool, current_timestamp):
  pass
 
def count_page_faults_lfu(page_table, page_references, frame_pool):
  pass
