package com.livewire

import kotlinx.coroutines.*
import kotlin.random.Random

// runBlocking:
//  1. Creates a coroutine scope — a container where coroutines can live
//  2. Blocks the calling thread — in this case, the main thread — until
//     every coroutine inside the block finishes
//  3. Returns the result of the last expression in the block
//
// Dispatchers.Default:
// https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-dispatchers/-default.html

fun main() = runBlocking(Dispatchers.Default) {
    // launch three async tasks
    val v1 = async { delay(1000); Random.nextDouble(0.95, 1.05) }
    val v2 = async { delay(1000); Random.nextDouble(0.95, 1.05) }
    val v3 = async { delay(1000); Random.nextDouble(0.95, 1.05) }
    
    // collect results
    val results = listOf(v1.await(), v2.await(), v3.await())
    println("Voltages returned from external sources:")
    results.forEach{
        println("\t%.4f".format(it))
    }
    val average = results.average()
    
    println("Average voltage: %.4f".format(average))
}