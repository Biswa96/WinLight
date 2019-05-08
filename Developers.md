# How to find

Always use a virtual machine to test. DO NOT do this in your working system.

* Install any network capturing tool like WireShark, tcpdump, Fiddler etc.
Fiddler may be easier to understand here. Allow it to capture HTTPS traffic with
Tools > Options > HTTPS > Decrypt HTTPS traffic. Allow it to capture all Windows
programs in WinConfig > Exempt All > Save Changes. Do not close the window.

* Open Immersive Control Panel aka. Settings > Personalization > Lock Screen > Windows SpotLight.
This executes Background Task Host process under Microsoft Content Delivery Manager.

* Wait some time. When you see `arc.msn.com` in host column in Fiddler
stop it to capture further network packets. Copy the whole URL with Ctrl+U.
The URL will be something like this:

```
https://arc.msn.com/v3/Delivery/Placement?pubid=da63df93-3dbc-42ae-a505-b34988683ac7&pid=338387&
adm=2&w=1&h=1&wpx=1&hpx=1&fmt=json&cltp=app&dim=le&rafb=0&nct=1&pm=1&cfmt=text,image,poly&
sft=jpeg,png,gif&topt=1&poptin=0&localid=w:13BB0C2A-BF26-FAA1-30D3-96E3178DBE1A&ctry=US&
time=20190501T195244Z&lc=en-US&pl=en-US&idtp=mid&uid=f7e90ccd-a609-45c2-8543-cd5fb4597749&
aid=00000000-0000-0000-0000-000000000000&ua=WindowsShellClient%2F9.0.40929.0%20%28Windows%29&
asid=d33a80c001534bd3bcd52f6ed281dbe9&ctmode=MultiSession&arch=x64&cdm=1&cdmver=10.0.18890.1000&
devfam=Windows.Desktop&devform=Unknown&devosver=10.0.18890.1000&disphorzres=1366&dispsize=15.8&
dispvertres=654&isu=0&lo=2655&metered=false&nettype=ethernet&npid=sc-338387&oemName=innotek%20GmbH&
oemid=innotek%20GmbH&ossku=Professional&rver=2&sc-mode=0&smBiosDm=VirtualBox&tl=2&tsu=2655&
waasBldFlt=1&waasCfgExp=1&waasCfgSet=1&waasRetail=1&waasRing=1
```

* In the scripts, the link is shortened as
`https://arc.msn.com/v3/Delivery/Placement?&fmt=json&cdm=1&ctry=US&pid=338387`.

# Internals

* The `pid` field comes from `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\ContentDeliveryManager`
registry values. See the [sample registry file](ContentDeliveryManager.reg.ini).

* The URL string is constructed in `ContentManagementSDK` file. See these DLL files:

<!-- -->
    
    C:\Windows\System32\ContentDeliveryManager.Utilities.dll
    C:\Windows\SystemApps\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\ContentDeliveryManager.Background.dll
    C:\Windows\SystemApps\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\ContentManagementSDK.dll

## List of Subscription IDs

The same link also downloads Store Apps recommendations, Start Menu Tiles icon etc.
From `CreativeFramework::TargetedContent::GetAdUnitIdFromSubscriptionId` arrays:

|        Subscription ID         |  Internal Ad ID  |  Public Ad ID  |
|:------------------------------:|:----------------:|:--------------:|
|  ActionCenter                  |  310092           |  310091       |
|  ApiTest                       |  280812           |  280812       |
|  DynamicLayouts                |  314558           |  314559       |
|  MinuteZeroOffers              |  310094           |  310093       |
|  OobeOffers                    |  314566           |  314567       |
|  ShareAppSuggestions           |  280814           |  280815       |
|  SilentInstalledApps           |  202913           |  202914       |
|  StartSuggestions              |  338381           |  338388       |
|  PeopleAppSuggestions          |  314562           |  314563       |
|  OneDriveLocal                 |  280797           |  280811       |
|  OneDriveSync                  |  280817           |  280810       |
|  OneDriveDocuments             |  88000162         |  88000161     |
|  OneDriveDesktop               |  88000164         |  88000163     |
|  OneDrivePictures              |  88000166         |  88000165     |
|  LockScreen*                   |  338380           |  338387*      |
|  WindowsTip                    |  338382           |  338389       |
|  Settings                      |  338386           |  338393       |
|  Signals                       |  346480           |  346481       |
|  SettingsHome                  |  353697           |  353696       |
|  SettingsValueBanner           |  88000106         |  88000105     |
|  SettingsAccountsYourInfo      |  353695           |  353694       |
|  Timeline                      |  353699           |  353698       |
|  AppDefaultsEdgeEnlightenment  |  88000044         |  88000045     |



More to be discovered...

