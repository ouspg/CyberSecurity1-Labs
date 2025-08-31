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
        string histContent = @$"
ls
pwd
whoami
ping 9.9.9.9
cmdkey /add:LAB-PC /user:{ctx.SvcUser} /pass:{ctx.SvcUserPass}
        ";
        File.AppendAllText(hist, histContent);
    }
}