# Custom Animations

Place your custom animation files (.fbx) in this folder.

## Custom Animation Sources:
- **Blender**: Create keyframe animations and export as FBX
- **Maya**: Professional animation software
- **Motion Capture**: Import mocap data
- **3ds Max**: Animation and export
- **Custom Keyframes**: Hand-crafted animations

## Export Settings for Blender:
```
Format: FBX
- Include: Armature, Mesh
- Transform: Apply Transform
- Animation: Include keyframes
- Armature: Only Deform Bones
```

## Export Settings for Maya:
```
Format: FBX
- Animation: Include
- Deformers: Include
- Constraints: Include
- Skeleton: Include
```

## File Naming Tips:
- Use descriptive names: `custom_dance.fbx`, `special_gesture.fbx`
- Include version numbers: `my_animation_v1.fbx`
- Avoid spaces, use underscores

## Example Files:
```
custom/
├── custom_dance_v1.fbx
├── special_gesture.fbx
├── unique_walk_cycle.fbx
├── character_intro.fbx
└── victory_pose.fbx
```

---
*Create amazing custom animations for your VRM models!*
