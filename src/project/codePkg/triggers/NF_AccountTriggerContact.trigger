/**
* @File Name:	NF_AccountTriggerContact.trigger
* @Description: On account value insertion udates the contact database  
* @Author:   	Sandeep Bharti
* @Group:   	Trigger
* @Modification Log	:
*-------------------------------------------------------------------------------------
* Ver       Date        Author      Modification
* 1.0       2018-05-25  Sandeep    Created the file/class
*/

trigger NF_AccountTriggerContact on Account(after insert, after update) {
    List<Contact> conList = new List<Contact>();
    
    Map<Id,Account> contactMap = new Map<Id,Account>(
        [SELECT Id,(SELECT Id FROM Contacts) FROM Account WHERE Id IN :Trigger.New]);
    
    for(Account a : Trigger.New) {
        if (contactMap.get(a.Id).Contacts.size() == 0) {
            conList.add(new Contact(LastName=a.Name + ' Contact',
                                       AccountId=a.Id));
        }           
    }
    if (conList.size() > 0) {
        insert conList;
    }
}