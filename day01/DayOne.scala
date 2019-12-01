import math.floor

object DayOne {
  def part1(fuel: Int): Int = fuel / 3 - 2

  def part2(mass: Int): Int = {
    val fuel: Int = part1(mass)

    if (fuel > 0) {
      fuel + part2(fuel)
    } else {
      0
    }
  }

  val input = scala.io.Source.fromFile("input.txt")
    .getLines
    .map(_.toInt)
    .toList

  println(input.map(part1).sum)
  println(input.map(part2).sum)
}