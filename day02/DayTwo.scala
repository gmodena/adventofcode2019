import scala.collection.mutable.ArrayBuffer
import util.control.Breaks._

object DayTwo extends Exception {
  val Target = 19690720
  val Offset = 4
  val input: ArrayBuffer[Int] = collection.mutable.ArrayBuffer(
    io.Source.fromFile("input.txt").mkString.trim.split(",").map(_.toInt): _*)

  def part1(program: ArrayBuffer[Int], noun: Int = 12, verb: Int = 2): Int = {

    program(1) = noun
    program(2) = verb

    var programCounter: Int = 0
    while (programCounter < program.size) {
      breakable {
        program.slice(programCounter, programCounter + Offset) match {
          case ArrayBuffer(1, l, r, dst) => {
            program(dst) = program(l) + program(r)
            programCounter += Offset
          }

          case ArrayBuffer(2, l, r, dst) => {
            program(dst) = program(l) * program(r)
            programCounter += Offset
          }

          case ArrayBuffer(99, _*) => {
            // break // TODO(gmodea): hangs here indefinitely
            programCounter = program.size
          }
        }
      }
    }
    program(0)
  }

  def part2(program: ArrayBuffer[Int], target: Int = 19690720): Option[Int] = {
    for (i <- 0 to 100; j <- 0 to 100
         if (part1(input.clone, noun = i, verb = j) == target)) {
      return Some(100 * i + j)
    }
    None
  }

  println(part1(input.clone))
  println(part2(input.clone, target = Target))
}
