package com.livewire

fun main() {
    // 24 hourly load readings in MW
    val loads = listOf(
        420.5, 380.2, 350.1, 340.0, 335.5, 360.0,
        410.2, 520.5, 680.3, 750.1, 820.0, 890.5,
        910.2, 870.3, 810.5, 760.2, 720.0, 650.3,
        580.5, 520.0, 480.3, 450.2, 430.1, 405.0
    )

    val averageLoad = loads.average()
    val peakLoad = loads.maxOrNull()
    val hoursAbove500 = loads.count { it > 500.0 }
    val puLoads = loads.map { it / 1000.0 }

    println("List of loads:")
    loads.forEach{
        print("${it}, ")
    }
    println("\naverage load: ${String.format("%.2f", averageLoad)}")
    println("peak load: ${peakLoad}")
    println("Number of hours above 500 MW: ${hoursAbove500}")
    println("Loads normalized to 1000 MW:")
    puLoads.forEach{
        print("${String.format("%.2f", it)}, ")
    }

}