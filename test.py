# novel hybrid scheduling algorithm

import numpy as np
import statistics

atime=[0,0,1,2,3,4]
init_btime=[12,8,23,10,30,15]
btime=[12,8,23,10,30,15]

# atime=[0,1,2,3,4,4,4,5,3,6]
# init_btime=[49,98,143,187,244,252,199,67,83,75]
# btime=[49,98,143,187,244,252,199,67,83,75]

# atime=[0,1,2,3,4,5,3,3,4,6]
# init_btime=[251,177,152,299,47,84,244,124,55,180]
# btime=[251,177,152,299,47,84,244,124,55,180]

# atime=[0,1,2,3,4,5,6,7,4,8]
# init_btime=[33,201,98,116,11,100,33,78,18,64]
# btime=[33,201,98,116,11,100,33,78,18,64]

n=len(atime)

ctime=[0]*n
tatime=[0]*n	# ct-at
wtime=[0]*n		#tat-bt
rtime=[0]*n
quantum=[0]*n
bvar=0
qvar=0

q1=[]	# 1 3 0
q2=[]	# 5 2 4
idx_tq1=[]
idx_tq2=[]
val_tq1=[]
val_tq2=[]

completed_tasks=[0]*n
time=0
sqrval=0
round_num=1

rtimeflag=[0]*n

med=statistics.median(btime)

for idx,ele in enumerate(btime):
	if(ele>med):
		idx_tq2.append(idx)
		val_tq2.append(ele)
	else:
		idx_tq1.append(idx)
		val_tq1.append(ele)


tmp_q1=[x for _,x in sorted(zip(val_tq1,idx_tq1))]
tmp_q2=[x for _,x in sorted(zip(val_tq2,idx_tq2))]

q1=tmp_q1
q2=tmp_q2

print("q1 "+str(q1))
print("q2 "+str(q2)+"\n")
qbar=med

print("INITIAL ROUND PARAMETERS")
print("btime "+str(btime))
print("qbar "+str(qbar))
print("quantum "+str(quantum)+"\n")

while(all(completed_tasks)==0):

	## RECALCULATE TIME QUANTUM
	for idx,val in enumerate(btime):
		if(completed_tasks[idx]==1):
			quantum[idx]=0
			continue
		else:
			if(idx in q1):
				sqr_val=(float)(val+quantum[idx])**2
			if(idx in q2):
				sqr_val=(float)(val-quantum[idx])**2

		quantum[idx]=qbar+(qbar/sqr_val)


	print("ROUND "+str(round_num)+" PARAMETERS")
	print("btime "+str(btime))
	print("qbar "+str(qbar))
	print("quantum "+str(quantum)+"\n")
	round_num=round_num+1

	tcnt=completed_tasks.count(0)
	print("number of tasks remaining "+str(tcnt)+"\n")
	
	icnt=0
	tasks_queue=[]
	completed_tasks_round=[0]*n
	tq1=q1[::-1]
	tq2=q2[::-1]

	## POPULATE TASKS QUEUE
	while(icnt<tcnt):

		cnt=0
		while(len(tq1)):
			cnt=cnt+1
			icnt=icnt+1
			val=tq1.pop()
			tasks_queue.append(val)

			if((cnt==2)):
				break
			

		cnt=0
		while(len(tq2)):
			cnt=cnt+1
			icnt=icnt+1
			val=tq2.pop()
			tasks_queue.append(val)

			if((cnt==1)):
				break		


	print("tasks queue is "+str(tasks_queue))

	## ASSIGN RESOURCES TO TASKS
	for idx,val in enumerate(tasks_queue):
		# to find responsetime
		if(rtimeflag[val]==0):
			rtimeflag[val]=1
			if(time>=atime[val]):
				rtime[val]=time-atime[val]
			else:
				rtime[val]=0

		if(btime[val]<=quantum[val]):
			print("btime before "+str(btime))
			completed_tasks[val]=1
			qbar=qbar-(float)(qbar/init_btime[val])
			time=time+btime[val]
			
			ctime[val]=time
			tatime[val]=time-atime[val]
			wtime[val]=(time-atime[val])-btime[val]
			
			btime[val]=0
			print("task number "+str(val)+" completed at time "+str(ctime[val])+"; qbar= "+str(qbar))
			print("btime now "+str(btime)+"\n")

		if(btime[val]>quantum[val]):
			print("btime before "+str(btime))
			time=time+quantum[val]
			btime[val]=btime[val]-quantum[val]
			print("task number "+str(val)+" execution finished at time "+str(time))
			print("btime now "+str(btime)+"\n")


	print("completed tasks "+str(completed_tasks)+"\n\n")
	for idx,val in enumerate(completed_tasks):
		if(val==1):
			if(idx in q1):
				q1.remove(idx)
			if(idx in q2):
				q2.remove(idx)
		else:
			continue


print("STATISTICS")
avg_wtime=sum(wtime)/n
avg_tatime=sum(tatime)/n
avg_rtime=sum(rtime)/n
print("average wtime= "+str(avg_wtime))
print("average tatime= "+str(avg_tatime))
print("average rtime= "+str(avg_rtime))
