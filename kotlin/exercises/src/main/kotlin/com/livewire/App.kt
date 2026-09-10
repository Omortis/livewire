package com.livewire

data class Breaker(val id: String, val status: String, val currentAmps: Double?)

fun main() {

    val breakers = listOf(
        Breaker("BRK-101", "CLOSED", 1250.54321),
        Breaker("BRK-102", "OPEN", null),     // null current — de-energized
        Breaker("BRK-103", "TRIPPED", 0.001),
        Breaker("BRK-104", "CLOSED", 980.2223),
        Breaker("BRK-105", "MAINTENANCE", null)
    )

    val amps = mutableListOf<Double?>()
    var nonNullCounter = 0
    breakers.forEach {
        print("id = ${it.id}, status = ${it.status}, ")
        val ampString = it.currentAmps?.let { String.format("%.1f", it) } ?: "No reading"
        println("currentAmps = ${ampString}")
        amps += it.currentAmps
    }
    
    val notNull = amps.filterNotNull()
    println("breakers contains ${notNull.size} valid readings.")
}