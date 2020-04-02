# SciDataTool
## Presentation
SciDataTool’s objective is to provide a **user-friendly, unified, flexible simulation framework for the multiphysic design and optimization of electrical machines and drives** based on open-source software.

It is meant to be used by researchers, R&D engineers and teachers in electrical engineering, both on standard topologies of electrical machines and on novel topologies (e.g. during a PhD work). An objective of Pyleecan is that every PhD student should start with Pyleecan instead of implementing (again) his own routines (e.g. coupling Scilab and Femm).

## Scope
The scope of the project is to simulate the following 2D radial flux machines:
* Surface, Surface Inset or Interior Permanent Magnet Synchronous Machines (SPMSM, SIPMSM, IPMSM) with inner or outer rotor
* Squirrel Cage Induction Machines (SCIM) and Doubly Fed Induction Machines (DFIM)

Then the project should address the following topologies:
* Direct Current Machines (DCM).
* Synchro Reluctant Machines (SyRM).
* Switched Reluctance Machines (SRM).

In the long-term basis Pyleecan will include 5 physics and several model for each (analytical, numerical...):
* Electrical
* Electromagnetics
* Heat Transfer
* Structural Mechanics
* Acoustics

## Origin and status of the project
EOMYS has started an open and non-commercial project named Pyleecan (Python Library for Electrical Engineering Computational Analysis). The starting code of Pyleecan is based on [MANATEE](https://eomys.com/produits/manatee/article/logiciel-manatee) (EOMYS commercial software) but Pyleecan is not an EOMYS only project: The initial maintainers includes other company and university. We are welcoming everyone that want to contribute.

The first model is complete and enables to compute the airgap flux density with FEMM on several machine type. The corresponding project are available in the [Validation folder](https://github.com/Eomys/pyleecan/tree/master/Tests/Validation) and can be used as example for your own simulation. More information on this coupling are available in the [first newsletter of pyleecan](https://mailchi.mp/51e852c72abd/pyleecan-news-website-and-first-simulations-coupling-with-femm?e=[UNIQID]). 

If you are interested by a topology or a specific model, you can [open an issue](https://github.com/Eomys/pyleecan/issues) on this Github repository to talk about it. We will gladly explain how to add it yourself or we will add it to the development list for further release.

## Documentation / Website
For now all the information on the project are available on [www.pyleecan.org](http://www.pyleecan.org). At this link, you will find the ICEM 2018 publication and the architecture documentation.

## Contact
You can contact us on Github by opening an issue (to request a feature, ask a question or report a bug) or at pyleecan@framalistes.org that redirect to all the maintainers.
