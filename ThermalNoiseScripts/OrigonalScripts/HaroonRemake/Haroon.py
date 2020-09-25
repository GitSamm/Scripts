import numpy as np
import matplotlib as mb
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_pdf import PdfPages

time=[]

# get data for time per cycle and save it in a dictionary 'd'

cycle_count=0
d={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
n=0
node=1
with open('cycles.txt') as t:
    for line in t:
       
        time = float(line.split(' ',1)[1].strip('\n'))
        current_node = float(line.split(' ',1)[0].strip('\n'))


        if current_node > node:


            cycle_count=0
            node = current_node
        
       
        d[cycle_count].append(time)
        
        cycle_count=cycle_count+1
        

for cycle,time in d.iteritems():
    
    
    
    if len(d[cycle]) < 24:
        number_zeros=24-len(d[cycle])
        z=[0]*number_zeros
 #       print len(z)
        x=[]
#        print len(d[cycle])
        print cycle
        x = z + d[cycle]
        d[cycle] = x
        
print d[12]

# get data for degrees of freedom and save it in dictionary 'e'
cycle_count=0
node=1
e={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}
with open('dof.txt') as f:
    for line in f:
        dof=float(line.split(' ',1)[1].strip('\n'))
 
        current_node = float(line.split(' ',1)[0].strip('\n'))

        if current_node > node:
            cycle_count=0
            node = current_node

        e[cycle_count].append(dof)

        cycle_count=cycle_count+1
        

#print e[8]



for cycle,dof in e.iteritems():



    if len(e[cycle]) < 24:
        number_zeros=24-len(e[cycle])
        z=[0]*number_zeros
   #     print len(z)
        x=[]
  #      print len(e[cycle])
        x = z + e[cycle]
        print cycle
        e[cycle] = x

print e[10]






xval=np.array(range(1,25),dtype=np.float32)

#plots cycles 0-8
c0_t=[]
c0_t=np.array(d[0],dtype=np.float32)
c1_t=np.array(d[1],dtype=np.float32)
c2_t=np.array(d[2],dtype=np.float32)
c3_t=np.array(d[3],dtype=np.float32)
c4_t=np.array(d[4],dtype=np.float32)
c5_t=np.array(d[5],dtype=np.float32)
c6_t=np.array(d[6],dtype=np.float32)
c7_t=np.array(d[7],dtype=np.float32)
c8_t=np.array(d[8],dtype=np.float32)
c9_t=np.array(d[9],dtype=np.float32)
c10_t=np.array(d[10],dtype=np.float32)
c11_t=np.array(d[11],dtype=np.float32)
c12_t=np.array(d[12],dtype=np.float32)


c9_t[c9_t == 0.0] = np.nan
c10_t[c10_t == 0.0] = np.nan
c11_t[c11_t == 0.0] = np.nan
c12_t[c12_t == 0.0] = np.nan


print c0_t



fig=plt.gcf()
ax=plt.gca()


gridwidth=0.5
gridcolor=(0.8,0.8,0.8)

ax.plot(xval,c0_t, label='$N=0$', color='b')
ax.plot(xval,c1_t, label='$N=1$', color='g')
ax.plot(xval,c2_t, label='$N=2$', color='r')
ax.plot(xval,c3_t, label='$N=3$', color='c')
ax.plot(xval,c4_t, label='$N=4$', color='m')
ax.plot(xval,c5_t, label='$N=5$', color='y')
ax.plot(xval,c6_t, label='$N=6$', color='k')
ax.plot(xval,c7_t, label='$N=7$', color='r', linestyle='dashed')
ax.plot(xval,c8_t, label='$N=8$', color='g', linestyle='dashed')
ax.plot(xval,c9_t, label='$N=9$', color='r', linestyle='dashed')
ax.plot(xval,c10_t, label='$N=10$', color='c', linestyle='dashed')
ax.plot(xval,c11_t, label='$N=11$', color='m', linestyle='dashed')
ax.plot(xval,c12_t, label='$N=12$', color='y', linestyle='dashed')

ax.set_xlim([1,24])
ax.set_yscale('linear')

ax.xaxis.set_major_locator(ticker.MultipleLocator(4))

ax.tick_params(axis='x', labelsize=24, pad=12, length=10)
ax.tick_params(which='minor', length=5)
ax.tick_params(axis='y', labelsize=24, length=10)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.set_xticks(xval, minor=True)
ax.set_xlabel('Cores', fontsize=32)
ax.set_ylabel('Time (s)', fontsize=32)
lgd = ax.legend(bbox_to_anchor=(1.0,.5), loc='center left', fontsize=16)

ax.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)

fig.tight_layout()


pdf = PdfPages('allcycles.pdf')
pdf.savefig( bbox_extra_artists=(lgd,), bbox_inches='tight')
pdf.close()

ax.cla()




#plots cycle 8 time

fig2=plt.gcf()
ax2=plt.gca()


gridwidth=0.5
gridcolor=(0.8,0.8,0.8)

ax2.plot(xval,c8_t, label='res 8', color='b')
ax2.set_xlim([1,24])
ax2.set_yscale('log')

ax2.xaxis.set_major_locator(ticker.MultipleLocator(4))

ax2.tick_params(axis='x', labelsize=10, pad=12, length=10)
ax2.tick_params(which='minor', length=5)
ax2.tick_params(axis='y', labelsize=10, pad=12, length=10)



ax2.set_xticks(xval, minor=True)
ax2.set_xlabel('Cores', fontsize=34)
ax2.set_ylabel('Time (s) ', fontsize=34)
ax2.legend(loc='upper right', fontsize=8)

ax2.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)

fig2.tight_layout()


pdf = PdfPages('cycle8_time.pdf')
#pdf.savefig()
pdf.close()


ax2.cla()
# plots cycle 8 degree of freedom

c8_dof=np.array(e[8],dtype=np.float32)
fig3=plt.gcf()
ax3=plt.gca()


gridwidth=0.5
gridcolor=(0.8,0.8,0.8)


ax3.plot(c8_dof,c8_t, label='res 8', color='r', marker='o', linestyle = 'None')

#ax.set_yscale('log')

#ax.xaxis.set_major_locator(ticker.MultipleLocator(4))

ax3.tick_params(axis='x', labelsize=10, pad=12, length=10)
ax3.tick_params(which='minor', length=5)
ax3.tick_params(axis='y', labelsize=10, pad=12, length=10)



#ax3.set_xticks(xval, minor=True)
ax3.set_ylabel('Time (s)', fontsize=34)
ax3.set_xlabel('Degrees of freedom ', fontsize=34)
ax3.legend(loc='upper right', fontsize=8)

ax3.grid(b=True, which='major', color=gridcolor, linestyle='solid', linewidth=gridwidth)

fig3.tight_layout()


pdf = PdfPages('cycle8_dof.pdf')
#pdf.savefig()
pdf.close()

ax3.cla()



n1_time=[]
n4_time=[]
n8_time=[]
n16_time=[]
n24_t=[]

