// * | Global Components | * \\
import IconWrapper from '~/components/icon-wrapper.vue'
declare module '@vue/runtime-core' {
  export interface GlobalComponents {
    IconWrapper: typeof IconWrapper
  }
}
