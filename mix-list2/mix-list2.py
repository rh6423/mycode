#!/usr/bin/env python3
proto = ['ssh', 'http', 'gopher']
protoa = ['ssh', 'http', 'gopher']
print(proto)
proto.append('dns') # this line will add 'dns' to the end of the list
protoa.append('dns') # this line will add 'dns' to the end of the list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to append method
print(protoa)
proto.insert(2, 'https') # insert https before gopher
proto.insert(8, 8080) # insert bogus gopher port in right place
print(proto)
