[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/nfa-vfxim/tk-multi-setframerange?include_prereleases)](https://github.com/nfa-vfxim/tk-multi-setframerange) 
[![GitHub issues](https://img.shields.io/github/issues/nfa-vfxim/tk-multi-setframerange)](https://github.com/nfa-vfxim/tk-multi-setframerange/issues) 


# Sync frame range with Flow Production Tracking <img src="icon_256.png" alt="Icon" height="24"/>

Sync the frame range in your scene with the one stored in Flow Production Tracking.

## Requirements

| ShotGrid version | Core version | Engine version |
|------------------|--------------|----------------|
| -                | v0.18.0      | -              |

## Configuration

### Strings

| Name                 | Description                                                                                                                                                                                         | Default value                                  |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| `menu_name`          | The name that will be shown in the Flow Production Tracking menu.                                                                                                                                   | Sync Frame Range with Flow Production Tracking |
| `sg_in_frame_field`  | The Flow Production Tracking field to use to retrieve the in frame. The app will look for this field on the entity associated with the current context (e.g. the current shot, current asset etc).  | sg_cut_in                                      |
| `sg_out_frame_field` | The Flow Production Tracking field to use to retrieve the out frame. The app will look for this field on the entity associated with the current context (e.g. the current shot, current asset etc). | sg_cut_out                                     |


### Hooks

| Name                   | Description                                                       | Default value                            |
|------------------------|-------------------------------------------------------------------|------------------------------------------|
| `hook_frame_operation` | Hook which contains all methods for setting/getting frame ranges. | {self}/frame_operations_{engine_name}.py |


