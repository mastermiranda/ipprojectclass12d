import streamlit as st
import pandas as pd
import tabulate
import numpy as np
import matplotlib.pyplot as plt
def visual():
    ch='y'
    while ch=='y' or ch=='Y':
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++Data Visualization+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(" ")
        print(" ")
        print(" 1. Histogram ")
        print(" 2. Line Chart ")
        print(" 3. Bar Chart ")
        print(" 4. GO BACK TO PREVIOUS MENU ")
        option1=input("Enter Your Choice: ")
        if option1=="1":
            histogram()
        elif option1=="2":
            linechart()
        elif option1=="3":
            bar_chart()
        elif option1=="4":
            chance1=input("Do You Really Want to Exit [y/n]?")
            if chance1=='y' or chance1=='Y':
                print("Exiting and Going Back to Main Menu...........")
                break
            else:
                print("Invalid Choice. TRY AGAIN........")
                continue
        else:
            ch=input("Do You Really Want to Exit [y/n]?")
def histogram():
    df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
    Co=df["Car"]
    Net=df["Net Sales (in Million $)"]
    print(tabulate.tabulate(df,headers=df.columns,tablefmt='double_outline'))
    plt.hist(Co,bins=len(Co),weights=Net,edgecolor='red')
    plt.title("Net Sales of Various Company During the Year 2020-24")
    plt.show()
def linechart():
    df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
    Co=df["Car"]
    Net=df["Net Sales (in Million $)"]
    print(tabulate.tabulate(df,headers=df.columns,tablefmt='double_outline'))
    plt.plot(Co)
    plt.title("Net Sales of Various Company During the Year 2020-24")
    plt.show()
def bar_chart():
    df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
    Co=df["Car"]
    Net=df["Net Sales (in Million $)"]
    print(tabulate.tabulate(df,headers=df.columns,tablefmt='double_outline'))
    index=np.arange(len(Co))
    plt.bar(Co,Net)
    plt.xlabel('Car',fontsize=4)
    plt.ylabel('Net Sales (in Million$)',fontsize=30)
    plt.xticks(index,Co,fontsize=8,rotation=30)
    plt.title("Net Sales of Various Company During the Year 2020-24")
    plt.show()
def manipulation():
    ch='y'
    while ch=='y' or ch=='Y':
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++Data Manipulation+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(" ")
        print(" ")
        print(" 1. Insert a Row ")
        print(" 2. Delete a Row ")
        print(" 3. Insert a Column ")
        print(" 4. Delete a Column ")
        print(" 5. GO BACK TO PREVIOUS MENU ")
        option=input("Enter Your Choice: ")
        if option=="1":
            print("DataFrame Before Inserting a New Row")
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(tabulate.tabulate(df,headers=df.columns,tablefmt='fancy_grid'))
            lst=[]
            columnname=df.columns
            for k in range(len(columnname)):
                print(columnname[k])
                rowvalue=input(":")
                lst.append(rowvalue)
                df.loc[len(df)]=lst
                df.to_csv(r'C:\Users\user\Documents\cars.csv')
                print("DataFrame After Inserting a New Row")
                df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
                print(df)
        elif option=="2":
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(tabulate.tabulate(df,headers=df.columns,tablefmt='fancy_grid'))
            i=input("Enter the S.NO to be Deleted: ")
            loc=df[(df.ID==i)].index
            df.drop(loc,inplace=True,axis=0)
            df.to_csv(r'C:\Users\user\Documents\cars.csv',index=False,encoding='utf-8')
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(df)
        elif option=="3":
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(tabulate.tabulate(df,headers=df.columns,tablefmt='fancy_grid'))
            column=input("Enter the Column Name: ")
            l=len(df)
            lst=[]
            for k in range(l):
                columnvalue=input("Enter the Value")
                lst.append(columnvalue)
            df[column]=pd.Series(lst)
            df.to_csv(r'C:\Users\user\Documents\cars.csv',encoding='utf-8',index=False,header=True)
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(tabulate(df,headers=df.columns,tablefmt='fancy_grid'))
        elif option=="4":
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(tabulate.tabulate(df,headers=df.columns,tablefmt='fancy_grid'))
            i=input("Enter the Column Name to be Deleted: ")
            df.drop(i,inplace=True,axis=1)
            df.to_csv(r'C:\Users\user\Documents\cars.csv',encoding='utf-8',index=False,header=True)
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(tabulate.tabulate(df,headers=df.columns,tablefmt='fancy_grid'))
        elif option=="5":
            chance1=input("Do you Really want to Exit [y/n]? ")
            if chance1=='y' or chance1=='Y':
                print("Exiting and Going Back to Main Menu..........")
                break
            else:
                print("Invalid Choices. TRY AGAIN.......")
                continue
        else:
            ch=input("Do you Really want to Exit [y/n]? ")
def read_csv_excel():
    df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
    ch='y'
    while ch=='y' or ch=='Y':
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++Read CSV/Excel Files+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(" ")
        print(" ")
        print(" 1. Display The First N Rows ")
        print(" 2. Dispay The Last N Rows ")
        print(" 3. Display The DataFrame After Sorting ")
        print(" 4. Display The Number of Cars Manufatured by Each Company ")
        print(" 5. GO BACK TO PREVIOUS MENU ")
        option=input("Enter Your Choice: ")
        if option=="1":
            n=int(input("Enter the Number of Rows to be Displayed from the Top: "))
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(df.head(n))
        elif option=="2":
            n=int(input("Enter the Number of Rows to be Displayed from the Bottom: "))
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            print(df.tail(n))
        elif option=="3":
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            column=input("Enter the Column on Which Sorting has to be Done []: ")
            print(df.sort_values(column))
        elif option=="4":
            df=pd.read_csv(r'C:\Users\user\Documents\cars.csv')
            col=input("Enter the ColumnName to by Grouped: ")
            print(df.groupby(col)['Car'].count())
        elif option=="5":
            chance1=input("Do you Really want to Exit [y/n]? ")
            if chance1=='y' or chance1=='Y':
                print("Exiting and Going Back to Main Menu........")
                break
        else:
            print("Invalid Choices. TRY AGAIN.....")
            continue
    else:
        ch=input("Do you Really Want to Exit [y/n]? ")
ans='y'
while ans=='y' or ans=='Y':
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++IP PROJECT 2024+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" ")
    print("By: Avin+Darsh+Eldho of XII-D")
    print(" ")
    print(" 1. Data Visualization ")
    print(" 2. Data Manipulation ")
    print(" 3. Read CSV/Excel Files ")
    print(" 4. Exit ")
    option=input("Enter Your Choice: ")
    if option=="1":
        visual()
    elif option=="2":
        manipulation()
    elif option=="3":
        read_csv_excel()
    elif option=="4":
        chance=input("Do you Really want to Exit [y/n]? ")
        if chance=='y' or chance=='Y':
            print()
            print("Thank You. Exiting Now.........")
            break
    else:
        print("Invalid Choices. TRY AGAIN......")
        continue
            
            
            
            
            
    
    
