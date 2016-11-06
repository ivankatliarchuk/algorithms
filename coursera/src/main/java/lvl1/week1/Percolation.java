/**
 * Name     : Percolation.java
 * Author   : ivan
 * Date     : 05 Nov 2016
 */
package lvl1.week1;

import edu.princeton.cs.algs4.WeightedQuickUnionUF;


/**
 *
 */
public class Percolation {

    boolean[][] opened;
    int size;
    int top;
    int bottom;
    private WeightedQuickUnionUF quf;

    /**
     * Creates n-by-n grid, with all sites blocked
     * @param n n-by-n grid
     */
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException();
        }
        size = n;
        this.opened = new boolean[n][n];
        quf = new WeightedQuickUnionUF(n * n);
        top = 0;
        bottom = size * size + 1;
    }

    /**
     * Open site (row, cot) if its not open already.
     * @param row row.
     * @param col column.
     */
    public void open(int row, int col) {
        if (opened.length <= row - 1 || opened[row - 1].length <= col - 1) {
            throw new IndexOutOfBoundsException();
        }
        if (isOpen(row, col)) {
            quf.connected(top, findIndexFlat(row, col));
        }
    }

    /**
     * is site (row, col) open.
     * @param row row.
     * @param col column.
     * @return true when open and false otherwise.
     */
    public boolean isOpen(int row, int col) {
        if (opened.length <= row - 1 || opened[row - 1].length <= col - 1) {
            throw new IndexOutOfBoundsException();
        }
        return opened[row - 1][col - 1];
    }

    /**
     * is site (row, column) full.
     * @param row
     * @param col
     * @return true when full and false otherwise.
     */
    public boolean isFull(int row, int col) {
        if (opened.length < row - 1 || opened[row - 1].length < col - 1) {
            throw new IndexOutOfBoundsException();
        }
        // connected ?
        return quf.connected(top, findIndexFlat(row, col));
    }

    /**
     * Whether percolates ot not.
     * @return true or false.
     */
    public boolean percolates() {
        // connection from top to bottom
        return quf.connected(top, bottom);
    }

    public int findIndexFlat(int row, int column) {
        return size * (row - 1) + column;
    }
}
