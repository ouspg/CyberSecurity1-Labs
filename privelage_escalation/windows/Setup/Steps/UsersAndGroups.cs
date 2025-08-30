using Microsoft.PowerShell.Commands;
using Setup.Common;

namespace Setup.Steps;

public static class UsersAndGroups
{
    public static void Run(Context ctx)
    {
        Console.WriteLine("Creating Users and Groups");
        CreateLocalAccount(ctx.StudentUser, ctx.StudentUserPass);
        CreateLocalAccount(ctx.DevUser, ctx.DevUserPass);
        CreateLocalAccount(ctx.SvcUser, ctx.SvcUserPass);
        CreateLocalAccount(ctx.AdminUser, ctx.AdminUserUserPass);
        AddUsersToGroups(ctx);
        LoadUserProfiles(ctx.StudentUser, ctx.StudentUserPass);
        LoadUserProfiles(ctx.DevUser, ctx.DevUserPass);
        LoadUserProfiles(ctx.SvcUser, ctx.SvcUserPass);
        LoadUserProfiles(ctx.AdminUser, ctx.AdminUserUserPass);


    }

    static void CreateLocalAccount(string username, string password)
    {
        Shell.Run($@"
            $p = ConvertTo-SecureString '{password}' -AsPlainText -Force 
            New-LocalUser -Name '{username}' -Password $p -PasswordNeverExpires:$true
           ");

        // Enable User
        Shell.Run($@"
        Enable-LocalUser -Name {username}
        ");
    }

    static void AddUsersToGroups(Context ctx)
    {
        Shell.Run($"Add-LocalGroupMember -Group 'Administrators' -Member '{ctx.AdminUser}' -ErrorAction SilentlyContinue");
        Shell.Run($"Add-LocalGroupMember -Group 'Users' -Member '{ctx.StudentUser}' -ErrorAction SilentlyContinue");
        Shell.Run($"Add-LocalGroupMember -Group 'Users' -Member '{ctx.DevUser}' -ErrorAction SilentlyContinue");
        Shell.Run($"Add-LocalGroupMember -Group 'Users' -Member '{ctx.SvcUser}' -ErrorAction SilentlyContinue");
    }

    static void LoadUserProfiles(string username, string password)
    {
        Shell.Run(@$"
        $username = '{username}'
        $password = '{password}'
        $securePassword = ConvertTo-SecureString $password -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential ($username, $securePassword)
        Start-Process powershell.exe -ArgumentList 'whoami' -Credential $credential -LoadUserProfile -WorkingDirectory 'C:\Windows\System32'
        ");
    }
}