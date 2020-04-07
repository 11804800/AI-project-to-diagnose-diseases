"# AI-project-to-diagnose-diseases" 
lst=['Corona','Asthma','ORVI','Meningitis','Bronchitis']
lst1=[1,2,3,4,5]
for i in range(0,5):
    print(lst1[i],lst[i])
Dis=int(input("Enter the number you want to get diagnosed otherwise zero to exit :"))
if(Dis==1):
    print("Corona")
    print("The Symptoms of this disease is high fever with dry cough and problem in breathing \n And it shows its symptoms within a week")
    Choice=int(input("Enter if you have ""observed this symptoms then 1 if not then 2 :"))
    if(Choice==1):
        print("Your answer is yes")
        print("Enter 1 for yes and 0 for no")
        Ans0=int(input("Have you travelled on through outer country recently :"))
        if(Ans0==1):
            print("Your answer is yes")
        elif(Ans0==0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()

        Ans01=int(input("Have you came in a contact with a person having problem in breathing and fever and cough :"))
        if(Ans01==1):
            print("Your answer is yes")
        elif(Ans01==0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
        Ans02=int(input("Have you came in contact with confirmed corona Virus patient :"))
        if(Ans02==1):
            print("Your answer is yes")
        elif(Ans02==0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
        Tot=(Ans0+Ans01+Ans02)/10
        if(Tot==0.3):
            print(" ")
        elif(Tot==0.2):
            print(" ")
        Ans = int(input("Do you have any coughing problem :"))
        if(Ans==1):
            print("Your answer is yes")
            sym1 = int(input("On scale of 1 to 10 rate Coughing :"))
            if(sym1>=11):
                print("Only rate from 1 to 10")
            Ans3=int(input("Do You have any problem like Asthma :"))
            if (Ans3 == 1):
                print("Your answer is yes")
            elif (Ans3 == 0):
                print("Your answer is No")
            else:
                print("please enter yes or no")
                exit()
            t=sym1
        Ans1 = int(input("Do you have fever :"))
        if(Ans1==1):
             print("Your answer is Yes")
             Sym2=int(input("On scale of 1 to 10 rate Fever :"))
             if(Sym2>=11):
                 print("Only rate from 1 to 10")
             t=t+Sym2
        Ans4=int(input("Are you facing problem in breathing :"))
        if (Ans4 == 1):
            print("Your answer is yes")
        elif (Ans4 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        if(Ans4==1):
            print("Your answer is yes")
            Sym3=int(input("On Scale of 1 to 10 rate your problem in breathing :"))
            if(Sym3>=11):
                print("Only rate from 1 to 10")
            Ans2 = int(input("Do you have any breathing problem ? then yes if not then no :"))
            if(Ans2==1):
                lst2=['Athama','Emphysema','Pneumonia']
                for i in range(0,3):
                    print(lst2[i])
                A=int(input("Enter the number"))
                if(A==1):
                    print("Asthama")
                elif(A==2):
                    print("Emphysema")
                elif(A==3):
                    print("penumonia")
            t=t+Sym3+Tot
        if(25.1<=t<=30.3):
            print("High chances")
            print("Sugestion \nYou are in immediately need of visiting  the nearest Corona help center And Cover your mouth,tell you family members to ")
            print("Stay away from  you and avoid physical contact and maintain at least 1 meter distance  Wash your hand after every tweenty minute")
        elif(24.3<=t<=19.1) :
            print("Medium chances")
            print("Sugestion \nYou need to visit  the nearest Corona help center for test and confirmation And Cover your mouth")
            print("Stay away from others and avoid physical contact and maintain at least 1 meter distance  Wash your hand \nafter every tweenty minute and stay at home")
        elif(18.2>=t>=0.3):
            print("Low Chances")
            print("Sugestion \nYou need to Cover your mouth Stay away from others and avoid physical contact and maintain at ")
            print(" least 1 meter distance  Wash your hand after every tweenty minute and stay at home.")
    elif(Choice==2):
        print("Thanks for using")
        exit()
    else:
        Print("Wrong input")
        exit()

if(Dis==2):
    print("Enter 1 for yes and 0 for no ")
    print("Asthma")
    print("Symptoms include difficulty in breathing ,chest pain ,cough and wheezing .the symptoms may sometime flare up")
    Choice = int(input("Enter if you have ""observed this symptoms then 1 if not then 2 :"))
    if (Choice == 1):
        print("Your answer is yes")
        sym1=int(input("Do you cough at night or all the time:"))
        if(sym1==1):
            print("Your answer is yes")
        elif(sym1==0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym2=int(input("Do you experience shortness in breathing or rapid breathing: "))
        if(sym2==1):
            print("Your answer is yes")
        elif(sym2==0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()

        sym3=int(input("Do you chest pressure ,flare ,Anxiety : "))
        if(sym3==1):
            print("Your answer is yes")
        elif(sym3==0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()

        sym4=int(input("Does your heart rate suddenly increases and you feel irritation in throat: "))
        if(sym4==1):
            print("Your answer is yes")
        elif(sym4==0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        t=sym1+sym2+sym3+sym4
        print(t)
        if(t>=4):
            print("suggestion \nyou are in critcial condition and you need treatment")
            print("teartment\nAsthma can be managed with resuce inhaler to treat symptoms (salbutamol) and controller inhaler that \nprevents symptoms(steroids)")
        if(t<=2):
            print("suggestion \nyour body is showing the less symptoms of asthma you just need a need a controller inhaler which will prevent you from asthma attack")
    elif(Choice == 2):
        print("Thanks for using")
        exit()
    else:
        Print("Wrong input")

elif(Dis==3):
    print("ORVI")
    print("Symptoms ussually resolve within two weeks and include a scratchy or sore throat,sneezing,stuffy\nnose and cough")
    Choice = int(input("Enter if you have ""observed this symptoms then 1 if not then 2 :"))
    if (Choice == 1):
        print("your answer is Yes")
        print("Enter 1 for yes and 0 for no")
        sym1 = int(input("Do you feel pain in the sinuses:"))
        if (sym1 == 1):
            print("Your answer is yes")
        elif (sym1 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym2 = int(input("have you lost the experience of smell and experiece congestion: "))
        if (sym2 == 1):
            print("Your answer is yes")
        elif (sym2 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym3 = int(input("Does your whole body is in fever and restless: "))
        if (sym3 == 1):
            print("Your answer is yes")
        elif (sym3 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym4 = int(input("Do you feel irritation in throat and soareness : "))
        if (sym4 == 1):
            print("Your answer is yes")
        elif (sym4 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym5=int(input("DO you have cough and headche and swollen lymph nodes: "))
        if (sym5 == 1):
            print("Your answer is yes")
        elif (sym5 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        t = sym1 + sym2 + sym3 + sym4+sym5
        print(t)
        if (t >= 5):
            print("suggestion \nyou are in bad condition and you need treatment")
            print(
                "teartment\nTreatment includes rest and medication to relieve symptoms. and medicines are couh medicine ,Nonsteroidal anti-inflammatory drug,Analgesic\nand dietary Supplemant ")
        if (t <= 3):
            print("suggestion \nyour body is showing the less symptoms of asthma you just need rest and normal mediction to relief")
    elif(Choice == 2):
        print("Your answer is no")
        print("Thanks for using")
        exit()
    else:
        Print("Wrong input")
        exit()
elif(Dis==4):
    print("Meningitis")
    print("symptoms include headche,fever,stiff neck")
    Choice = int(input("Enter if you have ""observed this symptoms then 1 if not then 2 :"))
    if (Choice == 1):
        print("your answer is Yes")
        print("Enter 1 for yes and 0 no")
        sym1 = int(input("Do you feel pain in the back:"))
        if (sym1 == 1):
            print("Your answer is yes")
            Ans=int(input("Rate your pain in back from 1 to 10"))
            if(Ans>=11):
                print("Only rate from 1 to 10")
                exit()
        elif (sym1 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
        sym2 = int(input("Do you have fever and you have lost your appetite and you are shivering: "))
        if (sym2 == 1):
            print("Your answer is yes")
            Ans0=int(input("Rate your fever from 1 to 10"))
            if(Ans0>=11):
                print("Only rate from 1 to 10")
                exit()
        elif (sym2 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")

        sym3 = int(input("Are you vomiting and feeling nausea: "))
        if (sym3 == 1):
            print("Your answer is yes")
        elif (sym3 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym4 = int(input("Is you skin has blotchy rashes or Red rashes : "))
        if (sym4 == 1):
            print("Your answer is yes")
        elif (sym4 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym5 = int(input("Does your heart beat has become fast: "))
        if (sym5 == 1):
            print("Your answer is yes")
        elif (sym5 == 0):
            print("Your answer is No")
        else:
            print("please enter yes or no")
            exit()
        sym6=int(input("Do you feel sleepiness all the time: "))
        if(sym6==1):
            print("Your answer is Yes")
        elif(sym6==0):
            print("your answer is No")
        else:
            print("Please enter yes or no ")
            exit()
        t = sym1 + sym2 + sym3 + sym4 + sym5+sym6
        print(t)
        if (t >= 6):
            print("suggestion \nyou are in Bad condition and you need treatment")
            print("teartment\nDepending on the cause, Meninfitis may get better on its own or it can be life threatening require urgent \nAnti-biotic treatment")
            print("teatment\nAnti-Biotic, Steroid and penicilin and oxyen therapy and Hospitalization")

        if (t <= 3):
            print("suggestion \nyour body is showing the less symptoms of meningitis If you still have doubt then you can take penincilin.")
    elif(Choice == 2):
        print("Thanks for using")
        exit()
    else:
        Print("Wrong input")
        exit()
elif(Dis==5):
    print("Bronchitis")
    print("Symptoms of bronchitis include coughing up thickened mucus and shortness of breath.")
    Choice=int(input("Enter 1 if yes otherwise 2 for no: "))
    if(Choice==1):
        print("Your answer is Yes")
        print("enter 1 for yes and 0 for no")
        sym1=int(input("Do you have cough problem: "))
        if(sym1==1):
            print("Your answer is Yes")
        elif(sym1==0):
            print("Your answer is no")
        else:
            print("please enter from 0 to 1")
            exit()
        sym2=int(input("Do you have Runny nose:  "))
        if(sym2==1):
            print("Your answer is Yes")
        elif(sym2==0):
            print("Your answer is no")
        else:
            print("please enter from 0 to 1")
            exit()
        sym3=int(input("Do feel Chest pressure and shortness of breath: "))
        if(sym3==1):
            print("Your answer is Yes")
        elif(sym3==0):
            print("Your answer is no")
        else:
            print("please enter from 0 to 1")
            exit()
        sym4=int(input("Do you feel restless and sleepiness all the day: "))
        if(sym4==1):
            print("Your answer is Yes")
        elif(sym4==0):
            print("Your answer is no")
        else:
            print("please enter from 0 to 1")
            exit()
        t=sym1+sym2+sym3+sym4
        if(t>=3):
            print("Suggestion\nyou are in bad condition and you have bronchitis and you need to take anti-inflammatory drug,Analgestic,Narotic and \ncough medicine")
        elif(t<=2):
            print("Suggestion\nyou have less symptoms of the bronchitis so you can go to nearby click or you can take Narcotic or Cough medicine.")

    elif(Choice==2):
        print("Your answer is No")
    else:
        print("Wrong input")
        exit()
else:
    print(“Please enter a valid number”)
    print("Thanks for using")
    exit()
 
