# 3-4
guests_dinner = ['aryo', 'dan', 'david', 'nathan']
invite_aryo = guests_dinner[0].title() + ", I'd like to cordially invite you to dinner."
invite_dan = guests_dinner[1].title() + ", I'd like to cordially invite you to dinner."
invite_david = guests_dinner[2].title() + ", I'd like to cordially invite you to dinner."
invite_nathan = guests_dinner[3].title() + ", I'd like to cordially invite you to dinner."
print invite_aryo + "\n" + invite_dan + "\n" + invite_david + "\n" + invite_nathan

# 3-5
print guests_dinner[3]
del guests_dinner[3]
guests_dinner.insert(3, 'rick')
print guests_dinner

invite_rick = "Hey " + guests_dinner[3].title() + ", I know it's last minute, but, I'd like to cordially invite you to dinner."
print invite_aryo + "\n" + invite_dan + "\n" + invite_david + "\n" + invite_rick

# 3-6
print  "I found a bigger dinner table!"
guests_dinner.insert(0, 'tony')
guests_dinner.insert(5, 'christopher')
guests_dinner.append('paulie')
print guests_dinner

invite_tony = guests_dinner[0].title() + ", come to dinner."
invite_christopher = guests_dinner[5].title() + ", come to dinner."
invite_paulie = guests_dinner[6].title() + ", come to dinner."

print invite_tony + "\n" + invite_aryo + "\n" + invite_dan + "\n" + invite_david + "\n" + invite_rick + '\n' + invite_christopher + '\n' + invite_paulie

# 3-7
print guests_dinner
print "The new dinner table won't arrive on time and I am only able to accomodate a party of two."
popped_paulie = guests_dinner.pop()
popped_christopher = guests_dinner.pop()
popped_rick = guests_dinner.pop()
popped_david = guests_dinner.pop()
popped_dan = guests_dinner.pop()
msg_aryo = "You are still more than welcome to come, " + guests_dinner[1].title() + "."
msg_tony = "You are still more than welcome to come, " + guests_dinner[0].title() + "."
print msg_aryo + '\n' + msg_tony
del guests_dinner[0] #Can be 1 or 0. Both work. Order of Operations.
del guests_dinner[0]
print guests_dinner

guests_remaining = len(guests_dinner)
print "So I will be expecting to accomodate " + str(guests_remaining) + " guests tonight. See you there!"


























