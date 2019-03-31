import analysis

def main():
    analysis.genCsv()

    #genPlot()


    #x = ""
    #x=np.arange(0, 10000, 2000)
    #data1 = pd.read_csv("results.csv", sep=",")#, header = None, index_col="Algorithim", names= ["Algorithim", "100", "250", "500", "750", "1000", "1250", "2500", "3750", "5000", "6250", "7500", "8750", "10000"
    #a = data1.loc["Bubble"]
    #plt.plot(a ,x,"ro-", label = "Bubble")
    #b = data1.loc["Insertion"]
    #plt.plot(b,x,"bo-", label = "Insert")
    #c = data1.loc["Bucket"]
    #plt.plot(c, x,"yo-", label = "Bucket")
    #d = data1.loc["Merge"]
    #plt.plot(d,x,"go-", label = "Merge")
    #e = data1.loc["Quick"]
    #plt.plot(e,x,"mo-", label = "Quick")


if __name__ == "__main__":
    main()