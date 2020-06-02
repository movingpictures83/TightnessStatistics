class TightnessStatisticsPlugin:
   def input(self, filename):
      meanMatrix = open(filename+".meansFullMatrix.csv", 'r')
      stdMatrix = open(filename+".meStdevFullMatrix.csv", 'r')
      self.mean = []
      self.std = []
      meanMatrix.readline()
      for line in meanMatrix:
         internalList = []
         contents = line.strip().split(',')
         for value in contents[1:]:
            internalList.append(value)
         self.mean.append(internalList)
      stdMatrix.readline()
      for line in stdMatrix:
         internalList = []
         contents = line.strip().split(',')
         for value in contents[1:]:
            internalList.append(value)
         self.std.append(internalList)        

   def run(self):
      self.results = []
      for i in range(len(self.mean)):
         # Order: Mean within self, stddev within self, mean with others, stddev with others
         internalTuple = [None, None, None, None]
         if (self.mean[i][i] == ''):
            internalTuple[0] = 0
         else:
            internalTuple[0] = float(self.mean[i][i])
         if (self.std[i][i] == ''):  # No standard deviation if only 2 nodes in cluster
            internalTuple[1] = 0
         else:
            internalTuple[1] = float(self.std[i][i])
         sumMean = 0
         sumStd = 0
         for j in range(0, i):
            if (self.mean[j][i] != ''):
               sumMean += float(self.mean[j][i])
            if (self.std[j][i] != ''):
               sumStd += float(self.std[j][i])
            #sumStd += float(self.std[j][i])
         for j in range(i+1, len(self.mean)):
            if (self.mean[i][j] != ''):
               sumMean += float(self.mean[i][j])
            if (self.std[i][j] != ''):
               sumStd += float(self.std[i][j])
         sumMean /= (len(self.mean)-1)
         sumStd /= (len(self.mean)-1)
         internalTuple[2] = sumMean
         internalTuple[3] = sumStd
         self.results.append(internalTuple)

   def output(self, filename):
         stats = open(filename, 'w')
         stats.write("Cluster,Mean Inside,Std Dev Inside,Mean Outside,Std Dev Outside\n")
         sumMeanInner = 0
         sumStdInner = 0
         sumMeanOuter = 0
         sumStdOuter = 0
         for i in range(len(self.results)):
            stats.write(str(i+1)+","+str(self.results[i][0])+","+str(self.results[i][1])+","+str(self.results[i][2])+","+str(self.results[i][3])+"\n")
            sumMeanInner += self.results[i][0]
            sumStdInner += self.results[i][1]
            sumMeanOuter += self.results[i][2]
            sumStdOuter += self.results[i][3]
         stats.write("Averages,"+str(sumMeanInner/len(self.results))+","+str(sumStdInner/len(self.results))+","+str(sumMeanOuter/len(self.results))+","+str(sumStdOuter/len(self.results))+"\n")
