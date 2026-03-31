# Can you help Tunisian company STEG detect fraud?
The Tunisian Company of Electricity and Gas (STEG) is a public and a non-administrative company, it is responsible for delivering electricity and gas across Tunisia. The company suffered tremendous losses in the order of 200 million Tunisian Dinars due to fraudulent manipulations of meters by consumers.

Using the client’s billing history, the aim of the challenge is to detect and recognize clients involved in fraudulent activities.

The solution will enhance the company’s revenues and reduce the losses caused by such fraudulent activities.

About STEG (https://www.steg.com.tn/en/institutionnel/mission.html)

The Tunisian Company of Electricity and Gas (STEG) is a public and a non-administrative company. It is responsible for delivering electricity and gas across Tunisia. 

Client:

    Client_id: Unique id for client
    District: District where the client is
    Client_catg: Category client belongs to
    Region: Area where the client is
    Creation_date: Date client joined
    Target: fraud:1 , not fraud: 0

Invoice data

    Client_id: Unique id for the client
    Invoice_date: Date of the invoice
    Tarif_type: Type of tax
    Counter_number:
    Counter_statue: takes up to 5 values such as working fine, not working, on hold statue, ect
    Counter_code:
    Reading_remarque: notes that the STEG agent takes during his visit to the client (e.g: If the counter shows something wrong, the agent gives a bad score)
    Counter_coefficient: An additional coefficient to be added when standard consumption is exceeded
    Consommation_level_1: Consumption_level_1
    Consommation_level_2: Consumption_level_2
    Consommation_level_3: Consumption_level_3
    Consommation_level_4: Consumption_level_4
    Old_index: Old index
    New_index: New index
    Months_number: Month number
    Counter_type: Type of counter [Gas, Electrik]

Evaluation

The metric used for this challenge is Area Under the Curve.

Then the submission file should be as follows:

|client_id       |target|
|----------------|------|
|test_Client_0   |0.986|
|test_Client_1   |0.011|
|test_Client_10  |0.734|

# Steg: payment Method
The Bill

The bill is bimonthly. It is established further to a four-month meter reading in urban area and a six-month meter reading in rural area or further to an estimation based on your last 12 months consumption (intermediary bill).
Intermediary bill

It involves the estimated amount of your consumption calculated according to your previous consumption added to due fees, the estimated amount of RTT (Tunisian Radio and Television) contribution and the different payment facilities (connection or others).
Regarding new subscribers, no advance payment would be invoiced to them as long as their meter has not been read.
The net to be paid of this bill will be deduced on the bill involving the actual reading of your consumption.
How to pay ?
Monthly payment

It enables you to spread your yearly electricity consumption over twelve month bills deducted directly from your bank or postal account.Monthly amounts are calculated on the basis of your past year's consumption which is brought up to date every year.

How to do ?

You send or deposit at your district a deduction authorization on your postal or bank account.
Authorized Payment 

The amount of each of your bills is automatically deducted from the current postal or bank account you have indicated.

How to do ?

You send your district your approval of payment. STEG sends you your consumption bill by mail for information. If you have no remarks or objections regarding the amount of your power consumption,  the due amount will be automatically withdrawed from your current account, 15 days after receiving your invoice.
Payment at the Post Desks

You can pay your bill at any  post-desk.
Payment at SONEDE windows

You have the possibility to pay your bill in almost all SONEDE pay-desk.
Online Payment 

Our online payment services allow you to pay your bill via your personal computer.

Reducing your bill

    Do not forget to turn off the lights when not needed.
    Remember that daylight is costless, so profit from it .
    Make a good choice and know how to adapt your lighting to your needs; you will profit from comfort and save money.
    If you have refrigerating devices, place them away from any heat source.
    Electric heater is expensive, try to reduce its use as much as you can.
    Control  the progress of your consumption regularly, either from meters or from the information mentioned on your bills.