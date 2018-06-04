# Simple Travis-CI Build Configurations

This is a repository of basic Travis-CI build configurations `*.yml` for simple projects.
These are a good starting point for building a `*.yml` build configuration file
for your project.


## Configurations

[iOS / MacOSX (Swift / Objective-c)](#ios--macosx)



## iOS / MacOSX

The sample iOS `ios.travis.yml` file is configured to use XCPretty by default to sanitize the
build output. It also contains the commands necessary for basic projects that are implementing cocoapods.
The `WORKSPACE`, `SCHEME`, and `DESTINATION` environment variables need to be updated with the correct ones from your project. `WORKSPACE` and its argument in the `xcodebuild` command can be removed if your project
does not make use of it.

```
# references:

# Travis-CI - Environment Variables : https://docs.travis-ci.com/user/environment-variables/
# Travis-CI - Objective-C / Swift : https://docs.travis-ci.com/user/languages/objective-c/
# XCPretty : https://github.com/supermarin/xcpretty#usage

osx_image: xcode9.3
language: objective-c

# CocoaPods
# cache: cocoapods
# podfile: Example/Podfile

before_install:
  - WORKSPACE="Example/Example.xcworkspace"
  - SCHEME="Example"
  - DESTINATION="platform=iOS Simulator,name=iPhone 8,OS=11.3"

  # Debug Commands
  - ls -R                                 # Current file tree
  - xcodebuild -list                        # List avaiable versions/simulators
  - xcodebuild -workspace $WORKSPACE -list  # List Schemes

  # CocoaPods
  - gem install cocoapods --quiet # Since Travis is not always on latest version

before_script:
  - rvm get head
  - gem install xcpretty

  # CocoaPods
  # - pod install
  # - pod install --project-directory=Example #For non-standard Podfile locations

script:

  - |
    set -o pipefail && \
    xcodebuild test \
    -enableCodeCoverage YES \
    -workspace $WORKSPACE \
    -scheme $SCHEME \
    -destination $DESTINATION \
    ONLY_ACTIVE_ARCH=NO \
    CODE_SIGN_IDENTITY=\"\" \
    CODE_SIGNING_REQUIRED=NO | \
    xcpretty
  - pod lib lint # --allow-warnings

  ```
