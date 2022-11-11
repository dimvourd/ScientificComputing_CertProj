def change_period(period,n):
    if period=='PM':
        period='AM'
        n=n+1

    else:
        period='PM'
        
    return period, n


def add_time(start, duration,day=None):

    start=start.split()
    hr=0
    #minutes
    mnt=int(start[0].split(':')[1])+int(duration.split(':')[1])
    if mnt>=60:
        hr=1
        mnt=mnt-60
       
    if len(str(mnt))==1:
        mnt='0'+str(mnt)
    else:
        mnt=str(mnt)
    
    
    #period
    period=start[1]
    
    #hour
    hr=int(start[0].split(':')[0])+int(duration.split(':')[0])+hr
    
    n=hr//24
    hr=hr%24
    
    if hr>12 and hr<=24:
        hr=hr-12
        period,n=change_period(period,n)    
    elif hr==12:
        period,n=change_period(period,n)
        
    #day
    new_time=str(hr)+':'+mnt+' '+period
    
    if day==None:
        if n==1: 
            new_time=new_time+' (next day)'
        elif n>1:
            new_time=new_time +' ({} days later)'.format(str(n))
    else:
        week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day=day.capitalize( )
        
        day=week[(n+week.index(day))%7]
        
            
        if n>1:
            new_time=new_time +', {} ({} days later)'.format(day,str(n))
        elif n==1:
            new_time=new_time +', {} (next day)'.format(day)
        else:
            new_time=new_time +', {}'.format(day)
    
    return new_time