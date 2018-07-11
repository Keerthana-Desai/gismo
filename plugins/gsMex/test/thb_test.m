% This MATLAB script tests the MEX interface of the gsTHBSplineBasis class.
% Author: O. Chanon, P. Noertoft

knots = {[0,0,0,1,2,2,2],[4,5,6]};
hbs2 = gsTHBSplineBasis(knots);

% Construct a truncated hierarchical basis by reading the specified file
filename = join([filedata,'thbbasis/simple.xml']);
fprintf('Reading THB spline basis from file: %s.\n',filename)
hbs = gsTHBSplineBasis(filename);

% Print sizes
fprintf('Size of the basis %d\n',hbs.size());
fprintf('The tree has %d nodes.\n',hbs.treeSize());
fprintf('Dimension of the parameter space: %d\n',hbs.dim());
fprintf('Number of levels: %d\n',hbs.maxLevel());

% Print support
para = hbs.support();
fprintf('The parameter range is: [%f %f %f %f]\n', para);

% Print tree
fprintf('Num. of leaves: %d.\n',hbs.treeLeafSize());
hbs.treePrintLeaves();

% Print points
pts = uniformPointGrid(para(1:2),para(3:4),5);
fprintf('pts\n')
disp(pts)

% Print evaluations
ev  = hbs.eval(pts);
fprintf('ev\n')
disp(ev)

% Print sum of evaluations
fprintf('sum(ev)\n')
disp(sum(ev,1))

% Print evaluations at point 
pt = [0.7; 0.7];
evpt  = hbs.eval(pt);
fprintf('ev at u=[0.7;0.7]\n')
disp(evpt)

% Print active functions
act = hbs.active(pt);
fprintf('act\n')
disp(act)

% Print single evaluation
evs = hbs.evalSingle(16,pt);
fprintf('evs\n')
disp(evs)

% Save to output file
hbs.save('output_simple');

% Print knot vector of level 1, direction 1
knots = hbs.knots(1,1);
fprintf('knots level 1, direction 1\n')
disp(knots)

