plugins {
    kotlin("jvm") version "2.1.10"
    application
}

repositories {
    mavenCentral()
}

application {
    mainClass.set("com.livewire.AppKt")
}

kotlin {
    jvmToolchain(17)
}
