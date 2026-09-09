package com.livewire;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

interface PowerFlowSolver {
    double[] solve(double[] injections);
}

class DcSolver implements PowerFlowSolver {
    public double[] solve(double[] injections) {
        return injections; // trivial pass-through
    }
}

class AcSolver implements PowerFlowSolver {
    public double[] solve(double[] injections) {
        double[] result = new double[injections.length];
        for (int i = 0; i < injections.length; i++) {
            result[i] = injections[i] * 0.95;
        }
        return result;
    }
}

public class App {
    public static void main(String[] args) {
        List<PowerFlowSolver> solvers = new ArrayList<>();
        solvers.add(new DcSolver());
        solvers.add(new AcSolver());
        
        double[] input = {1.0, -0.5, -0.5};
        
        for (PowerFlowSolver solver : solvers) {
            System.out.println(
                solver.getClass().getSimpleName() + ": " + 
                Arrays.toString(solver.solve(input))
            );
        }
    }
}