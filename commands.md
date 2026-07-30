# LINUX COMMAND LISTS

## 1.NAVIGATIONS

pwd           -                       Show current directory
ls                -                       List files
ls -l            -                       Detailed list
ls -a           -                       Show hidden files
cd folder  -                      Change directory
cd ..            -                     Go back one directory
cd ~             -                     Go to home directory
clear           -                      Clear terminal
# 2.FILE MANAGEMENT
touch file.txt               -      Create a file
mkdir myfolder          -      Create a directory
rmdir myfolder           -      Remove empty directory
rm file.txt                       -     Delete a file
rm -r myfolder             -     Delete directory
cp file1 file2                  -     Copy file
mv file1 file2                 -     Move/Rename file
cat file.txt                       -      Display file contents
nano file.txt                   -      Edit file
# 3.PERMISSIONS
chmod 755 file.sh       -     Change permissions
chmod +x file.sh          -       Make executable
ls -l                                     -      View permissions


# 4.USER INFORMATION
whoami           -        Current user
id                         -      User ID
hostname        -       System name
uname -a          -       Kernel information
# 5.PACKAGE MANAGEMENT 
sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt remove git
# 6.PROCESS MANAGEMENT
ps
ps -ef
top
kill PID
# 7.NETWORKING
ip a
ping google.com
curl https://example.com
wget https://example.com/file
# 8.DISK USAGE
df -h
du -sh folder
free -h
# 9.SEARCHING
find . -name "file.txt"
grep "hello" file.txt
history
# 10.COMPRESSION
zip file.zip file.txt
unzip file.zip
tar -cvf archive.tar folder
tar -xvf archive.tar
# 11.GIT COMMANDS
git init
git clone <repository-url>
git status
git add .
git commit -m "First commit"
git push origin main
git pull origin main
git branch
git checkout branch-name
git merge branch-name
# 12. WINDOWS 
explorer.exe .          -  Open current folder in Windows Explorer
code .                          - Open folder in VS Code
notepad.exe file.txt  -  Open file in Notepad
