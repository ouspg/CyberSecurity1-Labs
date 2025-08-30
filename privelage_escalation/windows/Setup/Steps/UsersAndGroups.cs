using Setup.Common;

namespace Setup.Steps;

public static class UsersAndGroups
{
    public static void Run(Context ctx)
    {
        Console.WriteLine("Creating Users and Groups");
        CreateLocalAccount(ctx.StudentUser, ctx.StudentUserPass);
    }

    static void CreateLocalAccount(string username, string password)
    {
        Shell.Run("pwd");
    }
}