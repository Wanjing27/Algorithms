def build_memblock(start_address, end_address,segment_size, process_id):
    newblock={}
    newblock["start_address"]=start_address
    newblock["end_address"]=end_address
    newblock["segment_size"]=segment_size
    newblock["process_id"]=process_id
    return newblock

def best_fit_allocate(request_size, memory_map,process_id):
    dif=99999
    best_block=build_memblock(0,0,0,0)
    for block in memory_map:
        if block["segment_size"]-request_size<dif and block["segment_size"]>=request_size \
            and block["process_id"]==0:
            dif=block["segment_size"]-request_size
            best_block=block
    if dif>0 and dif!=99999:
        memory_map.append(build_memblock(\
            best_block["start_address"]+request_size,\
            best_block["end_address"],\
            best_block["segment_size"]-request_size,\
            0))
        best_block["end_address"]=best_block["start_address"]+request_size-1
        best_block["segment_size"]=request_size
        best_block["process_id"]= process_id
    elif dif==0:
        best_block["process_id"]=process_id
    return best_block

def first_fit_allocate(request_size, memory_map,process_id):
    dif=99999
    first_block=build_memblock(0,0,0,0)
    for block in memory_map:
        if block["start_address"]-request_size<dif and block["segment_size"]>=request_size \
            and block["process_id"]==0:
            dif=block["segment_size"]-request_size
            first_block=block
    if dif>0 and dif!=99999:
        memory_map.append(build_memblock(\
            first_block["start_address"]+request_size,\
            first_block["end_address"],\
            first_block["segment_size"]-request_size,\
            0))
        first_block["end_address"]=first_block["start_address"]+request_size-1
        first_block["segment_size"]=request_size
        first_block["process_id"]= process_id
    elif dif==0:
        first_block["process_id"]=process_id
    return first_block

def worst_fit_allocate(request_size, memory_map,process_id):
    dif=-99
    worst_block=build_memblock(0,0,0,0)
    for block in memory_map:
        if block["segment_size"]-request_size>dif and block["segment_size"]>=request_size \
            and block["process_id"]==0:
            dif=block["segment_size"]-request_size
            worst_block=block
    if dif>0:
        memory_map.append(build_memblock(\
            worst_block["start_address"]+request_size,\
            worst_block["end_address"],\
            worst_block["segment_size"]-request_size,\
            0))
        worst_block["end_address"]=worst_block["start_address"]+request_size-1
        worst_block["segment_size"]=request_size
        worst_block["process_id"]= process_id
    elif dif==0:
        worst_block["process_id"]=process_id
    return worst_block
    
def next_fit_allocate(request_size, memory_map, process_id, last_address):
    dif=99999
    next_block=build_memblock(0,0,0,0)
    for block in memory_map:
        if block["start_address"]-request_size<dif and block["start_address"]>=last_address and block["segment_size"]>=request_size \
            and block["process_id"]==0:
            dif=block["segment_size"]-request_size
            next_block=block
    if dif>0 and dif!=99999:
        memory_map.append(build_memblock(\
            next_block["start_address"]+request_size,\
            next_block["end_address"],\
            next_block["segment_size"]-request_size,\
            0))
        next_block["end_address"]=next_block["start_address"]+request_size-1
        next_block["segment_size"]=request_size
        next_block["process_id"]= process_id
    elif dif==0:
        next_block["process_id"]=process_id
    return next_block

def release_memory(freed_block, memory_map):
    before_block=build_memblock(0,0,0,-1)
    after_block=build_memblock(0,0,0,-1)
    found_block={}
    found =False
    for block in memory_map:
        if found==False and block["start_address"] != freed_block["start_address"]:
          before_block=block
        elif block["start_address"]== freed_block["start_address"]:
            found_block=block
            found=True
        elif after_block["process_id"]==-1:
            after_block=block
    if before_block["process_id"]!=0 and after_block["process_id"]!=0:
            found_block["process_id"]=0
    elif before_block["process_id"]==0 and after_block["process_id"]!=0:
        before_block["end_address"]=found_block["end_address"]
        before_block["segment_size"]=before_block["end_address"]-before_block["start_address"]+1
        memory_map.remove(found_block)
    elif before_block["process_id"]!=0 and after_block["process_id"]==0:
        after_block["start_address"]=found_block["start_address"]
        after_block["segment_size"]=after_block["end_address"]-after_block["start_address"]+1
        memory_map.remove(found_block)
    else:
        before_block["end_address"]=after_block["end_address"]
        before_block["segment_size"]=before_block["end_address"]-before_block["start_address"]+1
        memory_map.remove(found_block)
        memory_map.remove(after_block)