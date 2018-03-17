import os
import matplotlib.pyplot as plt

def load_input(filename):
    assert os.path.isfile(filename)
    start=True
    with open(filename) as f:
        h_cpus, h_mems, _ = f.readline().strip().split()
        h_cpus = int(h_cpus)
        h_mems = 1024*int(h_mems)

        v_cpus = dict()
        v_mems = dict()
        v_flavors = set()
        while(True):
            line = f.readline().rstrip()
            if line.isdigit():
                for i in range(int(line)):
                    flavor, cpu, mem = f.readline().rstrip().split()
                    v_flavors.add(flavor)
                    v_cpus[flavor]=int(cpu)
                    v_mems[flavor]=int(mem)*1024
            elif line =='CPU':
                cpu_flag = True
            elif line=='MEM':
                cpu_flag=False
            elif len(line.strip().split())==2:
                if start==True:
                    startTime = line
                    start=False
                else:
                    endTime = line
            elif start==False:
                break
    return h_cpus, h_mems, v_flavors, v_cpus, v_mems, cpu_flag, startTime, endTime


def load_trainfile(filename, v_flavors):
    assert os.path.isfile(filename)
    flavors_data = {}
    for flavor in v_flavors:
        flavors_data[flavor]={}
    with open(filename) as f:
        pre_time = 0
        for line in f:
            flavor, time = line.rstrip().split()[1:3]
            if time!=pre_time:
                pre_time=time
                for flavor in v_flavors:
                    flavors_data[flavor][time]=0
            if flavor in v_flavors:
                flavors_data[flavor][time]+=1

    return flavors_data


if __name__=='__main__':
    h_cpus, h_mems, v_flavors , v_cpus, v_mems, cpu_flag, startTime, endTime = load_input("data/input_5flavors_cpu_7days.txt")
    print(h_cpus, h_mems, v_flavors, v_cpus, v_mems, cpu_flag, startTime, endTime)

    trainData = load_trainfile('data/TrainData_2015.1.1_2015.2.19.txt', v_flavors)
    print(len(trainData))
    print(trainData.keys())

    for flavor in v_flavors:
        adict = trainData[flavor].items()
        a=sorted(adict)
        data=[]
        times=[]
        for i, (time,cnt) in enumerate(a):
            data.append((i,cnt))
            times.append(time)
        x,y=zip(*data)
        #plt.xticks(x, times)
        plt.plot(x,y,label=flavor)
        plt.legend()
    plt.show()




