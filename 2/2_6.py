kata1, kata2 = input("masukkan kata pertama : ").split()

if kata1 == kata2:
    print("{} dan {} adalah anagram".format(kata1,kata2))
else: 
    print("{} dan {} bukan anagram".format(kata1,kata2))