def arithmetic_arranger(problems,cond=False):
    condition=True
    while condition:
    
        try: 
            assert len(problems)<=5
            
        except:
            arranged_problems='Error: Too many problems.'
            break
    
        try:
            for pr in problems:
                assert pr.split()[1]=='+' or pr.split()[1]=='-'
        
        except AssertionError:
            arranged_problems="Error: Operator must be '+' or '-'."
            break
        try:
            for pr in problems:
                assert pr.split()[0].isdigit()==True and pr.split()[2].isdigit()==True
        except:
            arranged_problems='Error: Numbers must only contain digits.'
            break
        
        try:
            for pr in problems:
                assert len(pr.split()[0])<=4 and len(pr.split()[2])<=4
              
        except:
            arranged_problems='Error: Numbers cannot be more than four digits.'
            break
        
        row1=[first.split()[0] for first in problems]
        sign=[first.split()[1] for first in problems]
        row2=[first.split()[2] for first in problems]
        #print(row2)
        row3=[]
        for i  in range(0,len(problems)):
            
            if len(row1[i])>len(row2[i]):
                row3.insert(i,'-'*(len(row1[i])+2))
                row2[i]=sign[i]+' '*( len(row3[i]) -len(row2[i])-1 ) +row2[i]
                row1[i]=' '*(len(row3[i])-len(row1[i]))+row1[i]
            elif len(row1[i])<len(row2[i]):
                row3.insert(i,'-'*(len(row2[i])+2))  
                row2[i]=sign[i]+' '+row2[i]
                row1[i]=' '*(len(row3[i])-len(row1[i]))+row1[i]
            else:
                row3.insert(i,'-'*(len(row1[i])+2))  
                row2[i]=sign[i]+' '+row2[i]
                row1[i]=' '*2+row1[i]
        row1='    '.join(row1)
        row2='    '.join(row2)
        
        row4=[]
        if cond==False:
            row3='    '.join(row3)
            arranged_problems=row1+'\n'+row2+'\n'+row3  
        else:
                      
            for i  in range(0,len(problems)):
                
                row4.insert(i, str(eval(problems[i])))

                row4[i]=' '*(len(row3[i])-len(row4[i]))+row4[i]
            row3='    '.join(row3)
            row4='    '.join(row4)
            arranged_problems=row1+'\n'+row2+'\n'+row3+'\n'+row4
        
        condition=False
    print(arranged_problems)
    return arranged_problems 
        
