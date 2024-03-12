:html_theme.sidebar_secondary.remove:

Research Interests
==================

.. dropdown:: Shape Optimization

   * Shape optimization refers to the process of optimizing the shape / design / geometry of some system to improve the systems quality

   * In our group, we do not parametrize a shape but work directly with a given discretized geometry, i.e., a mesh, which we obtain from CAD data

   * During the optimization, the location of the mesh nodes is optimized, resulting in a different geometry

   * At the moment, we are working on the following applications: Electrolysis and Fuel Cells, Chemical Reactors, Spinning Processes and Microchannel Systems, but we are always looking for new potential applications

.. dropdown:: Topology Optimization

   * Topology optimization is closely related to shape optimization: There, also the geometry or design of some system should be optimized

   * Whereas in shape optimization the topology of the system is fixed (i.e. the distribution of different materials or the "number of holes"), this is not the case for topology optimization, where an optimal topology or material distribution is sought

   * At the moment, we are mostly working on topology optimization for the application of electrolysis cells

.. dropdown:: Efficient Solution Algorithms for PDE Constrained Optimization

   * To obtain good optimization results fast, efficient solution algorithms are indisposable. They should make the most out of the limited CPU time available for optimization

   * In this field, we have developed several novel solution algorithms and methods:

     * Space Mapping Methods for Shape Optimization `<https://doi.org/10.1137/22M1515665>`_

     * Quasi-Newton Methods for Topology Optimization `<https://doi.org/10.1007/s00158-023-03653-2>`_

     * Nonlinear Conjugate Gradient Methods for Shape Optimization `<https://doi.org/10.1137/20M1367738>`_

   * All of these approaches are implemented in our software cashocs

   * Our software cashocs is also enhanced with the newest developments in the fields of shape optimization

.. dropdown:: Large-Scale Optimization

   * As we consider PDE constrained optimization for industrial applications, we have to solve large-scale optimization problems

   * In order to efficiently solve these, both efficient solution algorithms and parallelization are absolutely necessary

   * Our optimization software cashocs is designed to treat very large-scale optimization problems with several millions of design variables


