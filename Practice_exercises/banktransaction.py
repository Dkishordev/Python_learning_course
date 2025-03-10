""" write simple program in basic python using concept of list,
dictionary and functions that covers every possible scenarios:
--Banking app
--assume the existing balance , sender info, receiver info in dictionary and modify wherever necessary.
-- limit per day transaction to 100000
-- after transaction sender amount should not be less than 5000 """
from prettytable import PrettyTable
import ast 

transdetails =[{
    "name" :"trans1",
    "existingbalance": 10000,
    "alreadytransfered":80000,
    "transferamount": 1000,
    "receiveramount": 20000},
    {
    "name" :"trans2",
    "existingbalance": 30000,
    "alreadytransfered":100000,
    "transferamount": 1000,
    "receiveramount": 20000},
    {
    "name" :"trans3",
    "existingbalance": 20000,
    "alreadytransfered":5000,
    "transferamount": 5000,
    "receiveramount": 10000},
    {
    "name" :"trans4",
    "existingbalance": 30000,
    "alreadytransfered":5000,
    "transferamount": -5000,
    "receiveramount": 20000},
    {
    "name" :"trans5",
    "existingbalance": 10000,
    "alreadytransfered":5000,
    "transferamount": 6000,
    "receiveramount": 20000},
    {
    "name" :"trans6",
    "existingbalance": 30000,
    "alreadytransfered":10000,
    "transferamount": 35000,
    "receiveramount": 20000}
    ] 

def transaction_limit(trans_amount):
    if trans_amount >= 100000 :
        return False
    else:
        return True

def process_transaction(senderbalance, transamount, receiveramount,trans):
    senderbalance = senderbalance - transamount
    receiveramount = receiveramount + transamount
    #print(f"{trans}: Transaction success")
    return senderbalance, receiveramount

def checkbalance(extamt,transamt):
    if (extamt - transamt) >= 5000 and transamt > 0 :
        return True
    else:
        return False
def printdetails(transdetails):
    table = PrettyTable(["Transaction",  "Sender Amount", "Receiver Amount","Transaction Amount","Status"]) 
    for dictitems in transdetails:
        table.add_row([dictitems["name"], dictitems["existingbalance"], dictitems["receiveramount"], 
                       dictitems["transferamount"], dictitems["status"]])
            
    print(table)

    pass

def main():
    print("============== Before Transaction ===================")
    for item in transdetails:
        item.update({"status":"Not Transfered"})     
    printdetails(transdetails)
    for item in transdetails:
        sufficient_balance = checkbalance(item.get("existingbalance"),item.get("transferamount"))
        trans_allowed = transaction_limit(item.get("alreadytransfered"))
        if sufficient_balance and trans_allowed:
            senderamt, receiveramt =process_transaction(item.get("existingbalance"),item.get("transferamount"),
                                item.get("receiveramount"),item.get("name"))
            item.update({"existingbalance":senderamt})
            item.update({"receiveramount":receiveramt})
            item.update({"status":"Success"})
        else:
            if not sufficient_balance and not trans_allowed:
                item.update({"status":"Failure"})
                #print(f"{item.get("name")}: Balence is not sufficent or max transaction limit reached.") 
            elif not sufficient_balance and  trans_allowed:
                item.update({"status":"Failure"})
                #print(f"{item.get("name")}: Not sufficent balance")
            else:
                item.update({"status":"Failure"})
                #print(f"{item.get("name")}: Transaction limit reached.") 
    print("============== After Transaction ===================")
    printdetails(transdetails)


if __name__ == "__main__":
    main()
