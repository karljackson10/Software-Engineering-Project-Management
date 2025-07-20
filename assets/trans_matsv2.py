import pandas as pd
#Access the lateat DfE Transition Matix and store as a dataframe 
df = pd.read_csv("https://explore-education-statistics.service.gov.uk/data-catalogue/data-set/f65c2e07-a857-4245-b5ba-8effb0f89ba8/csv")
#convert the data frame to a dictionary
tm=df.to_dict()

def get_expected(subject, ks2):
    '''returns the expected points for a specificed qualification given ks2 starting points'''

    for i in tm['subject']:
        #searches the transition matrix for the subject
        if tm['subject'][i] == subject and tm['breakdown'][i] == 'Total' and tm['ks2_scaled_score_group'][i] != 'Total':
            #assigns the scaled score group to tm_ks2
            tm_ks2 = tm['ks2_scaled_score_group'][i]
            #assigns the limits for the lowest band
            if tm_ks2 == 'Less than 80':
              lower = 0
              upper =79.5
            else:
              #assigns the limits for the bands stored in the format
              # lower - higher 
              dash = tm_ks2.find('-')
              #ensures the limits are stored as decimal values
              lower = float(tm_ks2[:dash])
              upper = float(tm_ks2[dash+2:])    
            
            #finds a match for the ks2 value
            if float(ks2)>=lower and float(ks2) <=upper:
              print('Match: '+str(i)+' '+ tm['subject'][i] +' '+ tm['ks2_scaled_score_group'][i])
              band = tm_ks2
              #assigns and prints results for standard GCSEs
              if subject != 'Combined Science':
                #calculates the expected value to 2dp
                expected = round((float(tm['perc_1'][i])*1 + float(tm['perc_2'][i])*2 + float(tm['perc_3'][i])*3 + float(tm['perc_4'][i])*4 
                + float(tm['perc_5'][i])*5 + float(tm['perc_6'][i])*6 + float(tm['perc_7'][i])*7 + float(tm['perc_8'][i])*8 + float(tm['perc_9'][i])*9)/100,2)
                #display expected value
                print ('Expected: ' + str(expected))
                #calculates probabilites as a decimal from the sting stored in TM
                chance9 = float(tm['perc_9'][i])/100
                chance98 = chance9 + float(tm['perc_8'][i])/100
                chance97 = chance98 +float(tm['perc_7'][i])/100
                chance96 = chance97 + float(tm['perc_6'][i])/100
                chance95 = chance96 + float(tm['perc_5'][i])/100
                chance94 = chance95 + float(tm['perc_4'][i])/100
                chance93 = chance94 + float(tm['perc_3'][i])/100
                chance92 = chance93 + float(tm['perc_2'][i])/100
                chance91 = chance92 + float(tm['perc_1'][i])/100
              else:
                #caclulates the output for combined-science which has a differnt data structure
                expected = round((float(tm['perc_11'][i])*1
                                + float(tm['perc_21'][i])*1.5
                                + float(tm['perc_22'][i])*2
                                + float(tm['perc_32'][i])*2.5
                                + float(tm['perc_33'][i])*3
                                + float(tm['perc_43'][i])*3.5
                                + float(tm['perc_44'][i])*4
                                + float(tm['perc_54'][i])*4.5
                                + float(tm['perc_55'][i])*5
                                + float(tm['perc_65'][i])*5.5
                                + float(tm['perc_66'][i])*6
                                + float(tm['perc_76'][i])*6.5
                                + float(tm['perc_77'][i])*7
                                + float(tm['perc_87'][i])*7.5
                                + float(tm['perc_88'][i])*8
                                + float(tm['perc_98'][i])*8.5
                                + float(tm['perc_99'][i])*9                              
                                )/100,2)
                
                #caluates cumulative probabiliets of achieving a grade
                chance9 = round(float(tm['perc_99'][i])/100,3)
                chance98 = round((chance9 + (float(tm['perc_98'][i]) + float(tm['perc_88'][i]) )/100),3)
                chance97 = round((chance98 + (float(tm['perc_87'][i]) + float(tm['perc_77'][i]) )/100),3)
                chance96 = round((chance97 + (float(tm['perc_76'][i]) + float(tm['perc_66'][i]) )/100),3)
                chance95 = round((chance96 + (float(tm['perc_65'][i]) + float(tm['perc_55'][i]) )/100),3)
                chance94 = round((chance95 + (float(tm['perc_54'][i]) + float(tm['perc_44'][i]) )/100),3)
                chance93 = round((chance94 + (float(tm['perc_43'][i]) + float(tm['perc_33'][i]) )/100),3)
                chance92 = round((chance93 + (float(tm['perc_32'][i]) + float(tm['perc_22'][i]) )/100),3)
                chance91 = round((chance92 + (float(tm['perc_21'][i]) + float(tm['perc_11'][i]) )/100),3)
                

              #displays probabilites of achieving threshold grades
              print('Chance 7+ ' + str(chance97*100) + '%')
              print('Chance 5+ ' + str(chance95*100) + '%')
              print('Chance 4+ ' + str(chance94*100) + '%')
              #returns statisitics as a tuple
              return [expected, round(chance91,3), round(chance92,3), round(chance93,3), round(chance94,3),
                     round(chance95,3), round(chance96,3), round(chance97,3), round(chance98,3), round(chance9,3), band]

#Only executed if the script is run as a main programme       
if __name__ == "__main__":
    print('Start')


    subject='Art and Design'
    #subject = 'Combined Science'
    ks2=102
    get_expected(subject,ks2)
   