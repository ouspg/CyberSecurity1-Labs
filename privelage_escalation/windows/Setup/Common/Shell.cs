using System.Management.Automation;

namespace Setup.Common;

public static class Shell
{
    public static void Run(string script)
    {
        using (PowerShell ps = PowerShell.Create())
        {
            ps.AddScript(script);
            var results = ps.Invoke();
            foreach (var r in results)
            {
                Console.WriteLine(r);
            }
        }
    }
}