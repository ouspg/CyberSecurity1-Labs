namespace Setup.Common;

public sealed class Context
{
    public string StudentUser = "student";
    public string DevUser = "Dev";
    public string SvcUser = "SVC";
    public string AdminLab = "Admin Lab";

    public string StudentUserPass = Environment.GetEnvironmentVariable("ACCOUNT_A_PASS");
    public string DevUserPass = Environment.GetEnvironmentVariable("ACCOUNT_B_PASS");
    public string SvcUserPass = Environment.GetEnvironmentVariable("ACCOUNT_C_PASS");
    public string AdminLabUserPass = Environment.GetEnvironmentVariable("ACCOUNT_D_PASS");

    public static Context LoadOrCreate()
    {
        return new Context();
    }

}