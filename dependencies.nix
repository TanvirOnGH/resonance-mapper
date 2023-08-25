# Reference: <https://nixos.wiki/wiki/Python>
{pkgs ? import <nixpkgs> {}}: let
  deps = ps:
    with ps; [
      pyaudio
      numpy
    ];
  python = pkgs.python3.withPackages deps;
in
  python.env
