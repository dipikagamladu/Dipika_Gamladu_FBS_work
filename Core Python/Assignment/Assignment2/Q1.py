#convert the time entered in hh , min , and sec into seconds.
hour = int(input('Enter hours:'))            #1
min = int(input('Enter minutes:'))            #60
sec = int(input('Enter seconds:'))            #3600
total_seconds = hour*3600 + min*60 + sec
print(total_seconds)