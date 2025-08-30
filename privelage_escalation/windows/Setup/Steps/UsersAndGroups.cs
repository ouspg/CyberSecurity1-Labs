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

        // Make adminlab a local admin
        Shell.Run($"Add-LocalGroupMember -Group 'Administrators' -Member '{ctx.AdminUser}' -ErrorAction SilentlyContinue");
    }

    static void CreateLocalAccount(string username, string password)
    {
        Shell.Run($@"
            if (-not (Get-LocalUser -Name '{username}' -ErrorAction SilentlyContinue)) {{
                $p = ConvertTo-SecureString '{password}' -AsPlainText -Force
                New-LocalUser -Name '{username}' -Password $p -NoPasswordExpired -PasswordNeverExpires
            }}");
    }
}