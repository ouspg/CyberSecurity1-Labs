namespace Setup.Common;

public sealed class Context
{
    public string StudentUser = "student";
    public string DevUser = "Dev";
    public string SvcUser = "SVC";
    public string AdminUser= "Admin Lab";

    public string StudentUserPass = "password1";
    public string DevUserPass = "password1";
    public string SvcUserPass = "password1";
    public string AdminUserUserPass = "password1";

    public string ServiceName = "Acme Tools";
    public string ServiceDisplayName = "Acme Tools Service";

    public static Context LoadOrCreate()
    {
        return new Context();
    }

}