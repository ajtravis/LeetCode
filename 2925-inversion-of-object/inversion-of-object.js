/**
 * @param {Object|Array} obj
 * @return {Object}
 */
var invertObject = function(obj) {
    let swapped = {}
    
    for (const key in obj) {
        if(!swapped[obj[key]]) {
          swapped[obj[key]] = key;
        }
        else if(typeof swapped[obj[key]] === 'string') { 
            swapped[obj[key]] = [swapped[obj[key]], key]
        } 
        else {
            swapped[obj[key]] = [...swapped[obj[key]], key]
            // swapped[obj[key]].push(key)
        }

        
      }
    return swapped
};