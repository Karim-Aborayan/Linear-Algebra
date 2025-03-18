using System.Collections;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Numerics;

namespace Linear_Algebra_C_
{
    public class Matrix<T>: IEnumerable, INotifyPropertyChanged where T : INumber<T>
    {   
        public event PropertyChangedEventHandler? PropertyChanged;
        public void OnPropertyChanged(string propertyName)
        {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }

        public int Rows { get; set; }
        public int Cols { get; set; }
        private  T[,] _matrix;

        public Matrix(int rows, int cols)
        {
            Rows = rows;
            Cols = cols;
            _matrix = new T[rows, cols];
        }

        public Matrix(T[,] matrix)
        {
            Rows = matrix.GetLength(0);
            Cols = matrix.GetLength(1);
            _matrix = matrix;
        }

        public T this[int row, int col]
        {
            get => _matrix[row,col];
            set
            {
                _matrix[row, col] = value;
                OnPropertyChanged("Item[]");
            }
        }

        public IEnumerator GetEnumerator()
        {
            return _matrix.GetEnumerator();
        }

    }
}
