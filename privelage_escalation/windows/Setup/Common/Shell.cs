using System.Management.Automation;
using System.Management.Automation.Runspaces;

namespace Setup.Common;

public static class Shell
{
    public static void Run(string script)
    {
        using var runspace = RunspaceFactory.CreateRunspace();
        runspace.Open();
        using var ps = PowerShell.Create();
        ps.Runspace = runspace;
        ps.AddScript(script);
        var results = ps.Invoke();
    }
}