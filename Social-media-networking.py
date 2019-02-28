import random
def each_user(file_name):
    friends = open(file_name).read().splitlines()
    eachuser = []
    for i in range(1,len(friends)):
        x = int(friends[i][:friends[i].index(" ")])
        y = int(friends[i][friends[i].index(" ")+1:])

        if x not in eachuser:
            eachuser.append(x)
        if y not in eachuser:
            eachuser.append(y)
    eachuser.sort()
    return eachuser

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    uniq = each_user(file_name)

    t = []
    for i in range(1,len(friends)):
        x = friends[i][:(friends[i].index(" "))]
        y = friends[i][friends[i].index(" ")+1:]
        t.append((int(x),int(y)))

    prev = each_user(file_name).copy()
    for i in range(len(t)):
        user01 = t[i][0]
        user02 = t[i][1]
        user03= t[i][1]
        user04= t[i][0]

        if user01 in prev:
            network.append(((user01),[user02]))
            prev.remove(user01)

        else:
            for r in range(len(uniq)):
                if user01 == network[r][0]:
                    network[r][1].append(user02)
                    break 

        if user03 in prev:
            network.append(((user03,[user04])))
            prev.remove(user03)
        else:
            for u in range(len(uniq)):
                if user03 == network[u][0]:
                    network[u][1].append(user04)
                    break
    network.sort()
    return network
def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    a = None
    b = None
    for x in range(len(network)):
        if user1 == network[x][0]:
            a = x
        if user2 == network[x][0]:
            b = x
    for x in (network[a][1]):
        for y in (network[b][1]):
            if x == y:
                if y not in common:
                    common.append(y)
                
    
    common.sort()
    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    length_commonfriends = []
    for x in range(len(network)-1):
        if (user != network[x][0]) and (user not in network[x][1]):
            length_commonfriends.append((network[x][0],getCommonFriends(user,network[x][0],network)))
    maximum_number_of_friends = None
    maximum_number_of_friends_index = None
    
    for x in range(len(length_commonfriends)):
        if maximum_number_of_friends == None:
            maximum_number_of_friends = len(length_commonfriends[x][1])
            maximum_number_of_friends_index = x
        elif (len(length_commonfriends[x][1])) > (maximum_number_of_friends):
            maximum_number_of_friends = len(length_commonfriends[x][1])
            maximum_number_of_friends_index = x
            
    if (maximum_number_of_friends != None) and ( len(length_commonfriends)!= 0):
        return int(length_commonfriends[maximum_number_of_friends_index][0])
    else:
        return None
    

    


def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    a = 0
    for x in range(len(network)):
        if len(network[x][1]) >= k:
            a += 1
    return a
    
 

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    highest = 0
    for x in range(len(network)):
        if len(network[x][1]) > highest:
            highest = len(network[x][1])
    return highest
    
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    highest = 0
    for x in range(len(network)):
        if len(network[x][1]) > highest:
            highest = len(network[x][1])
    for x in range(len(network)):
        if len(network[x][1]) == highest:
            max_friends.append(network[x][0])
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    a = 0
    b = 0
    for x in range(len(network)):
        a += len(network[x][1])
        b += 1

    c = a/b
    return c
    
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    t = []
    l = []
    for x in range(len(network)):
        if (network[x][0]) not in t:
            t.append(network[x][0])
    t.sort()
    for x in range(len(network)):
        l = network[x][1]
        l.append(network[x][0])
        l.sort()
        if (l == t):
            return True
    return False
    


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    all_users_in_network = []
    for x in range(len(network)):
        all_users_in_network.append(network[x][0])

    q = True
    while q:
        x = input("Enter an integer for a user ID: ").strip()
        if x.isdigit():
            x = int(x)
            if x in all_users_in_network:
                return x
                q = False
            else:
                print("That user does not exist. Try again.")
        else:
            print("That was not an integer. Try again.")
    

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
