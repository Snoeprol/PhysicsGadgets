using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NavierStokes
{
    public class Coordinates
    {
        public int _N;
        public int _D;
        public int _V;
        public Coordinates(int N, int D)
        {
            _N = N;
            _D = D;
            _V = (int) Math.Pow(N, D);
        }
        public int Coord2Index(int[] coordinate)
        {
            int index = 0;
            for (int d = 0; d < _D; d++)
            {
                index += coordinate[d] * (int)Math.Pow(_N, d);
            }
            return index;
        }
        public void Index2Coord(int index, int[] coordinate)
        {
            for (int d = _D - 1; d > -1; d--)
            {
                int divider = (int) Math.Pow(_N, d);
                coordinate[d] = index / divider;
                index = index % divider;
            }
        }

        private int CalcNeighbour(int index, int dimension, int direction)
        {
            int[] coord_out = new int[_D];
            Index2Coord(index, coord_out);
            if (direction == 1)
            {
                coord_out[dimension] = (coord_out[dimension] + 1) % _N;
            }
            else
            {
                coord_out[dimension] = (coord_out[dimension] - 1) % _N;
            }
            return Coord2Index(coord_out);
        }
    }
}
