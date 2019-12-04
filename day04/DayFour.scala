object DayFour {
  var part1 = 0
  var part2 = 0
  def main(args: Array[String]): Unit = {
    (307237 to 769058+1).foreach { number =>
      val numberSeq = number.toString.toSeq
      val isIncreasing = numberSeq.sorted.equals(numberSeq)
      val numberFreq = numberSeq.groupBy(identity).view.mapValues(_.size).toSeq.map(t => t._2)
      if (isIncreasing && numberFreq.exists(_ > 1)) {
        part1 += 1
      }
      if (isIncreasing && numberFreq.exists(_ == 2)) {
        part2 += 1
      }
    }
    println(part1)
    println(part2)
  }
}