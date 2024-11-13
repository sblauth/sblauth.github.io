Publications
============



Submitted Articles / Preprints
------------------------------


#.  | **Enforcing Mesh Quality Constraints in Shape Optimization with a Gradient Projection Method**
    | *with Christian Leithäuser*
    | submitted, 2024

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                For the numerical solution of shape optimization problems, particularly those constrained by partial differential equations (PDEs), the quality of the underlying mesh is of utmost importance. Particularly when investigating complex geometries, the mesh quality tends to deteriorate over the course of a shape optimization so that either the optimization comes to a halt or an expensive remeshing operation must be performed before the optimization can be continued. In this paper, we present a novel, semi-discrete approach for enforcing a minimum mesh quality in shape optimization. Our approach is based on Rosen's gradient projection method, which incorporates mesh quality constraints into the shape optimization problem. The proposed constraints bound the angles of triangular and solid angles of tetrahedral mesh cells and, thus, also bound the quality of these mesh cells. The method treats these constraints by projecting the search direction to the linear subspace of the currently active constraints. Additionally, only slight modifications to the usual line search procedure are required to ensure the feasibility of the method. We present our method for two- and three-dimensional simplicial meshes. We investigate the proposed approach numerically for the drag minimization of an obstacle in a two-dimensional flow and for the large-scale, three-dimensional optimization of a structured packing used in a distillation column. Our results show that the proposed method is indeed capable of guaranteeing a minimum mesh quality for both academic examples and challenging industrial applications. Particularly, our approach allows the shape optimization of extremely complex structures while ensuring that the mesh quality does not deteriorate.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Blauth2024Enforcing,
                      author        = {Sebastian Blauth and Christian Leithäuser},
                      title         = {{Enforcing Mesh Quality Constraints in Shape Optimization with a Gradient Projection Method}},
                      year          = {2024},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Enforcing Mesh Quality Constraints in Shape Optimization with a Gradient Projection Method
                    Sebastian Blauth and Christian Leithäuser
                    Preprint, 2024



#.  | **A Novel Deflation Approach for Topology Optimization and Application for Optimization of Bipolar Plates of Electrolysis Cells**
    | *with Leon Baeck, Christian Leithäuser, René Pinnau, and Kevin Sturm*
    | submitted, 2024
    | :bdg-link-secondary-line:`preprint: arXiv:2406.17491 <https://arxiv.org/abs/2406.17491>`
   
    .. dropdown:: Additional resources
        :icon: three-bars
      
        .. tab-set::
      
            .. tab-item:: Abstract
         
                Topology optimization problems usually feature multiple local minimizers. To guarantee convergence to local minimizers that perform best globally or to find local solutions that are desirable for practical applications due to easy manufacturability or aesthetic designs, it is important to compute multiple local minimizers of topology optimization problems. Existing methods typically rely on Newton-type solvers during the optimization process, which makes them unsuitable for sensitivity-based topology optimization. In this paper, we introduce a novel deflation approach to systematically find multiple local minimizers of general topology optimization problems. The approach is based on a penalization of previously found local solutions in the objective. We validate our approach on the so-called two-pipes five-holes example. Finally, we introduce a model for the topology optimization of bipolar plates of hydrogen electrolysis cells and demonstrate that our deflation approach enables the discovery of novel designs for such plates.
         
            .. tab-item:: BibTeX citation
         
                .. code-block:: bibtex
         
                    @Article{Baeck2024Novel,
                      author        = {Leon Baeck and Sebastian Blauth and Christian Leithäuser and René Pinnau and Kevin Sturm},
                      title         = {{A Novel Deflation Approach for Topology Optimization and Application for Optimization of Bipolar Plates of Electrolysis Cells}},
                      year          = {2024},
                      archiveprefix = {arXiv},
                      eprint        = {2406.17491},
                      primaryclass  = {math.OC},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    A Novel Deflation Approach for Topology Optimization and Application for Optimization of Bipolar Plates of Electrolysis Cells
                    Leon Baeck, Sebastian Blauth, Christian Leithäuser, René Pinnau, and Kevin Sturm
                    Preprint on arXiv, 2024
                    https://arxiv.org/abs/2406.17491



#.  | **Computing Multiple Local Minimizers for the Topology Optimization of Bipolar Plates in Electrolysis Cells**
    | *with Leon Baeck, Christian Leithäuser, René Pinnau, Kevin Sturm*
    | submitted, 2024
    | :bdg-link-secondary-line:`preprint: arXiv:2401.09230 <https://arxiv.org/abs/2401.09230>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                In this paper we consider the topology optimization for a bipolar plate of a hydrogen electrolysis cell. We use the Borvall-Petersson model to describe the fluid flow and derive a criterion for a uniform flow distribution in the bipolar plate. Furthermore, we introduce a novel deflation approach to compute multiple local minimizers of topology optimization problems. The approach is based on a penalty method that discourages convergence towards previously found solutions. Finally, we demonstrate this technique on the topology optimization for bipolar plates and show that multiple distinct local solutions can be found.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Misc{Baeck2024Computing,
                      author        = {Leon Baeck and Sebastian Blauth and Christian Leithäuser and René Pinnau and Kevin Sturm},
                      title         = {{Computing Multiple Local Minimizers for the Topology Optimization of Bipolar Plates in Electrolysis Cells}},
                      year          = {2024},
                      archiveprefix = {arXiv},
                      eprint        = {2401.09230},
                      primaryclass  = {math.OC},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Computing Multiple Local Minimizers for the Topology Optimization of Bipolar Plates in Electrolysis Cells
                    Leon Baeck, Sebastian Blauth, Christian Leithäuser, René Pinnau, and Kevin Sturm
                    Preprint on arXiv, 2024
                    https://arxiv.org/abs/2401.09230



Articles in Peer-Reviewed Journals
----------------------------------



#.  | **CFD-based shape optimization of structured packings for enhancing separation efficiency in distillation**
    | *with Dennis Stucke, Mohamed Adel Ashour, Johannes Schnebele, Thomas Grützner, and Christian Leithäuser*
    | Chemical Engineering Science 302, 2025
    | :bdg-link-primary-line:`doi: 10.1016/j.ces.2024.120803 <https://doi.org/10.1016/j.ces.2024.120803>` :bdg-link-secondary-line:`preprint: arXiv:2407.11099 <https://arxiv.org/abs/2407.11099>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Free-form shape optimization techniques are investigated to improve the separation efficiency of structured packings in laboratory-scale distillation columns. A simplified simulation model based on computational fluid dynamics (CFD) for the mass transfer in the distillation column is used and a corresponding shape optimization problem is formulated. The goal of the optimization is to increase the mass transfer in the column by changing the packing's shape, which has been previously used as criterion for increasing the separation efficiency of the column. The computational shape optimization yields promising results, with an increased mass transfer of nearly 20 %. For validation, the resulting optimized shape is additively manufactured using 3D-printing and investigated experimentally. The experimental results are in good agreement with the performance improvement predicted by the computational model, yielding an increase in separation efficiency of around 20 %.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Blauth2025CFD,
                      author  = {Sebastian Blauth and Dennis Stucke and Mohamed Adel Ashour and Johannes Schnebele and Thomas Grützner and Christian Leithäuser},
                      journal = {Chemical Engineering Science},
                      title   = {{CFD-based shape optimization of structured packings for enhancing separation efficiency in distillation}},
                      year    = {2025},
                      issn    = {0009-2509},
                      volume  = {302},
                      doi     = {10.1016/j.ces.2024.120803},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    CFD-based shape optimization of structured packings for enhancing separation efficiency in distillation
                    Sebastian Blauth, Dennis Stucke, Mohamed Adel Ashour, Johannes Schnebele, Thomas Grützner, and Christian Leithäuser
                    Chemical Engineering Science 302, 2025
                    https://doi.org/10.1016/j.ces.2024.120803


#.  | **Multi-Criteria Shape Optimization of Flow Fields for Electrochemical Cells**
    | *with Marco Baldan, Sebastian Osterroth, Christian Leithäuser, Ulf-Peter Apfel, Julian Kleinhaus, Kevinjeorjios Pellumbi, Daniel Siegmund, Konrad Steiner, and Michael Bortz*
    | Chemie Ingenieur Technik 96(5), 2024
    | :bdg-link-primary-line:`doi: 10.1002/cite.202300161 <https://doi.org/10.1002/cite.202300161>` :bdg-link-secondary-line:`preprint: arXiv:2309.13958 <https://arxiv.org/abs/2309.13958>` :bdg-link-info-line:`on the web <https://www.itwm.fraunhofer.de/en/fields-of-application/renewable-energy-sustainability/electrochemical-cells.html>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                We consider the shape optimization of flow fields for electrochemical cells. Our goal is to improve the cell by modifying the shape of its flow field. To do so, we introduce simulation models of the flow field with and without the porous transport layer. The latter is less detailed and used for shape optimization, whereas the former is used to validate our obtained results. We propose three objective functions based on the uniformity of the flow and residence time as well as the wall shear stress. After considering the respective optimization problems separately, we use techniques from multi-criteria optimization to treat the conflicting objective functions systematically. Our results highlight the potential of our approach for generating novel flow field designs for electrochemical cells.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Blauth2024Multi,
                      author   = {Blauth, Sebastian and Baldan, Marco and Osterroth, Sebastian and Leithäuser, Christian and Apfel, Ulf-Peter and Kleinhaus, Julian and Pellumbi, Kevinjeorjios and Siegmund, Daniel and Steiner, Konrad and Bortz, Michael},
                      journal  = {Chemie Ingenieur Technik},
                      title    = {{Multi-Criteria Shape Optimization of Flow Fields for Electrochemical Cells}},
                      year     = {2024},
                      number   = {5},
                      pages    = {616-626},
                      volume   = {96},
                      doi      = {10.1002/cite.202300161},
                      keywords = {CFD, Electrochemical cell, Multi-criteria optimization, Numerical optimization, Shape optimization},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Multi-Criteria Shape Optimization of Flow Fields for Electrochemical Cells
                    Sebastian Blauth, Marco Baldan, Sebastian Osterroth, Christian Leithäuser, Ulf-Peter Apfel, Julian Kleinhaus, Kevinjeorjios Pellumbi, Daniel Siegmund, Konrad Steiner, and Michael Bortz
                    Chemie Ingenieur Technik 96(5), 2024
                    https://doi.org/10.1002/cite.202300161



#.  | **Multi-Scale Simulation of a Novel Integrated Reactor for Hydrogen Production by Ammonia Decomposition**
    | *with Julie Damay, Sebastian Osterroth, Christian Leithäuser, Christian Hofmann, Gunther Kolb, Martin Wichert, Konrad Steiner, and Michael Bortz*
    | Chemie Ingenieur Technik 96(5), 2024
    | :bdg-link-primary-line:`doi: 10.1002/cite.202300166 <https://doi.org/10.1002/cite.202300166>` :bdg-link-secondary-line:`preprint: hal-04265601 <https://hal.science/hal-04265601>` :bdg-link-info-line:`on the web <https://www.itwm.fraunhofer.de/en/fields-of-application/renewable-energy-sustainability/ammonpaktor.html>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                A novel reactor concept for ammonia decomposition utilizing tail gas from a purification unit as heat supply is presented. The designed micro-structured reactor integrates both endothermic ammonia decomposition and exothermic tail gas combustion. The reactor and corresponding process are simulated using a mathematical multi-scale model, which combines the results of multiple detailed computational fluid dynamics simulations into a fast surrogate model. The latter is coupled with a process simulation software via a so-called container to simulate the entire process. The efficiency of the presented reactor concept is determined and benefits over alternative approaches are highlighted.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Blauth2024Multia,
                      author   = {Blauth, Sebastian and Damay, Julie and Osterroth, Sebastian and Leithäuser, Christian and Hofmann, Christian and Kolb, Gunther and Wichert, Martin and Steiner, Konrad and Bortz, Michael},
                      journal  = {Chemie Ingenieur Technik},
                      title    = {{Multi-Scale Simulation of a Novel Integrated Reactor for Hydrogen Production by Ammonia Decomposition}},
                      year     = {2024},
                      number   = {5},
                      pages    = {627-641},
                      volume   = {96},
                      doi      = {10.1002/cite.202300166},
                      keywords = {Ammonia decomposition, Computational fluid dynamics simulation, Hydrogen production, Multi-scale simulation, Process simulation},
                    }


            .. tab-item:: Plain text citation

                .. code-block:: text

                    Multi-Scale Simulation of a Novel Integrated Reactor for Hydrogen Production by Ammonia Decomposition
                    Sebastian Blauth, Julie Damay, Sebastian Osterroth, Christian Leithäuser, Christian Hofmann, Gunther Kolb, Martin Wichert, Konrad Steiner, and Michael Bortz
                    Chemie Ingenieur Technik 96(5), 2024
                    https://doi.org/10.1002/cite.202300166



#.  | **Continuous Synthesis of Diazo Acetonitrile: From Experiments to Physical and Grey-Box Modeling**
    | *with Marco Baldan, Dušan Bošković, Christian Leithäuser, Alexander Mendl, Ligia Radulescu, Maud Schwarzer, Heinrich Wegner, and Michael Bortz*
    | Chemie Ingenieur Technik 96(5), 2024
    | :bdg-link-primary-line:`doi: 10.1002/cite.202300191 <https://doi.org/10.1002/cite.202300191>` :bdg-link-secondary-line:`preprint: arXiv:2310.09315 <https://arxiv.org/abs/2310.09315>` :bdg-link-info-line:`on the web <https://www.shapid.fraunhofer.de/en.html>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Diazo compounds are gathering interest for their potential in promoting greener synthesis routes. We investigate, at a lab-scale, the continuous synthesis of diazo acetonitrile (DAN) using a micro-structured flow reactor and a flow reaction calorimeter. Data concerning DAN formation in the former, and relative to reaction heat and gas flow rate in the latter, are collected. We present both a physical and a grey-box simulation model, both of which are calibrated to our measurements. Both models provide valuable insights into the DAN synthesis. The grey-box approach is useful to incorporate the complex chemical reaction pathways for DAN synthesis and decomposition that are currently hard to address with the physical model.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Baldan2024Continuous,
                      author   = {Baldan, Marco and Blauth, Sebastian and Bošković, Dušan and Leithäuser, Christian and Mendl, Alexander and Radulescu, Ligia and Schwarzer, Maud and Wegner, Heinrich and Bortz, Michael},
                      journal  = {Chemie Ingenieur Technik},
                      title    = {{Continuous Synthesis of Diazo Acetonitrile: From Experiments to Physical and Grey-Box Modeling}},
                      year     = {2024},
                      number   = {5},
                      pages    = {658-670},
                      volume   = {96},
                      doi      = {10.1002/cite.202300191},
                      keywords = {Continuous flow chemistry, Diazo acetonitrile, Green chemistry, Grey-box modeling, Parameter identification},
                    }


            .. tab-item:: Plain text citation

                .. code-block:: text

                    Continuous Synthesis of Diazo Acetonitrile: From Experiments to Physical and Grey-Box Modeling
                    Marco Baldan, Sebastian Blauth, Dušan Bošković, Christian Leithäuser, Alexander Mendl, Ligia Radulescu, Maud Schwarzer, Heinrich Wegner, and Michael Bortz
                    Chemie Ingenieur Technik 96(5), 2024
                    https://doi.org/10.1002/cite.202300191



#.  | **Version 2.0 - cashocs: A Computational, Adjoint-Based Shape Optimization and Optimal Control Software**
    | SoftwareX 24, 2023
    | :bdg-link-primary-line:`doi: 10.1016/j.softx.2023.101577 <https://doi.org/10.1016/j.softx.2023.101577>` :bdg-link-secondary-line:`preprint: arXiv:2306.09828 <https://arxiv.org/abs/2306.09828>` :bdg-link-success-line:`code on GitHub <https://github.com/sblauth/cashocs>` :bdg-link-info-line:`on the web <https://www.itwm.fraunhofer.de/en/departments/tv/products-and-services/shape-optimization-cashocs-software.html>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                In this paper, we present version 2.0 of cashocs. Our software automates the solution of PDE constrained optimization problems for design optimization and optimal control. Since its inception, many new features and useful tools have been added to cashocs, making it even more flexible and efficient. The most significant additions are a framework for space mapping, the ability to solve topology optimization problems with a level-set approach, the support for parallelism via MPI, and the ability to handle additional (state) constraints. In this software update, we describe the key additions to cashocs, which is now even better-suited for solving complex PDE constrained optimization problems.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Blauth2023Version,
                      author   = {Sebastian Blauth},
                      journal  = {SoftwareX},
                      title    = {{Version 2.0 - cashocs: A Computational, Adjoint-Based Shape Optimization and Optimal Control Software}},
                      year     = {2023},
                      issn     = {2352-7110},
                      pages    = {101577},
                      volume   = {24},
                      doi      = {10.1016/j.softx.2023.101577},
                      keywords = {PDE constrained optimization, Shape optimization, Topology optimization, Space mapping},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Version 2.0 - cashocs: A Computational, Adjoint-Based Shape Optimization and Optimal Control Software
                    Sebastian Blauth
                    SoftwareX 24, 2024
                    https://doi.org/10.1016/j.softx.2023.101577



#.  | **Quasi-Newton methods for topology optimization using a level-set method**
    | *with Kevin Sturm*
    | Structural and Multidisciplinary Optimization 66(9), 2023
    | :bdg-link-primary-line:`doi: 10.1007/s00158-023-03653-2 <https://doi.org/10.1007/s00158-023-03653-2>` :bdg-link-secondary-line:`preprint: arXiv:2303.15070 <https://arxiv.org/abs/2303.15070>` :bdg-link-success-line:`code on GitHub <https://github.com/sblauth/quasi_newton_methods_for_topology_optimization>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                The ability to efficiently solve topology optimization problems is of great importance for many practical applications. Hence, there is a demand for efficient solution algorithms. In this paper, we propose novel quasi-Newton methods for solving PDE-constrained topology optimization problems. Our approach is based on and extends the popular solution algorithm of Amstutz and Andrä (A new algorithm for topology optimization using a level-set method, Journal of Computational Physics, 216, 2006). To do so, we introduce a new perspective on the commonly used evolution equation for the level-set method, which allows us to derive our quasi-Newton methods for topology optimization. We investigate the performance of the proposed methods numerically for the following examples: Inverse topology optimization problems constrained by linear and semilinear elliptic Poisson problems, compliance minimization in linear elasticity, and the optimization of fluids in Navier-Stokes flow, where we compare them to current state-of-the-art methods. Our results show that the proposed solution algorithms significantly outperform the other considered methods: They require substantially less iterations to find a optimizer while demanding only slightly more resources per iteration. This shows that our proposed methods are highly attractive solution methods in the field of topology optimization.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2023Quasi,
                      author   = {Blauth, Sebastian and Sturm, Kevin},
                      journal  = {Struct. Multidiscip. Optim.},
                      title    = {{Quasi-Newton methods for topology optimization using a level-set method}},
                      year     = {2023},
                      issn     = {1615-147X,1615-1488},
                      number   = {9},
                      pages    = {203},
                      volume   = {66},
                      doi      = {10.1007/s00158-023-03653-2},
                      fjournal = {Structural and Multidisciplinary Optimization},
                      mrclass  = {99-06},
                      mrnumber = {4635978},
                    }


            .. tab-item:: Plain text citation

                .. code-block:: text

                    Quasi-Newton methods for topology optimization using a level-set method
                    Sebastian Blauth and Kevin Sturm
                    Structural and Multidisciplinary Optimization 66(9), 2023
                    https://doi.org/10.1007/s00158-023-03653-2



#.  | **Space Mapping for PDE Constrained Shape Optimization**
    | SIAM Journal on Optimization 33(3), 2023
    | :bdg-link-primary-line:`doi: 10.1137/22M1515665 <https://doi.org/10.1137/22M1515665>` :bdg-link-secondary-line:`preprint: arXiv:2208.05747 <https://arxiv.org/abs/2208.05747>` :bdg-link-success-line:`code on GitHub <https://github.com/sblauth/space_mapping_shape_optimization>`
   
    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                The space mapping technique is used to efficiently solve complex optimization problems. It combines the accuracy of fine model simulations with the speed of coarse model optimizations to approximate the solution of the fine model optimization problem. In this paper, we propose novel space mapping methods for solving shape optimization problems constrained by partial differential equations (PDEs). We present the methods in a Riemannian setting based on Steklov-Poincaré-type metrics and discuss their numerical discretization and implementation. We investigate the numerical performance of the space mapping methods on several model problems. Our numerical results highlight the methods' great efficiency for solving complex shape optimization problems.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Blauth2023Space,
                      author   = {Blauth, Sebastian},
                      journal  = {SIAM J. Optim.},
                      title    = {{Space Mapping for PDE Constrained Shape Optimization}},
                      year     = {2023},
                      issn     = {1052-6234,1095-7189},
                      number   = {3},
                      pages    = {1707--1733},
                      volume   = {33},
                      doi      = {10.1137/22M1515665},
                      fjournal = {SIAM Journal on Optimization},
                      mrclass  = {49Q10 (35Q93 49M41 65K05)},
                      mrnumber = {4622415},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Space Mapping for PDE Constrained Shape Optimization
                    Sebastian Blauth
                    SIAM Journal on Optimization 33(3), 2023
                    https://doi.org/10.1137/22M1515665



#.  | **Asymptotic analysis for optimal control of the Cattaneo model**
    | *with René Pinnau, Matthias Andres, and Claudia Totzeck*
    | Journal of Mathematical Analysis and Applications 527(1), 2023
    | :bdg-link-primary-line:`doi: 10.1016/j.jmaa.2023.127375 <https://doi.org/10.1016/j.jmaa.2023.127375>` :bdg-link-secondary-line:`preprint: arXiv:2302.07630 <https://arxiv.org/abs/2302.07630>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                We consider an optimal control problem with tracking-type cost functional constrained by the Cattaneo equation, which is a well-known model for delayed heat transfer. In particular, we are interested the asymptotic behaviour of the optimal control problems for a vanishing delay time :math:`\tau \rightarrow 0`. First, we show the convergence of solutions of the Cattaneo equation to the ones of the heat equation. Assuming the same right-hand side and compatible initial conditions for the equations, we prove a linear convergence rate. Moreover, we show linear convergence of the optimal states and optimal controls for the Cattaneo equation towards the ones for the heat equation. We present numerical results for both, the forward and the optimal control problem confirming these linear convergence rates.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2023Asymptotic,
                      author   = {Blauth, Sebastian and Pinnau, Ren\'{e} and Andres, Matthias and Totzeck, Claudia},
                      journal  = {J. Math. Anal. Appl.},
                      title    = {{Asymptotic analysis for optimal control of the Cattaneo model}},
                      year     = {2023},
                      issn     = {0022-247X,1096-0813},
                      number   = {1},
                      pages    = {Paper No. 127375, 21},
                      volume   = {527},
                      doi      = {10.1016/j.jmaa.2023.127375},
                      fjournal = {Journal of Mathematical Analysis and Applications},
                      mrclass  = {49J20 (35Q49 49J45 65M60)},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Asymptotic analysis for optimal control of the Cattaneo model
                    Sebastian Blauth, René Pinnau, Matthias Andres, and Claudia Totzeck
                    Journal of Mathematical Analysis and Applications 527(1), 2023
                    https://doi.org/10.1016/j.jmaa.2023.127375



#.  | **Validating a simulation model for laser-induced thermotherapy using MR thermometry**
    | *with Frank Hübner, Christian Leithäuser, Roland Schreiner, Norbert Siedow, and Thomas Vogl*
    | International Journal of Hyperthermia 39(1), 2022
    | :bdg-link-primary-line:`doi: 10.1080/02656736.2022.2129102 <https://doi.org/10.1080/02656736.2022.2129102>` :bdg-link-secondary-line:`preprint: arXiv:2204.07502 <https://arxiv.org/abs/2204.07502>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Objectives

                We want to investigate whether temperature measurements obtained from MR thermometry are accurate and reliable enough to aid the development and validation of simulation models for Laser-induced interstitial thermotherapy (LITT).

                Methods

                Laser-induced interstitial thermotherapy (LITT) is applied to ex-vivo porcine livers. An artificial blood vessel is used to study the cooling effect of large blood vessels in proximity to the ablation zone. The experimental setting is simulated using a model based on partial differential equations (PDEs) for temperature, radiation, and tissue damage. The simulated temperature distributions are compared to temperature data obtained from MR thermometry.

                Results

                The overall agreement between measurement and simulation is good for two of our four test cases, while for the remaining cases drift problems with the thermometry data have been an issue. At higher temperatures local deviations between simulation and measurement occur in close proximity to the laser applicator and the vessel. This suggests that certain aspects of the model may need some refinement.

                Conclusion

                Thermometry data is well-suited for aiding the development of simulations models since it shows where refinements are necessary and enables the validation of such models.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Huebner2022Validating,
                      author    = {Frank Hübner and Sebastian Blauth and Christian Leithäuser and Roland Schreiner and Norbert Siedow and Thomas J. Vogl},
                      journal   = {International Journal of Hyperthermia},
                      title     = {{Validating a simulation model for laser-induced thermotherapy using MR thermometry}},
                      year      = {2022},
                      number    = {1},
                      pages     = {1315-1326},
                      volume    = {39},
                      doi       = {10.1080/02656736.2022.2129102},
                      publisher = {Taylor & Francis},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Validating a simulation model for laser-induced thermotherapy using MR thermometry
                    Frank Hübner, Sebastian Blauth, Christian Leithäuser, Roland Schreiner, Norbert Siedow, and Thomas J. Vogl
                    International Journal of Hyperthermia 39(1), 2022
                    https://doi.org/10.1080/02656736.2022.2129102



#.  | **Nonlinear Conjugate Gradient Methods for PDE Constrained Shape Optimization Based on Steklov-Poincaré-Type Metrics**
    | SIAM Journal on Optimization 31(3), 2021
    | :bdg-link-primary-line:`doi: 10.1137/20M1367738 <https://doi.org/10.1137/20M1367738>` :bdg-link-secondary-line:`preprint: arXiv:2007.12891 <https://arxiv.org/abs/2007.12891>` :bdg-link-success-line:`code on GitHub <https://github.com/sblauth/nonlinear_shape_cg_benchmark>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Shape optimization based on shape calculus has received a lot of attention in recent years, particularly regarding the development, analysis, and modification of efficient optimization algorithms. In this paper we propose and investigate nonlinear conjugate gradient methods based on Steklov--Poincaré-type metrics for the solution of shape optimization problems constrained by partial differential equations. We embed these methods into a general algorithmic framework for gradient-based shape optimization methods and discuss the numerical discretization of the algorithms. We numerically compare the proposed nonlinear conjugate gradient methods to the already established gradient descent and limited memory BFGS methods for shape optimization on several benchmark problems. The results show that the proposed nonlinear conjugate gradient methods perform well in practice and that they are an efficient and attractive addition to already established gradient-based shape optimization algorithms.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2021Nonlinear,
                      author     = {Blauth, Sebastian},
                      journal    = {SIAM J. Optim.},
                      title      = {{Nonlinear Conjugate Gradient Methods for PDE Constrained Shape Optimization Based on Steklov-Poincar\'{e}-Type Metrics}},
                      year       = {2021},
                      issn       = {1052-6234,1095-7189},
                      number     = {3},
                      pages      = {1658--1689},
                      volume     = {31},
                      doi        = {10.1137/20M1367738},
                      fjournal   = {SIAM Journal on Optimization},
                      mrclass    = {49Q10 (35Q93 49M05 49M37 90C53)},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Nonlinear Conjugate Gradient Methods for PDE Constrained Shape Optimization Based on Steklov-Poincaré-Type Metrics
                    Sebastian Blauth
                    SIAM Journal on Optimization 31(3), 2021
                    https://doi.org/10.1137/20M1367738



#.  | **cashocs: A Computational, Adjoint-Based Shape Optimization and Optimal Control Software**
    | SoftwareX 13, 2021
    | :bdg-link-primary-line:`doi: 10.1016/j.softx.2020.100646 <https://doi.org/10.1016/j.softx.2020.100646>` :bdg-link-secondary-line:`preprint: arXiv:2010.02048 <https://arxiv.org/abs/2010.02048>` :bdg-link-success-line:`code on GitHub <https://github.com/sblauth/cashocs>` :bdg-link-info-line:`on the web <https://www.itwm.fraunhofer.de/en/departments/tv/products-and-services/shape-optimization-cashocs-software.html>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                The solution of optimization problems constrained by partial differential equations (PDEs) plays an important role in many areas of science and industry. In this work we present cashocs, a new software package written in Python, which automatically solves such problems in the context of optimal control and shape optimization. The software cashocs implements a discretization of the continuous adjoint approach, which derives the necessary adjoint systems and (shape) derivatives in an automated fashion. As cashocs is based on the finite element software FEniCS, it inherits its simple, high-level user interface. This makes it straightforward to define and solve PDE constrained optimization problems with our software. In this paper, we discuss the design and functionalities of cashocs and also demonstrate its straightforward usability and applicability.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2021cashocs,
                      author   = {Sebastian Blauth},
                      journal  = {SoftwareX},
                      title    = {{cashocs: A Computational, Adjoint-Based Shape Optimization and Optimal Control Software}},
                      year     = {2021},
                      issn     = {2352-7110},
                      pages    = {100646},
                      volume   = {13},
                      doi      = {10.1016/j.softx.2020.100646},
                      keywords = {PDE constrained optimization, Adjoint approach, Shape optimization, Optimal control},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    cashocs: A Computational, Adjoint-Based Shape Optimization and Optimal Control Software
                    Sebastian Blauth
                    SoftwareX 13, 2021
                    https://doi.org/10.1016/j.softx.2020.100646



#.  | **Optimal control of the Sabatier process in microchannel reactors**
    | *with Christian Leithäuser and René Pinnau*
    | Journal of Engineering Mathematics 128(1), 2021
    | :bdg-link-primary-line:`doi: 10.1007/s10665-021-10134-2 <https://doi.org/10.1007/s10665-021-10134-2>` :bdg-link-secondary-line:`preprint: arXiv:2007.12457 <https://arxiv.org/abs/2007.12457>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                We consider the optimization of a chemical microchannel reactor by means of PDE-constrained optimization techniques, using the example of the Sabatier reaction. To model the chemically reacting flow in the microchannels, we introduce a three- and a one-dimensional model. As these are given by strongly coupled and highly nonlinear systems of partial differential equations (PDEs), we present our software package cashocs which implements the adjoint approach and facilitates the numerical solution of the subsequent optimization problems. We solve a parameter identification problem numerically to determine necessary kinetic parameters for the models from experimental data given in the literature. The obtained results show excellent agreement to the measurements. Finally, we present two optimization problems for optimizing the reactor’s product yield. First, we use a tracking-type cost functional to maximize the reactant conversion, keep the flow rate of the reactor fixed, and use its wall temperature as optimization variable. Second, we consider the wall temperature and the inlet gas velocity as optimization variables, use an objective functional for maximizing the flow rate in the reactor, and ensure the quality of the product by means of a state constraint. The results obtained from solving these problems numerically show great potential for improving the design of the microreactor.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2021Optimal,
                      author   = {Blauth, Sebastian and Leith\"{a}user, Christian and Pinnau, Ren\'{e}},
                      journal  = {J. Engrg. Math.},
                      title    = {{Optimal control of the Sabatier process in microchannel reactors}},
                      year     = {2021},
                      issn     = {0022-0833,1573-2703},
                      pages    = {Paper No. 19, 28},
                      volume   = {128},
                      doi      = {10.1007/s10665-021-10134-2},
                      fjournal = {Journal of Engineering Mathematics},
                      mrclass  = {80A32 (35Q35 49M05 49M41 65K10 76V05)},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Optimal control of the Sabatier process in microchannel reactors
                    Sebastian Blauth, Christian Leithäuser, and René Pinnau
                    Journal of Engineering Mathematics 128(1), 2021
                    https://doi.org/10.1007/s10665-021-10134-2



#.  | **Model hierarchy for the shape optimization of a microchannel cooling system**
    | *with Christian Leithäuser and René Pinnau*
    | ZAMM Journal of Applied Mathematics and Mechanics 101(4), 2021
    | :bdg-link-primary-line:`doi: 10.1002/zamm.202000166 <https://doi.org/10.1002/zamm.202000166>` :bdg-link-secondary-line:`preprint: arXiv:1911.06819 <https://arxiv.org/abs/1911.06819>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                We model a microchannel cooling system and consider the optimization of its shape by means of shape calculus. A three-dimensional model covering all relevant physical effects and three reduced models are introduced. The latter are derived via a homogenization of the geometry in 3D and a transformation of the three-dimensional models to two dimensions. A shape optimization problem based on the tracking of heat absorption by the cooler and the uniform distribution of the flow through the microchannels is formulated and adapted to all models. We present the corresponding shape derivatives and adjoint systems, which we derived with a material derivative free adjoint approach. To demonstrate the feasibility of the reduced models, the optimization problems are solved numerically with a gradient descent method. A comparison of the results shows that the reduced models perform similarly to the original one while using significantly less computational resources.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2021Model,
                      author   = {Blauth, Sebastian and Leith\"{a}user, Christian and Pinnau, Ren\'{e}},
                      journal  = {ZAMM Z. Angew. Math. Mech.},
                      title    = {{Model hierarchy for the shape optimization of a microchannel cooling system}},
                      year     = {2021},
                      issn     = {0044-2267,1521-4001},
                      number   = {4},
                      pages    = {Paper No. e202000166, 28},
                      volume   = {101},
                      doi      = {10.1002/zamm.202000166},
                      fjournal = {ZAMM. Zeitschrift f\"{u}r Angewandte Mathematik und Mechanik. Journal of Applied Mathematics and Mechanics},
                      mrclass  = {76D55 (35Q35 49M41 49Q10 65K05 65K10)},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Model hierarchy for the shape optimization of a microchannel cooling system
                    Sebastian Blauth, Christian Leithäuser, and René Pinnau
                    ZAMM Journal of Applied Mathematics and Mechanics 101(4), 2021
                    https://doi.org/10.1002/zamm.202000166



#.  | **Shape sensitivity analysis for a microchannel cooling system**
    | *with Christian Leithäuser and René Pinnau*
    | Journal of Mathematical Analysis and Applications 492(2), 2020
    | :bdg-link-primary-line:`doi: 10.1016/j.jmaa.2020.124476 <https://doi.org/10.1016/j.jmaa.2020.124476>` :bdg-link-secondary-line:`preprint: arXiv:2005.02754 <https://arxiv.org/abs/2005.02754>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                We analyze the theoretical framework of a shape optimization problem for a microchannel cooling system. To this end, a cost functional based on the tracking of absorbed energy by the cooler as well as some desired flow on a subdomain of the cooling system is introduced. The flow and temperature of the coolant are modeled by a Stokes system coupled to a convection diffusion equation. We prove the well-posedness of this model on a domain transformed by the speed method. Further, we rigorously prove that the cost functional of our optimization problem is shape differentiable and calculate its shape derivative by means of a recent material derivative free adjoint approach.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2020Shape,
                      author   = {Blauth, Sebastian and Leith\"{a}user, Christian and Pinnau, Ren\'{e}},
                      journal  = {J. Math. Anal. Appl.},
                      title    = {{Shape sensitivity analysis for a microchannel cooling system}},
                      year     = {2020},
                      issn     = {0022-247X},
                      number   = {2},
                      pages    = {124476},
                      volume   = {492},
                      doi      = {10.1016/j.jmaa.2020.124476},
                      fjournal = {Journal of Mathematical Analysis and Applications},
                      mrclass  = {49Q12 (35Q35 49Q10 76D07)},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Shape sensitivity analysis for a microchannel cooling system
                    Sebastian Blauth, Christian Leithäuser, and René Pinnau
                    Journal of Mathematical Analysis and Applications 492(2), 2020
                    https://doi.org/10.1016/j.jmaa.2020.124476



#.  | **Identification of the blood perfusion rate for laser-induced thermotherapy in the liver**
    | *with Matthias Andres, Christian Leithäuser, and Norbert Siedow*
    | Journal of Mathematics in Industry 10, 2020
    | :bdg-link-primary-line:`doi: 10.1186/s13362-020-00085-1 <https://doi.org/10.1186/s13362-020-00085-1>` :bdg-link-secondary-line:`preprint: arXiv:1910.09199 <https://arxiv.org/abs/1910.09199>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Using PDE-constrained optimization we introduce a parameter identification approach which can identify the blood perfusion rate from MR thermometry data obtained during the treatment with laser-induced thermotherapy (LITT). The blood perfusion rate, i.e., the cooling effect induced by blood vessels, can be identified during the first stage of the treatment. This information can then be used by a simulation to monitor and predict the ongoing treatment. The approach is tested with synthetic measurements with and without artificial noise as input data.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Andres2020Identification,
                      author   = {Andres, Matthias and Blauth, Sebastian and Leith\"{a}user, Christian and Siedow, Norbert},
                      journal  = {J. Math. Ind.},
                      title    = {{Identification of the blood perfusion rate for laser-induced thermotherapy in the liver}},
                      year     = {2020},
                      volume   = {10},
                      doi      = {10.1186/s13362-020-00085-1},
                      fjournal = {Journal of Mathematics in Industry},
                      mrclass  = {92C50 (35Q92 93-10 93B30)},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Identification of the blood perfusion rate for laser-induced thermotherapy in the liver
                    Matthias Andres, Sebastian Blauth, Christian Leithäuser, and Norbert Siedow
                    Journal of Mathematics in Industry 10, 2020
                    https://doi.org/10.1186/s13362-020-00085-1



#.  | **Mathematical modeling of vaporization during laser-induced thermotherapy in liver tissue**
    | *with Frank Hübner, Christian Leithäuser, Norbert Siedow, and Thomas Vogl*
    | Journal of Mathematics in Industry 10, 2020
    | :bdg-link-primary-line:`doi: 10.1186/s13362-020-00082-4 <https://doi.org/10.1186/s13362-020-00082-4>` :bdg-link-secondary-line:`preprint: arXiv:1910.12515 <https://arxiv.org/abs/1910.12515>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Laser-induced thermotherapy (LITT) is a minimally invasive method causing tumor destruction due to heat ablation and coagulative effects. Computer simulations can play an important role to assist physicians with the planning and monitoring of the treatment. Our recent study with ex-vivo porcine livers has shown that the vaporization of the water in the tissue must be taken into account when modeling LITT. We extend the model used for simulating LITT to account for vaporization using two different approaches. Results obtained with these new models are then compared with the measurements from the original study.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2020Mathematical,
                      author   = {Blauth, Sebastian and H\"{u}bner, Frank and Leith\"{a}user, Christian and Siedow, Norbert and Vogl, Thomas J.},
                      journal  = {J. Math. Ind.},
                      title    = {{Mathematical modeling of vaporization during laser-induced thermotherapy in liver tissue}},
                      year     = {2020},
                      volume   = {10},
                      doi      = {10.1186/s13362-020-00082-4},
                      fjournal = {Journal of Mathematics in Industry},
                      mrclass  = {92C50 (78A55)},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Mathematical modeling of vaporization during laser-induced thermotherapy in liver tissue
                    Sebastian Blauth, Frank Hübner, Christian Leithäuser, Norbert Siedow, and Thomas J. Vogl
                    Journal of Mathematics in Industry 10, 2020
                    https://doi.org/10.1186/s13362-020-00082-4



Conference Proceedings
----------------------



#.  | **Topology Optimization for Uniform Flow Distribution in Electrolysis Cells**
    | *with Leon Baeck, Christian Leithäuser, René Pinnau, and Kevin Sturm*
    | Proceedings in Applied Mathematics and Mechanics 23(3), 2023
    | :bdg-link-primary-line:`doi: 10.1002/pamm.202300163 <https://doi.org/10.1002/pamm.202300163>` :bdg-link-secondary-line:`preprint: arXiv:2308.01826 <https://arxiv.org/abs/2308.01826>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                In this paper we consider the topology optimization for a bipolar plate of a hydrogen electrolysis cell. We present a model for the bipolar plate using the Stokes equation with an additional drag term, which models the influence of fluid and solid regions. Furthermore, we derive a criterion for a uniform flow distribution in the bipolar plate. To obtain shapes that are well-manufacturable, we introduce a novel smoothing technique for the fluid velocity. Finally, we present some numerical results and investigate the influence of the smoothing on the obtained shapes.

            .. tab-item:: BibTeX citation

                .. code-block:: bibtex

                    @Article{Baeck2023Topology,
                      author  = {Baeck, Leon and Blauth, Sebastian and Leithäuser, Christian and Pinnau, René and Sturm, Kevin},
                      journal = {PAMM},
                      title   = {{Topology optimization for uniform flow distribution in electrolysis cells}},
                      year    = {2023},
                      number  = {3},
                      pages   = {e202300163},
                      volume  = {23},
                      doi     = {10.1002/pamm.202300163},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Topology optimization for uniform flow distribution in electrolysis cells
                    Leon Baeck, Sebastian Blauth, Christian Leithäuser, René Pinnau, and Kevin Sturm
                    Proceedings in Applied Mathematics and Mechanics 23(3), 2023
                    https://doi.org/10.1002/pamm.202300163



#.  | **Shape Optimization with Nonlinear Conjugate Gradient Methods**
    | Spectral and High Order Methods for Partial Differential Equations ICOSAHOM 2020+1 (Lecture Notes in Computational Science and Engineering 137), 2023
    | :bdg-link-primary-line:`doi: 10.1007/978-3-031-20432-6_9 <https://doi.org/10.1007/978-3-031-20432-6_9>` :bdg-link-secondary-line:`preprint: arXiv:2201.05394 <https://arxiv.org/abs/2201.05394>` :bdg-link-success-line:`code on GitHub <https://github.com/sblauth/nonlinear_shape_cg_benchmark>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                In this chapter, we investigate recently proposed nonlinear conjugate gradient (NCG) methods for shape optimization problems. We briefly introduce the methods as well as the corresponding theoretical background and investigate their performance numerically. The obtained results confirm that the NCG methods are efficient and attractive solution algorithms for shape optimization problems.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @InCollection{Blauth2023Shape,
                      author    = {Blauth, Sebastian},
                      booktitle = {Spectral and {H}igh {O}rder {M}ethods for {P}artial {D}ifferential {E}quations {ICOSAHOM} 2020+1},
                      publisher = {Springer, Cham},
                      title     = {{Shape Optimization with Nonlinear Conjugate Gradient Methods}},
                      year      = {2023},
                      isbn      = {978-3-031-20431-9; 9783031204326},
                      pages     = {169--181},
                      series    = {Lect. Notes Comput. Sci. Eng.},
                      volume    = {137},
                      doi       = {10.1007/978-3-031-20432-6\_9},
                      mrclass   = {99-06},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Shape Optimization with Nonlinear Conjugate Gradient Methods
                    Sebastian Blauth
                    Spectral and High Order Methods for Partial Differential Equations ICOSAHOM 2020+1 (Lecture Notes in Computational Science and Engineering 137), 2023
                    https://doi.org/10.1007/978-3-031-20432-6_9



#.  | **Optimal Control and Asymptotic Analysis of the Cattaneo Equation**
    | *with Matthias Andres, René Pinnau, and Claudia Totzeck*
    | Proceedings in Applied Mathematics and Mechanics 19(1), 2019
    | :bdg-link-primary-line:`doi: 10.1002/pamm.201900184 <https://doi.org/10.1002/pamm.201900184>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                We compare the classical Fourier model for heat transfer to the Cattaneo model for delayed heat transfer. In particular, we consider the asymptotic behavior of the Cattaneo model for a vanishing delay time in the context of an optimal control problem with tracking type cost functional. It is possible to rigorously prove that both optimal controls and states for this problem constrained by the Cattaneo equation converge to the respective optimal control and state of the problem constrained by the heat equation (cf. [1]). Here, we present a short overview of the topic as well as some numerical results for the limit process.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Blauth2019Optimal,
                      author   = {Blauth, Sebastian and Andres, Matthias and Pinnau, Ren\'{e} and Totzeck, Claudia},
                      journal  = {PAMM},
                      title    = {{Optimal Control and Asymptotic Analysis of the Cattaneo Equation}},
                      year     = {2019},
                      number   = {1},
                      pages    = {e201900184},
                      volume   = {19},
                      doi      = {10.1002/pamm.201900184},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Optimal Control and Asymptotic Analysis of the Cattaneo Equation
                    Sebastian Blauth, Matthias Andres, René Pinnau, and Claudia Totzeck
                    Proceedings in Applied Mathematics and Mechanics 19(1), 2019
                    https://doi.org/10.1002/pamm.201900184



#.  | **A Numerical Comparison of Consensus-Based Global Optimization to other Particle-based Global Optimization Schemes**
    | *with Claudia Totzeck, René Pinnau, and Steffen Schotthöfer*
    | Proceedings in Applied Mathematics and Mechanics 18(1), 2018
    | :bdg-link-primary-line:`doi: 10.1002/pamm.201800291 <https://doi.org/10.1002/pamm.201800291>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                We compare a first-order stochastic swarm intelligence model called consensus-based optimization (CBO), which may be used for the global optimization of a function in multiple dimensions, to other particle swarm algorithms for global optimization. CBO allows for passage to the mean-field limit resulting in a nonlocal, degenerate, parabolic PDE. Exploiting tools from PDE analysis, it is possible to rigorously prove convergence results for the algorithm (see [3]). In the present article we discuss numerical results obtained with the Particle Swarm Optimization (PSO) [4], Wind-Driven Optimization (WDO) [6] and CBO and show that CBO leads to very competitive results.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Totzeck2018Numerical,
                      author  = {Totzeck, Claudia and Pinnau, René and Blauth, Sebastian and Schotthöfer, Steffen},
                      journal = {PAMM},
                      title   = {{A Numerical Comparison of Consensus-Based Global Optimization to other Particle-based Global Optimization Schemes}},
                      year    = {2018},
                      number  = {1},
                      pages   = {e201800291},
                      volume  = {18},
                      doi     = {10.1002/pamm.201800291},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    A Numerical Comparison of Consensus-Based Global Optimization to other Particle-based Global Optimization Schemes
                    Claudia Totzeck, René Pinnau, Sebastian Blauth, and Steffen Schotthöfer
                    Proceedings in Applied Mathematics and Mechanics 18(1), 2018
                    https://doi.org/10.1002/pamm.201800291



Academic Theses
---------------



#.  | **Adjoint-Based Shape Optimization and Optimal Control with Applications to Microchannel Systems**
    | Fraunhofer Verlag, 2021, PhD Thesis
    | :bdg-link-primary-line:`doi: 10.24406/publica-fhg-283725 <https://doi.org/10.24406/publica-fhg-283725>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                This thesis investigates optimization problems constrained by partial differential equations (PDEs) with microchannel systems as novel applications. As our first application, we consider the shape optimization of a microchannel cooling system, rigorously analyze the problem, and prove its shape differentiability. Further, we also consider the numerical optimization of the cooling system for which we employ a hierarchy of reduced models. As our second application, we investigate the optimization of a chemical microchannel reactor for the Sabatier process. For this, we solve a parameter identification problem to determine the kinetic reaction parameters and consider the optimization of the reactor's operating conditions using techniques from PDE constrained optimal control. To provide efficient solution techniques for shape optimization problems, we introduce novel nonlinear conjugate gradient methods for shape optimization and analyze their performance on several benchmark problems. Finally, we present our open-source software cashocs, which implements and automates the adjoint approach and, thus, facilitates the numerical solution of PDE constrained optimization problems.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @PhdThesis{Blauth2021Adjoint,
                      author = {Blauth, Sebastian},
                      school = {TU Kaiserslautern},
                      title  = {{Adjoint-Based Shape Optimization and Optimal Control with Applications to Microchannel Systems}},
                      year   = {2021},
                      type   = {Dissertation},
                      doi    = {10.24406/publica-fhg-283725},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Adjoint-Based Shape Optimization and Optimal Control with Applications to Microchannel Systems
                    Sebastian Blauth
                    Fraunhofer Verlag, 2021
                    https://doi.org/10.24406/publica-fhg-283725



#.  | **Optimal Control and Asymptotic Analysis of the Cattaneo Model**
    | KLUEDO, 2018, Master's Thesis
    | :bdg-link-primary-line:`urn:nbn:de:hbz:386-kluedo-53727 <https://nbn-resolving.org/urn:nbn:de:hbz:386-kluedo-53727>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Optimal control of partial differential equations is an important task in applied mathematics where it is used in order to optimize, for example, industrial or medical processes. In this thesis we investigate an optimal control problem with tracking type cost functional for the Cattaneo equation with distributed control, that is, :math:`\tau y_{tt} + y_t - \Delta y = u`. Our focus is on the theoretical and numerical analysis of the limit process :math:`\tau \to 0` where we prove the convergence of solutions of the Cattaneo equation to solutions of the heat equation. We start by deriving both the Cattaneo and the classical heat equation as well as introducing our notation and some functional analytic background. Afterwards, we prove the well-posedness of the Cattaneo equation for homogeneous Dirichlet boundary conditions, that is, we show the existence and uniqueness of a weak solution together with its continuous dependence on the data. We need this in the following, where we investigate the optimal control problem for the Cattaneo equation: We show the existence and uniqueness of a global minimizer for an optimal control problem with tracking type cost functional and the Cattaneo equation as a constraint. Subsequently, we do an asymptotic analysis for :math:`\tau \to 0` for both the forward equation and the aforementioned optimal control problem and show that the solutions of these problems for the Cattaneo equation converge strongly to the ones for the heat equation. Finally, we investigate these problems numerically, where we examine the different behaviour of the models and also consider the limit :math:`\tau \to 0`, suggesting a linear convergence rate.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @MastersThesis{Blauth2018Optimal,
                      author = {Sebastian Blauth},
                      school = {Technische Universit{\"a}t Kaiserslautern},
                      title  = {{Optimal Control and Asymptotic Analysis of the Cattaneo Model}},
                      year   = {2018},
                      type   = {Masterthesis},
                      url    = {http://nbn-resolving.de/urn:nbn:de:hbz:386-kluedo-53727},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Optimal Control and Asymptotic Analysis of the Cattaneo Model
                    Sebastian Blauth
                    KLUEDO, 2018
                    https://nbn-resolving.org/urn:nbn:de:hbz:386-kluedo-53727



Book Chapters
-------------



#.  | **Mathematical Modeling and Simulation of Laser-Induced Thermotherapy for the Treatment of Liver Tumors**
    | *with Frank Hübner, Christian Leithäuser, Norbert Siedow, and Thomas Vogl*
    | Modeling, Simulation and Optimization in the Health- and Energy-Sector, 2022
    | :bdg-link-primary-line:`doi: 10.1007/978-3-030-99983-4_1 <https://doi.org/10.1007/978-3-030-99983-4_1>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Laser-induced thermotherapy (LITT) plays an important role in oncology to treat human liver tumors. LITT is an alternative method which is used when surgery is too dangerous for the patient. It is a minimally invasive method causing tumor destruction due to heat ablation and coagulative effects of the tissue. The big advantage of the LITT compared to other minimally invasive procedures is that the treatment takes place under MRI control, such that patients are exposed to a small radiation dose. Based on temperature-sensitive magnetic resonance parameters, it is feasible to monitor the tissue temperature during cancer treatment (MR thermometry). Combining both MR thermometry and mathematical simulation is a promising procedure to identify temperature-dependent tissue parameters and to optimize the cancer treatment. The present paper describes the mathematical modeling of the laser-induced thermotherapy. The well-known Pennes bioheat equation is coupled with the radiative transfer equation which describes the energy gain of the tumor tissue. It is shown, that the modeling of vaporization is important to match mathematical simulation with temperature measurements for ex-vivo porcine liver.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @InProceedings{Blauth2022Mathematical,
                      author    = {Blauth, Sebastian and H{\"u}bner, Frank and Leith{\"a}user, Christian and Siedow, Norbert and Vogl, Thomas J.},
                      booktitle = {Modeling, Simulation and Optimization in the Health- and Energy-Sector},
                      title     = {{Mathematical Modeling and Simulation of Laser-Induced Thermotherapy for the Treatment of Liver Tumors}},
                      year      = {2022},
                      address   = {Cham},
                      editor    = {Pinnau, Ren{\'e} and Gauger, Nicolas R. and Klar, Axel},
                      pages     = {3--23},
                      publisher = {Springer International Publishing},
                      doi       = {10.1007/978-3-030-99983-4_1},
                      isbn      = {978-3-030-99983-4},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    Mathematical Modeling and Simulation of Laser-Induced Thermotherapy for the Treatment of Liver Tumors
                    Sebastian Blauth, Frank Hübner, Christian Leithäuser, Norbert Siedow, and Thomas J. Vogl
                    Modeling, Simulation and Optimization in the Health- and Energy-Sector, 2022
                    https://doi.org/10.1007/978-3-030-99983-4_1



Others
------



#.  | **Optimization of hole patterns for homogeneous cooling**
    | *with Walter Arne and Christian Leithäuser*
    | Man-Made Fibers International 3 / 2024, 2024
    | :bdg-link-primary-line:`URL <https://www.textiletechnology.net/epaper/chemical-fibers-international/108/epaper/Man-Made-Fibers-International-32024/index.html>`




#.  | **MINT-EC-Girls-Camp: Math-Talent-School**
    | *with Lena Leiß, Stefan Ruzika, Thomas Jung, Andrea Meier, and Robert Sicks*
    | KOMMS Reports (Reports zur Mathematischen Modellierung in MINT-Projekten in der Schule) 9, 2019
    | :bdg-link-primary-line:`urn:nbn:de:hbz:386-kluedo-57924 <https://nbn-resolving.org/urn:nbn:de:hbz:386-kluedo-57924>`

    .. dropdown:: Additional resources
        :icon: three-bars

        .. tab-set::

            .. tab-item:: Abstract

                Die MINT-EC-Girls-Camp: Math-Talent-School ist eine vom Fraunhofer Institut für Techno- und Wirtschaftsmathematik (ITWM) initiierte Veranstaltung, die regelmäßig als Kooperation zwischen dem Felix-Klein-Zentrum für Mathematik und dem Verein mathematisch-naturwissenschaftlicher Excellence-Center an Schulen e.V. (Verein MINT-EC) durchgeführt wird. Die methodisch-didaktische Konzeption der Math-Talent-Schools erfolgt durch das Kompetenzzentrum für Mathematische Modellierung in MINT-Projekten in der Schule (KOMMS), einer wissenschaftlichen Einrichtung des Fachbereichs Mathematik der Technischen Universität Kaiserslautern. Die inhaltlich-organisatorische Ausführung übernimmt das Fraunhofer-Institut für Techno- und Wirtschaftsmathematik ITWM in enger Abstimmung und Kooperation von Wissenschaftlern der Technischen Universität und des Fraunhofer ITWM. Die MINT-EC-Girls-Camp: Math-Talent-School hat zum Ziel, Mathematik-interessierten Schülerinnen einen Einblick in die Arbeitswelt von Mathematikerinnen und Mathematikern zu geben. In diesem Artikel stellen wir die Math-Talent-School vor. Hierfür werden die fachlichen und fachdidaktischen Hintergründe der Projekte beleuchtet, der Ablauf der Veranstaltung erläutert und ein Fazit gezogen.

            .. tab-item:: BibTeX citation
 
                .. code-block:: bibtex

                    @Article{Leiss2019MINT,
                      author = {Lena Leiß and Stefan Ruzika and Sebastian Blauth and Thomas Jung and Andrea Maier and Robert Sicks},
                      title  = {{MINT-EC-Girls-Camp: Math-Talent-School}},
                      year   = {2019},
                      url    = {http://nbn-resolving.de/urn:nbn:de:hbz:386-kluedo-57924},
                    }

            .. tab-item:: Plain text citation

                .. code-block:: text

                    MINT-EC-Girls-Camp: Math-Talent-School
                    Lena Leiß, Stefan Ruzika, Sebastian Blauth, Thomas Jung, Andrea Maier, and Robert Sicks
                    KOMMS Reports (Reports zur Mathematischen Modellierung in MINT-Projekten in der Schule) 9, 2019
                    https://nbn-resolving.org/urn:nbn:de:hbz:386-kluedo-57924


