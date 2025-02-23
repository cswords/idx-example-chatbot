# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python3
    pkgs.python311Packages.pip
  ];
  # Sets environment variables in the workspace
  env = {
    PORT = "9080";
  };
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      "ms-python.python"
    ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        create-venv = ''
          python -m venv .venv
          source .venv/bin/activate
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        '';
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "main.py" ];
      };
      # To run something each time the workspace is (re)started, use the `onStart` hook
    };
    # Enable previews and customize configuration
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["./start.sh"];
          env = {
            PORT = "$PORT";
          };
          manager = "web";
        };
      };
    };
  };
}
