def isnullpcb(process):
    if process["process_id"]==0 and\
        process["arrival_timestamp"]==0 and\
        process["total_bursttime"]==0 and\
        process["execution_starttime"]==0 and\
        process["execution_endtime"]==0 and\
        process["remaining_bursttime"]==0 and\
        process["process_priority"]==0:
        return True
    else:
        return False

def build_pcb(id, ts, tbt,st,et,rbt,pp):
  PCB = {
        "process_id": id,
        "arrival_timestamp" : ts,
        "total_bursttime": tbt,
        "execution_starttime" : st,
        "execution_endtime": et,
        "remaining_bursttime": rbt,
        "process_priority":pp
    }
  return PCB

def handle_process_arrival_pp(ready_queue, current_process, new_process, timestamp):
    if isnullpcb(current_process):
        new_process["execution_starttime"]=timestamp
        new_process["execution_endtime"]=timestamp+new_process["remaining_bursttime"]
        return new_process
    else:
        if new_process["process_priority"]>= current_process["process_priority"]:
            new_process["execution_starttime"]=0
            new_process["execution_endtime"]=0
            new_process["remaining_bursttime"]=new_process["total_bursttime"]
            ready_queue.append(new_process)
            return current_process
        else:
            new_process["execution_starttime"]=timestamp
            new_process["execution_endtime"]=timestamp+new_process["remaining_bursttime"]
            new_process["remaining_bursttime"]=new_process["total_bursttime"]
            current_process["remaining_bursttime"]=current_process["total_bursttime"]-timestamp + \
                current_process["execution_starttime"]
            current_process["execution_endtime"]=0
            ready_queue.append(current_process)
            return new_process

def handle_process_completion_pp(ready_queue, timestamp):
  if len(ready_queue)==0:
    return build_pcb(0,0,0,0,0,0,0)
  else:
    high_priority=9999
    high_pcb={}
    for this_pcb in ready_queue:
      if this_pcb ["process_priority"] < high_priority:
        high_priority=this_pcb["process_priority"]
        high_pcb=this_pcb
    ready_queue.remove(high_pcb)
    high_pcb["execution_starttime"]=timestamp
    high_pcb["execution_endtime"]=timestamp + high_pcb["remaining_bursttime"]
    return  high_pcb

 
def handle_process_arrival_srtp(ready_queue, current_process, new_process, timestamp):
  if isnullpcb(current_process):
        new_process["execution_starttime"]=timestamp
        new_process["execution_endtime"]=timestamp+new_process["remaining_bursttime"]
        return new_process
  else:
        if new_process["total_bursttime"]>= current_process["remaining_bursttime"]:
            new_process["execution_starttime"]=0
            new_process["execution_endtime"]=0
            new_process["remaining_bursttime"]=new_process["total_bursttime"]
            ready_queue.append(new_process)
            return current_process
        else:
            new_process["execution_starttime"]=timestamp
            new_process["execution_endtime"]=timestamp+new_process["remaining_bursttime"]
            new_process["remaining_bursttime"]=new_process["total_bursttime"]
            current_process["remaining_bursttime"]=current_process["total_bursttime"]-timestamp + \
                current_process["execution_starttime"]
            current_process["execution_endtime"]=0
            current_process["execution_starttime"]=0
            ready_queue.append(current_process)
            return new_process
 
def handle_process_completion_srtp(ready_queue, timestamp):
  if len(ready_queue)==0:
    return build_pcb(0,0,0,0,0,0,0)
  else:
    min_burst=9999999
    min_pcb={}
    for this_pcb in ready_queue:
      if this_pcb ["remaining_bursttime"] < min_burst:
        min_burst=this_pcb["remaining_bursttime"]
        min_pcb=this_pcb
    ready_queue.remove(min_pcb)
    min_pcb["execution_starttime"]=timestamp
    min_pcb["execution_endtime"]=timestamp + min_pcb["remaining_bursttime"]
    return  min_pcb
  

def handle_process_arrival_rr(ready_queue, current_process, new_process, timestamp, time_quantum):
  if isnullpcb(current_process):
        new_process["execution_starttime"]=timestamp
        if time_quantum>new_process["total_bursttime"]:
          new_process["execution_endtime"]=timestamp+new_process["total_bursttime"]
        else:
          new_process["execution_endtime"]=timestamp+time_quantum
        return new_process
  else:
    new_process["execution_starttime"]=0
    new_process["execution_endtime"]=0
    new_process["remaining_bursttime"]=new_process["total_bursttime"]
    ready_queue.append(new_process)
    return current_process
 
def handle_process_completion_rr(ready_queue, timestamp, time_quantum):
  if len(ready_queue)==0:
    return build_pcb(0,0,0,0,0,0,0)
  else:
    early_arrival=9999
    early_pcb={}
    for this_pcb in ready_queue:
      if this_pcb ["arrival_timestamp"] < early_arrival:
        early_arrival=this_pcb["arrival_timestamp"]
        early_pcb=this_pcb
    ready_queue.remove(early_pcb)
    early_pcb["execution_starttime"]=timestamp
    if time_quantum > early_pcb["remaining_bursttime"]:
          early_pcb["execution_endtime"]=timestamp + early_pcb["remaining_bursttime"]
    else:
      early_pcb["execution_endtime"]=timestamp+time_quantum
      
    return  early_pcb
