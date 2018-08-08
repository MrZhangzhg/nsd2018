#!/bin/bash

if [ -n "$1" ]; then
    nums=$1
else
    nums=5
fi

count=0

while [ $count -lt $nums ]
do
    let n++
    id user$n &> /dev/null
    if [ $? -ne 0 ]; then
         useradd user$n
         echo 123456 | passwd --stdin user$n &>/dev/null
         chage -d0 user$n
         let count++
         echo -e "create user$n...\t\t\t\t\033[32;1m[DONE]\033[0m"
    fi
done
#!/bin/bash

if [ -n "$1" ]; then
    nums=$1
else
    nums=5
fi

count=0

while [ $count -lt $nums ]
do
    let n++
    id user$n &> /dev/null
    if [ $? -ne 0 ]; then
         useradd user$n
         echo 123456 | passwd --stdin user$n &>/dev/null
         chage -d0 user$n
         let count++
         echo -e "create user$n...\t\t\t\t\033[32;1m[DONE]\033[0m"
    fi
done

