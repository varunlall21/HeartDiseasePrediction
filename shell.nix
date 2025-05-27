{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.flask
    pkgs.python3Packages.pandas
    pkgs.python3Packages.joblib
    pkgs.python3Packages.scikit-learn
  ];
}