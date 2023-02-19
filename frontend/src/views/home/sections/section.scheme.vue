<script setup>
import { SvgScheme } from "~/components/svg";
import {
  ElementSchemeModal,
  ElementSchemeInfo,
  ElementSchemeTemperature,
  ElementSchemeProgress,
} from "~/components/elements";

const info = {
  info_kbc: [
    {
      title: "Разряжение, мм.в.ст",
      value: 75,
    },
    {
      title: "Уровень пыли, мг/м3",
      value: 2,
    },
  ],
  info_rotor: [
    {
      title: "Ток, А",
      value: 75,
    },
    {
      title: "Ток двигателя, А",
      value: 2,
    },
    {
      title: "Напряжение ротера, кВт",
      value: 75,
    },
    {
      title: "Напряжение статера, кВт",
      value: 2,
    },
  ],
};

const data = {
  ps1: {
    t: 222,
    v: 1,
    g: 1,
    o: 1,
  },
  ps2: {
    t: 222,
    v: 1,
    g: 1,
    o: 1,
  },
  ps3: {
    t: 222,
  },
  ps4: {
    t: 222,
  },
  ps5: {
    t: 222,
  },
  ps6: {
    t: 222,
  },
  ps7: {
    t: 222,
    v: 1,
    g: 1,
    o: 1,
  },
  ps8: {
    t: 222,
    v: 1,
    g: 1,
    o: 1,
  },
  ps9: {
    t: 222,
  },
};
</script>

<template>
  <div class="scheme">
    <svg-scheme />
    <element-scheme-modal
      title="8 ПС"
      :data="data.ps8"
      class="scheme__modal scheme__modal-ps8"
    />
    <element-scheme-modal
      title="9 ПС"
      :data="data.ps9"
      class="scheme__modal scheme__modal-ps9"
    />
    <element-scheme-modal
      title="7 ПС"
      :data="data.ps7"
      class="scheme__modal scheme__modal-ps7"
    />
    <element-scheme-modal
      title="6 ПС"
      :data="data.ps6"
      class="scheme__modal scheme__modal-ps6"
    />
    <element-scheme-modal
      title="5 ПС"
      :data="data.ps5"
      class="scheme__modal scheme__modal-ps5"
    />
    <element-scheme-modal
      title="4 ПС"
      :data="data.ps4"
      class="scheme__modal scheme__modal-ps4"
    />
    <element-scheme-modal
      title="3 ПС"
      :data="data.ps3"
      class="scheme__modal scheme__modal-ps3"
    />
    <element-scheme-modal
      title="2 ПС"
      :data="data.ps2"
      class="scheme__modal scheme__modal-ps2"
    />
    <element-scheme-modal
      title="1 ПС"
      :data="data.ps1"
      class="scheme__modal scheme__modal-ps1"
    />
    <element-scheme-info
      class="scheme__info scheme__info-kbc"
      :data="info.info_kbc"
    />
    <element-scheme-info
      class="scheme__info scheme__info-rotor"
      :data="info.info_rotor"
    />
    <element-scheme-temperature
      class="scheme__temp scheme__temp-oil"
      value="23"
    />
    <element-scheme-temperature
      class="scheme__temp scheme__temp-colder--down"
      value="123"
    />
    <element-scheme-temperature
      class="scheme__temp scheme__temp-colder--up"
      value="423"
    />
    <element-scheme-temperature
      class="scheme__temp scheme__pressure"
      value="423"
    />
    <element-scheme-progress
      class="scheme__progress scheme__progress-kbc"
      max="147"
      min="0"
      value="100"
      title="Температура газа, °C "
    />
    <element-scheme-progress
      class="scheme__progress scheme__progress-oil"
      max="187"
      min="0"
      value="34"
      title="УРОВЕНЬ МАСЛА, %"
    />
    <element-scheme-progress
      class="scheme__progress scheme__progress-pressure-oil"
      max="220"
      min="0"
      value="2,5"
      title="Давление масла, кг/см2"
    />
  </div>
</template>

<style lang="scss" scoped>
.scheme {
  position: relative;
  width: 1111px;
  height: 715px;
  margin-left: 100px;
  &__progress {
    position: absolute;
    &-kbc {
      top: 137px;
      left: 73px;
    }
    &-oil {
      top: 130px;
      left: 472px;
    }
    &-pressure-oil {
      top: 282px;
      right: 0px;
    }
  }
  &__pressure {
    top: 226px;
    right: 312px;
  }
  &__temp {
    position: absolute;
    &-oil {
      top: 117px;
      right: 345px;
    }
    &-colder {
      &--up {
        top: 26px;
        right: 190px;
      }
      &--down {
        top: 26px;
        right: 258px;
      }
    }
  }
  &__info {
    position: absolute;
    &-kbc {
      top: 180px;
      left: 70px;
    }
    &-rotor {
      top: 365px;
      right: 164px;
    }
  }
  &__modal {
    position: absolute;
    width: 120px;
    &-ps1 {
      bottom: 103px;
      left: 988px;
    }
    &-ps2 {
      bottom: 103px;
      left: 648px;
    }
    &-ps3 {
      bottom: 393px;
      left: 552px;
    }
    &-ps4 {
      bottom: 366px;
      left: 234px;
    }
    &-ps5 {
      bottom: 160px;
      left: 490px;
    }
    &-ps6 {
      bottom: 160px;
      left: 268px;
    }
    &-ps7 {
      bottom: 13px;
      left: 248px;
    }
    &-ps8 {
      bottom: 125px;
      left: -130px;
    }
    &-ps9 {
      left: -130px;
      bottom: 282px;
    }
  }
}
</style>
