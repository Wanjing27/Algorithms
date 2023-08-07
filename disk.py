def build_rcb(request_id, arrival_timestamp,cylinder, address, process_id):
    request={}
    request["request_id"]=request_id
    request["arrival_timestamp"]=arrival_timestamp
    request["cylinder"]=cylinder
    request["address"]=address
    request["process_id"]=process_id

def is_null_rcb(request):
    if request["request_id"]==0 and request["arrival_timestamp"]and request["cylinder"]==0\
        and request["address"]==0 and request["process_id"]==0:
        return True
    else:
        return False


def handle_request_arrival_fcfs(request_queue, current_request, new_request, timestamp):
    if is_null_rcb(new_request)==True:
        return new_request
    else:
        request_queue.append(new_request)
        return current_request

def handle_request_completion_fcfs(request_queue):
    min_rcb={}
    if len(request_queue)==0:
        return build_rcb(0,0,0,0,0)
    else:
        min_at=9999999
        for request in request_queue:
            if request["arrival_timestamp"]<min_at:
                min_at=request["arrival_timestamp"]
                min_rcb=request
    request_queue.remove(min_rcb)
    return min_rcb
 
def handle_request_arrival_sstf(request_queue, current_request, new_request, timestamp):  
  pass

def handle_request_completion_sstf(request_queue, current_cylinder):
  pass
 
def handle_request_arrival_look(request_queue, current_request, new_request, timestamp):  
  pass

def handle_request_completion_look(request_queue, current_cylinder, direction):
  pass

