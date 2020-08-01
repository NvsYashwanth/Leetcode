class Solution:
    def reformatDate(self, date: str) -> str:
        arr=date.split(" ")
        Month=['Jan','Feb','Mar','Apr','May','Jun','Jul',
              'Aug','Sep','Oct','Nov','Dec']
        s=str(Month.index(arr[1])+1)
        m=len(s)
        if m==1:
            s='0'+s
        ss=arr[0][:-2]
        if len(ss)==1:
            ss='0'+ss
        return(arr[2]+'-'+s+'-'+ss)