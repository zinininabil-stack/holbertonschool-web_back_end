export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const selectedList = [...set].filter((value) => value.startsWith(startString));
  const cleanList = selectedList.map((value) => value.slice(startString.length));
  const result = cleanList.join('-');
  return result;
}