package com.livewire

sealed class ScadaMessage

class AnalogValue(val value: Double) : ScadaMessage()
class DigitalStatus(val state: Boolean) : ScadaMessage()
class Alarm(val severity: Int) : ScadaMessage()

fun handleMessage(msg: ScadaMessage): String = when (msg) {
    is AnalogValue -> "Analog: ${msg.value}"
    is DigitalStatus -> "Digital Status: ${msg.state}"
    is Alarm -> "Alarm: ${msg.severity}"
}

fun main() {

    var analogValue = AnalogValue(12.34)
    var digitalStatus = DigitalStatus(false)
    var alarm = Alarm(0)

    println("Messages returned:")
    println("\t${handleMessage(analogValue)}")
    println("\t${handleMessage(digitalStatus)}")
    println("\t${handleMessage(alarm)}")

}