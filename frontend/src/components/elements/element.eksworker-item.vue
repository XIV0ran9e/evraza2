<script setup>
import { IconOkRound, IconArrowRight, IconSheme } from "~/components/icons";
import {
  ElementEksworkerSubtitle,
  ElementLastChange,
} from "~/components/elements";
import { CommonSelect, CommonInfoBlock } from "~/components/common";
import { enums } from "~/core/enum";
import { computed, onMounted, watch, ref } from "vue";

const props = defineProps({
  eksData: Object,
  worker: Object,
});

//todo refactor - no algoritm no time :(
const formattedEnum = ref({});

const formattedWorkers = ref({})

onMounted(() => {
  const { worker } = props;
  for (let key in worker) {
    formattedWorkers.value[key.replace(String.fromCharCode(92), "")] = worker[key]
  }
  formattedEnum.value = {
    p1: {
      temp_p1: worker[enums.p1['temp_p1']],
      vibration_p1: worker[enums.p1['vibration_p1']],
      horizontal_p1: worker[enums.p1['horizontal_p1']],
      vertical_p1: worker[enums.p1['vertical_p1']],
    },
    p2: {
      temp_p1: worker[enums.p2['temp_p2']],
      vibration_p1: worker[enums.p2['vibration_p2']],
      horizontal_p1: worker[enums.p2['horizontal_p2']],
      vertical_p1: worker[enums.p2['vertical_p2']],
    },
    p3: {
      temp_p1: worker[enums.p3['temp_p3']],
      vibration_p1: worker[enums.p3['vibration_p3']],
      horizontal_p1: worker[enums.p3['horizontal_p3']],
      vertical_p1: worker[enums.p3['vertical_p3']],
    },

    p4: {
      temp_p1: worker[enums.p4['temp_p4']],
      vibration_p1: worker[enums.p4['vibration_p4']],
      horizontal_p1: worker[enums.p4['horizontal_p4']],
      vertical_p1: worker[enums.p4['vertical_p4']],
    },
    p5: {
      temp_p1: worker[enums.p5['temp_p5']],
      vibration_p1: worker[enums.p5['vibration_p5']],
      horizontal_p1: worker[enums.p5['horizontal_p5']],
      vertical_p1: worker[enums.p5['vertical_p5']],
    },
    p6: {
      temp_p1: worker[enums.p6['temp_p6']],
      vibration_p1: worker[enums.p6['vibration_p6']],
      horizontal_p1: worker[enums.p6['horizontal_p6']],
      vertical_p1: worker[enums.p6['vertical_p6']],
    },

    p7: {
      temp_p1: worker[enums.p7['temp_p7']],
      vibration_p1: worker[enums.p7['vibration_p7']],
      horizontal_p1: worker[enums.p7['horizontal_p7']],
      vertical_p1: worker[enums.p7['vertical_p7']],
    },
    p8: {
      temp_p1: worker[enums.p8['temp_p8']],
      vibration_p1: worker[enums.p8['vibration_p8']],
      horizontal_p1: worker[enums.p8['horizontal_p1']],
      vertical_p1: worker[enums.p8['vertical_p1']],
    },
    p9: {
      temp_p1: worker[enums.p9['temp_p9']],
      vibration_p1: worker[enums.p9['vibration_p9']],
      horizontal_p1: worker[enums.p9['horizontal_p9']],
      vertical_p1: worker[enums.p9['vertical_p9']],
    },
  };
});

const emit = defineEmits('set')

const open = () => {
  emit('set', { ...formattedEnum.value })
}
</script>

<template>
  <div class="eksworker" @click="open">
    <header class="eksworker__header">
      <p class="eksworker__title">
        <icon-wrapper class="eksworker__status" width="12" height="12">
          <icon-ok-round />
        </icon-wrapper>
        {{ eksData.title }}
      </p>
      <button class="eksworker__button">
        <icon-wrapper width="8" height="8">
          <icon-arrow-right />
        </icon-wrapper>
      </button>
    </header>
    <div class="eksworker__content">
      <element-eksworker-subtitle
        :title="eksData.rotor_id"
        :date="eksData.rotor_installed"
        class="eksworker__subtitle"
      />
      <element-last-change :date="worker['breakdown_forecast']" class="eksworker__lastchange" />
      <icon-wrapper class="eksworker__scheme" width="211" height="118">
        <icon-sheme />
      </icon-wrapper>
      <div class="eksworker__info">
        <common-select class="eksworker__select" title="Предупреждение">
          <common-info-block title="№1 п-к" />
        </common-select>
        <common-select class="eksworker__select" title="Все подшипники">
          <!-- TODO to for :( -->
          <common-info-block type="p1" :status="formattedEnum.p1" title="№1 п-к" />
          <common-info-block type="p2" :status="formattedEnum.p2" title="№2 п-к" />
          <common-info-block type="p3" :status="formattedEnum.p3" title="№3 п-к" />
          <common-info-block type="p4" :status="formattedEnum.p4" title="№4 п-к" />
          <common-info-block type="p5" :status="formattedEnum.p5" title="№5 п-к" />
          <common-info-block type="p6" :status="formattedEnum.p6" title="№6 п-к" />
          <common-info-block type="p7" :status="formattedEnum.p7" title="№7 п-к" />
          <common-info-block type="p8" :status="formattedEnum.p8" title="№8 п-к" />
          <common-info-block type="p9" :status="formattedEnum.p9" title="№9 п-к" />
          <common-info-block type="oil" :status="formattedEnum.oil" title="Уровень масла" />
        </common-select>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.eksworker {
  cursor: pointer;
  border-radius: 7px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  height: fit-content;
  &__scheme {
    margin: 0 auto 20px auto;
  }
  &__header {
    background-color: var(--blocks-bg);
    color: var(--main-text-color);
    padding: 10px;
    display: flex;
    justify-content: space-between;
  }
  &__lastchange {
    margin: 14px 0 14px 0;
  }
  &__content {
    padding: 0 10px;
    border-radius: 0 0 7px 7px;
    background-color: var(--blocks-secondary-bg);
  }
  &__status {
    margin-right: 8px;
  }
  &__button {
    width: 35px;
    height: 35px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--main-text-color);
  }
  &__title {
    display: flex;
    align-items: center;
    font-size: 12px;
  }
}
</style>
