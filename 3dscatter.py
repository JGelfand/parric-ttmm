if __name__ == "__main__":
    import matplotlib.pyplot as plot
    from mpl_toolkits.mplot3d import Axes3D
    size=5000
    files=[]
    for i in range(1,37):
        files.append(str(int(size/1000))+"k_"+str(i)+".txt")
    points=[]
    for f in files:
        f=open(f,"r")
        line=f.readline().split(" ")
        point=( float(line[3][1:-1]), float(line[4][:-1]), float(line[5][:-2]))
        point=(point[0]/size, point[1]/size, point[2]/size)
        points.append(point)
    
    fig=plot.figure()
    graph=fig.add_subplot(111, projection="3d")
    graph.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points] )
    graph.set_xlabel("ts1")
    graph.set_ylabel("ts2")
    graph.set_zlabel("ts3")
    graph.set_xlim3d(0,1)
    graph.set_ylim3d(0,1)
    graph.set_zlim3d(0,1)
    plot.show()
