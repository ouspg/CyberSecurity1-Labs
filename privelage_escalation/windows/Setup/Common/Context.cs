namespace Setup.Common;

public sealed class Context
{
    public string StudentUser = "student";
    public string DevUser = "Developer";
    public string SvcUser = "SVC";
    public string AdminUser= "AdminLab";

    // TODO: update the passwords to make them less generic, could be random created during runtime
    public string StudentUserPass = "password1@#";
    public string DevUserPass = "password1@#";
    public string SvcUserPass = "password1@#";
    public string AdminUserUserPass = "password1@#";

    public string ServiceName = "Acme Tools";
    public string ServiceDisplayName = "Acme Tools Service";

    public static Context LoadOrCreate()
    {
        return new Context();
    }

}