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
    Counter_number: Zählernummer
    Counter_statue: takes up to 5 values such as working fine (Satus=0), not working, on hold statue, ect
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

    # EDA
    - objects: invoice_date, counter_statue, counter_type
- classes, but not with type object: tarif_type, counter_code, reading_remarque, counter_coefficient, months_number

- what about hight consumtion-levels => fraud detection, or a companie ( client_train.client_cat/invoice_train.tarif_type )? 
- same with old_index - new_index
- coefficent, old_index, new_index and the consumtion-levels are belonging together
- what about the high numbers of month_numbers -> error? are that days?

- counter_statue: should have 5 classes but there are more ... 5 of them are strings ( '0' '5' '1' '4' 'A' ) the rest are int
* A = only client: train_Client_30467 has those statues for counter_number == 9505424 later it change to 0 -> and the other features also the same, except date of invoice and number of month, also just onr observation has a level of consommation of 50 -> else it is 0 => 'A' can be replaced with 0
* '0', '1', '4', '5' -> can be changed to int
* all the other classes, their observations are calculating month_number by adding consommation_level_2 with new_index ???? What happend there ????
* counter_statue == 269375 -> can be droped, since there is just one observation and also the train_Client_53725 belong to only that observation 	
* counter_statue == 420 -> can be droped, since there is just one observation and also the train_Client_79075 has one Electric contract with more than one date of invoice but the observation with counter_staue is a Gas contract
* 
- month_number > 88 columns are delayed at one posistion to the right -> delete
- counter_code: < 100 is this a mistake?

- reading_remarque: compare this to target, because if something is wrong the agent gives a bad score -> according to plots below, low numbers might be bad 

- consommation_levels

# Feature ideas
Hier sind einige Ansätze, die dir helfen können:
🔍 Typische Betrugsmuster bei Stromzählern
Muster	Erkennungsmerkmal
Manipulation des Zählers	Plötzlicher Verbrauchsrückgang trotz gleichem Nutzungsverhalten
Zähler-Rücksetzung	old_index > new_index oder ungewöhnliche Sprünge
Unregelmäßige Ablesungen	Fehlende Werte oder lange Lücken in reading_remarque
Verbrauch außerhalb der Norm	Abweichung von consommation_level_* im Vergleich zu ähnlichen Kunden
📊 Feature Engineering Ideen

Basierend auf deinen Spalten könntest du folgende Features erstellen:

# Verbrauchstrends
df['consumption_trend'] = df.groupby('client_id')['consommation_level_4'].transform(lambda x: x.pct_change())

# Zählerstand-Konsistenz
df['index_anomaly'] = (df['old_index'] > df['new_index']).astype(int)

# Verbrauch pro Monat normalisieren
df['avg_monthly_consumption'] = df['consommation_level_4'] / df['months_number']

# Abweichung vom Tarif-Durchschnitt
df['consumption_vs_tarif_avg'] = df['consommation_level_4'] / df.groupby('tarif_type')['consommation_level_4'].tr