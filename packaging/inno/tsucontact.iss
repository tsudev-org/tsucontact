; Bộ cài Windows của Tsu Contact (Inno Setup 6) - đóng gói thư mục PyInstaller onedir (TSU_ONEDIR=1).
; Lý do có bộ cài: PyInstaller onefile bị phần mềm diệt virus học máy báo nhầm (DISTRIBUTION_TRUST mục 3,
; ISS-20261121-2340-3857). Cài theo người dùng, KHÔNG cần quyền quản trị; có lối tắt Start Menu và trình gỡ cài đặt.
; Dựng: iscc /DAppVersion=<v> /DSourceDir=<dist\tsucontact> /DOutputBase=<tên tệp không đuôi> /O<thư mục ra> tsucontact.iss

#ifndef AppVersion
  #error Thiếu /DAppVersion
#endif
#ifndef SourceDir
  #error Thiếu /DSourceDir
#endif
#ifndef Compression
  #define Compression "lzma2/max"
#endif
#ifndef Solid
  #define Solid "yes"
#endif
#ifndef OutputBase
  #error Thiếu /DOutputBase
#endif

[Setup]
; AppId cố định - KHÔNG đổi, đổi là bản cài mới không nhận ra bản cũ để nâng cấp/gỡ.
AppId={{6F1C2B7E-4A0D-4E5B-9C3A-7D2E1B8F4C60}
AppName=Tsu Contact
AppVersion={#AppVersion}
AppVerName=Tsu Contact {#AppVersion}
AppPublisher=TsuDEV
AppPublisherURL=https://tsudev.com
AppSupportURL=https://contact.tsudev.com
AppUpdatesURL=https://github.com/tsudev-org/tsucontact/releases
AppCopyright=Copyright (c) 2026 TsuDEV
VersionInfoVersion={#AppVersion}.0
VersionInfoCompany=TsuDEV
VersionInfoDescription=Tsu Contact - bộ cài
VersionInfoProductName=Tsu Contact
DefaultDirName={autopf}\Tsu Contact
DefaultGroupName=Tsu Contact
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
MinVersion=10.0
LicenseFile=..\..\LICENSE
SetupIconFile=..\..\assets\icons\app.ico
UninstallDisplayIcon={app}\tsucontact.exe
UninstallDisplayName=Tsu Contact
OutputBaseFilename={#OutputBase}
Compression={#Compression}
SolidCompression={#Solid}
WizardStyle=modern
CloseApplications=yes

[Languages]
Name: "en"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "{#SourceDir}\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\Tsu Contact"; Filename: "{app}\tsucontact.exe"
Name: "{autodesktop}\Tsu Contact"; Filename: "{app}\tsucontact.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\tsucontact.exe"; Description: "{cm:LaunchProgram,Tsu Contact}"; Flags: nowait postinstall skipifsilent
