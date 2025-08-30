using Setup.Common;

namespace Setup.Steps;

public static class CredSeeding
{
    public static void Run(Context ctx)
    {
        // Password in PS history
        Console.WriteLine("Seeding Credentials");
        var hist = $@"C:\Users\{ctx.StudentUser}\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt";
        Directory.CreateDirectory(Path.GetDirectoryName(hist)!);
        File.AppendAllText(hist, $"cmdkey /add:LAB-PC /user:{ctx.StudentUser} /pass:{ctx.StudentUserPass}");

        // Saved credentials
        Shell.Run($"runas /user:{ctx.DevUser} /pass:{ctx.DevUserPass} 'cmdkey /add:LAB-PC /user:{ctx.SvcUser} /pass:{ctx.SvcUserPass}'")
    }
}