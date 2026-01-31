{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = with pkgs; [ git ruff zlib sqlite ];

  languages.python = {
    enable = true;
    package = pkgs.python3;
    venv.enable = true;
    venv.requirements = ''
      pybaseball
      pandas
    '';

  };

  #if you want R, uncomment this next line
  # languages.r.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
