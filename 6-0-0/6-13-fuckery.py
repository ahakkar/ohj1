f=lambda s,z='\00':(r:=lambda s,L,p:not(s)and(L)or s[0]>p[-1]and r(s[1:],L,p+s[0])or r(s[1:],len(p)>len(L)and(p)or L,s[0]))(s+z,z,z)

def main():
    longest_substring_in_order = f

    print(longest_substring_in_order("abcdfklmn"))      
    print(longest_substring_in_order("abcfdf"))
    print(longest_substring_in_order("abcabcdefgabab"))  
    print(longest_substring_in_order("acdkbarstyefgioprtyrtyx"))
    print(longest_substring_in_order("ffgdfjkgabcdf"))          
    print(longest_substring_in_order("x"))
    print(longest_substring_in_order("aaa"))
    print(longest_substring_in_order('xyzstuopqklmefgabc'))
    print(longest_substring_in_order('acdkbarstyefgioprtyrtyx'))

if __name__ == "__main__":
    main()
