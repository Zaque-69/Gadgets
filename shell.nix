{ pkgs ? import <nixpkgs> {} } : 

pkgs.mkShell{
  nativeBuildInputs = with pkgs; [
    python311
    python311Packages.beautifulsoup4
    python311Packages.customtkinter
    python311Packages.keyboard
    python311Packages.moviepy
    python311Packages.opencv4
    python311Packages.pillow
    python311Packages.pyautogui
    python311Packages.pytube
    python311Packages.qrcode
    python311Packages.requests
    python311Packages.tkinter
  ];

  shellHook = ''
    echo "Shell prepared!"
  '';
}