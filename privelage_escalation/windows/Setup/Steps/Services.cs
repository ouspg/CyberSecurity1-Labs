using Setup.Common;

namespace Setup.Steps;

public static class Services
{
    public static void Run(Context ctx)
    {
        Console.WriteLine("Setting up misconfigured Services...");

        var svcDir = $@"C:\Users\{ctx.SvcUser}\Lab Service";
        Directory.CreateDirectory(svcDir);

        // Replace this with some beign binary
        var svcExe = Path.Combine(svcDir, "service.exe");
        File.Copy(Path.Combine(Environment.SystemDirectory, "cmd.exe"), svcExe, true);

        // Create service
        // Shell.Run(@$"
        // sc create {ctx.ServiceName} binPath= {svcExe} start= auto DisplayName= {ctx.ServiceDisplayName} obj= {ctx.SvcUser} password= {ctx.SvcUserPass}
        // ");
        Shell.Run(@$"
        $username = '$env:COMPUTERNAME\{ctx.AdminUser}'
$password = '{ctx.AdminUserUserPass}'
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($username, $securePassword)
New-Service -Name {ctx.ServiceName} `
            -BinaryPathName '{svcExe}' `
            -DisplayName '{ctx.ServiceDisplayName}' `
            -Description 'Service running as {ctx.AdminUser} user' `
            -StartupType Manual `
            -Credential $credential
        ");
    }
}