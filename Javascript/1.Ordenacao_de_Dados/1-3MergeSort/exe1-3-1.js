// left and right estao classificados
const merge = (leftArr, rightArr) => {

};


// recursiva
const mergeSort = array => {
  if (array.length <= 1){
    return array;
  }

  const middleIndex = Math.floor(array.length / 2);
  const leftArr = array.slice(0, middleIndex);
  const rightArr = array.slice(middleIndex)

  return merge;
};

console.log(mergeSort([4, 3, 9, 2, 7, 1, 5, 8], 0, 7))
