using Setup.Common;
using Setup.Steps;

namespace Setup;

class Program
{
    static void Main(string[] args)
    {
        var ctx = Context.LoadOrCreate();
        UsersAndGroups.Run(ctx);
        CredSeeding.Run(ctx);
        // Services.Run();
        // Privelages.Run();

    }
}
