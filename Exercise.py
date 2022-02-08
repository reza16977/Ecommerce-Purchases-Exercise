import pandas as pd
ecom=pd.read_csv('Ecommerce Purchases')
ecom.head()    #checking the head of of DataFrame
ecom.info()    #checking the count of rows and columns and ...
ecom['Purchase Price'].mean()    #average of Purchase Price
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()      #min and max of purchase price
ecom[ecom['Language']=='en'].count()   #how many customers select english as there language on website
ecom[ecom['Job']=='Lawyer'].info()      #how many customer 's job is lawyer .
ecom['AM or PM'].value_counts()         #count of people who shopped on Am or Pm 
ecom['Job'].value_counts().head(5)     # 5commen job title
ecom[ecom['Lot']=='90 WT']['Purchase Price'] # Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **
ecom[ecom['Credit Cart']==926535242672853]['Email'] #What is the email of the person with the following Credit Card Number: 4926535242672853
ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()   #How many people have American Express as their Credit Card Provider *and made a purchase above $95 ?
sum(ecom['CC Exp Date'].apply(lambda x:x[3:])=='25')    #Hard: How many people have a credit card that expires in 2025?
ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)  #What are the top 5 most popular email providers/hosts
