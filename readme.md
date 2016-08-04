ElivsPy
====

ElvisPy is an configuration management tool that works as an extra layer over Fabric, that abstract some common tasks as python functions (resources) so to avoid writting static strings.

In future it would be cool to have other things like variable reading from json files so roles, environments and nodes can be defined.

#### TODO
These resources are missing

 * user
 * group
 * service
 * apt_package
 * chmod chown
 * mount
 * file
 * cron
 * bash
 * execute
 * tar, zip

Attributes loading
In order to have roles, environments and nodes as json files it's important
to know how the precedence of these attributes.
Read https://docs.chef.io/attributes.html#attribute-precedence for further info about attributes
A good place to setup these attributes would be on peanuts.py file. Maybe on run_peanuts method
