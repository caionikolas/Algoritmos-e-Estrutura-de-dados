function InsertionSort(n) {
  let atual
  for (let i = 1; i < n.length; i++) { 
    let j = i - 1
    atual = n[i]
    while (j >= 0 && atual > n[j]){
      n[j+1] = n[j]
      j--
    }
    n[j+1] = atual
  }
  return n
}

A = [31, 41, 59, 26, 41, 58]
B = [13, 2, 1, 3, 8, 5]

console.log(InsertionSort(A))
console.log(InsertionSort(B))