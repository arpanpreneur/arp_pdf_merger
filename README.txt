On Windows, to run a PowerShell script with administrative privileges, follow these steps:

1. Open the Start menu (Press Windows key), type `powershell`, right-click on `Windows PowerShell`, and select `Run as administrator`.

2. If the User Account Control dialog box appears, confirm that the action it displays is what you want, and then click `Yes`.

3. By default, Windows PowerShell is not set up to run scripts. So, you need to change the execution policy to allow scripts. Run the following command:

```
Set-ExecutionPolicy RemoteSigned
```

This command allows the running of PowerShell scripts. You should select `Yes` or `Yes to All` when asked for permissions.

4. Navigate to the directory where your script is located by using the `cd` (Change Directory) command, for example:

```
cd C:\path\to\your\arp_mdf_merger\
```

5. Finally, to run the script, type the following and press Enter:

```
.\installer.ps1
```

6. Once the above is done, you can simply do
```
python path/to/source path/to/dest
```