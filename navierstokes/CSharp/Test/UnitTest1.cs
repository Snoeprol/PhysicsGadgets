using Microsoft.VisualStudio.TestTools.UnitTesting;
using NavierStokes;
using System.Collections.Generic;

namespace Test
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            var coordinates = new Coordinates(2, 4);
            for (int i = 0; i < coordinates._V; i++)
            {
                List<int> coordinate = new List<int>();
                coordinates.Index2Coord(i, coordinate);
                System.Console.WriteLine("{0}", coordinate);
            }
        }
    }
}
