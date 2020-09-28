import pandas as pd
import re


class cleaner(object):
    productData_df = pd.read_csv('productData.csv', delimiter='|', names=['product_Id', 'max_price', 'price_was', 'price_selling', 'price_savings_totalPercentage', 'price_typeIndicator', 'availabilityQuantity', 'storeNumber', 'urls', 'title'])
    
    myProductIds=[]

    with open('prodid.txt') as f:
        for product in f:
            product=product.replace("\n","")
            product= product.split('/')[5]
            myProductIds.append(product)

        

    for product in myProductIds:
        for i in range(len(productData_df.index)):
            print('Checking For Max Prices for product '+ product)
            if productData_df['product_Id'][i].astype(int) == int(product):
                highest_value = productData_df['price_selling'][i].astype(float)
                if (highest_value < productData_df['price_selling'][i].astype(float)):
                    highest_value = productData_df['price_selling'][i].astype(float)
                productData_df.loc[productData_df['product_Id'] == int(product), 'max_price'] = highest_value

    for product in myProductIds:
        print('Calculating Savings For ' + product)
        for i in range(len(productData_df.index)):
            maxPrice = productData_df['max_price'][i].astype(float)
            sellingPrice = productData_df['price_selling'][i].astype(float)
            productData_df.loc[productData_df['product_Id'] == int(product), 'price_savings_total'] = maxPrice - sellingPrice

    for product in myProductIds:
        print('Calculating Savings Percentage ' + product)
        for i in range(len(productData_df.index)):
            maxPrice = productData_df['max_price'][i].astype(float)
            sellingPrice = productData_df['price_selling'][i].astype(float)
            productData_df.loc[productData_df['product_Id'] == int(product), 'price_savings_totalPercentage'] = 1 - (maxPrice//sellingPrice)
            
    
    productData_df.to_csv('cleanData.csv', index=False)

cleaner()
            #print(highest_value)
        #highest_value = productData_df['price_selling'][0].astype(float)



        

