export default (mathFunction) => {
  const result = [];
  try {
    result.push(mathFunction());
  } catch (error) {
    result.push(error.toString());
  }
  result.push('Guardrail was processed');
  return result;
};