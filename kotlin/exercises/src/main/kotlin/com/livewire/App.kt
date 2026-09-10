package com.livewire

fun List<Double>.normalize(base: Double): List<Double> {
    val normalized = this.map { it / base}
    return normalized
}

fun List<Double>.movingAverage(window: Int): List<Double> {
    val windows = this.windowed(size = window, step = 1)
    return windows.map{ it.average() }
}

fun main() {

    val loads = listOf(
        420.5, 380.2, 350.1, 340.0, 335.5, 360.0,
        410.2, 520.5, 680.3, 750.1, 820.0, 890.5,
        910.2, 870.3, 810.5, 760.2, 720.0, 650.3,
        580.5, 520.0, 480.3, 450.2, 430.1, 405.0
    )

    val normalized = loads.normalize(1000.0)

    val windowList = normalized.movingAverage(3)

    println("Loads normalized to 1000 MW:")
    normalized.forEach {
        print("${String.format("%.2f", it)}, ")
    }
    println()
    println("Running 3 hour averages:")
    windowList.forEach {
        print("${String.format("%.2f", it)}, ")
    }
}