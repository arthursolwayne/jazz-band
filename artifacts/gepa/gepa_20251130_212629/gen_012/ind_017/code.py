
from mido import MidiFile, MidiTrack, Message, MetaMessage
import time

# Initialize MIDI file
mid = MidiFile(ticks_per_beat=480)
track = MidiTrack()
mid.tracks.append(track)

# Set tempo (160 BPM)
track.append(MetaMessage('set_tempo', tempo=480000, time=0))  # 60 BPM = 500000, so 160 BPM is 480000

# Define note durations and velocities
NOTE_DURATION = 480  # 1 beat = 480 ticks
VEL = 90  # Standard velocity

# Key: Dm (D, F, A, C)
# Scale: D Dorian (D, E, F, G, A, B, C)
# We'll use Dm7, G7, Cm7, F7 as the chord progression for four bars in Dm (Dorian mode)

# Define chord tones and passing tones
# Bar 1: Drums only
# Bar 2: Full ensemble (Dm7 over first 2 beats, G7 over 3-4)
# Bar 3: Dm7 over first 2 beats, G7 over 3-4
# Bar 4: Dm7 over first 2 beats, G7 over 3-4

# Drum pattern (Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth)
# Bar 1 (Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth)
drum_notes = [36, 38, 42, 36, 38, 42, 36, 38, 42, 36, 38, 42]  # Kick, Snare, Hi-hat
drum_times = [0, 0, 0, 96, 96, 96, 192, 192, 192, 288, 288, 288]
for note, time in zip(drum_notes, drum_times):
    track.append(Message('note_on', note=note, velocity=VEL, time=time))
    track.append(Message('note_off', note=note, velocity=VEL, time=NOTE_DURATION // 3))

# Bar 2: Full band
# Bass line (walking line in Dm7 -> G7)
bass_line = [62, 60, 61, 63, 65, 64, 63, 62]  # D, C, C#, D, F, E, D, C
bass_times = [0, 0, 0, 0, 96, 96, 96, 96]
for note, time in zip(bass_line, bass_times):
    track.append(Message('note_on', note=note, velocity=VEL, time=time))
    track.append(Message('note_off', note=note, velocity=VEL, time=NOTE_DURATION // 3))

# Piano comp: Dm7 on 2 and 4 (C, F, Am, D)
piano_notes = [60, 64, 64, 60, 64, 64, 60, 64]  # C, F, F, C, F, F, C, F
piano_times = [0, 0, 0, 0, 96, 96, 96, 96]
for note, time in zip(piano_notes, piano_times):
    track.append(Message('note_on', note=note, velocity=VEL, time=time))
    track.append(Message('note_off', note=note, velocity=VEL, time=NOTE_DURATION // 3))

# Saxophone solo: Start with a short motif that sings
# Motif: D (62) -> F (64) -> A (65) -> C (60) -> D (62)
sax_notes = [62, 64, 65, 60, 62]
sax_times = [0, 0, 0, 0, 96]
for note, time in zip(sax_notes, sax_times):
    track.append(Message('note_on', note=note, velocity=VEL, time=time))
    track.append(Message('note_off', note=note, velocity=VEL, time=NOTE_DURATION // 3))

# Bar 3: Repeat bass and piano pattern with slightly different voicings
# Bass line: D, C, C#, D, F, E, D, C
bass_line = [62, 60, 61, 63, 65, 64, 63, 62]
bass_times = [288, 288, 288, 288, 384, 384, 384, 384]
for note, time in zip(bass_line, bass_times):
    track.append(Message('note_on', note=note, velocity=VEL, time=time))
    track.append(Message('note_off', note=note, velocity=VEL, time=NOTE_DURATION // 3))

# Piano comp: G7 on 2 and 4 (B, D, F, G)
piano_notes = [62, 65, 67, 67, 62, 65, 67, 67]
piano_times = [288, 288, 288, 288, 384, 384, 384, 384]
for note, time in zip(piano_notes, piano_times):
    track.append(Message('note_on', note=note, velocity=VEL, time=time))
    track.append(Message('note_off', note=note, velocity=VEL, time=NOTE_DURATION // 3))

# Bar 4: Repeat sax motif but delayed and with space
# Motif: D (62) -> F (64) -> A (65) -> C (60) -> D (62)
sax_notes = [62, 64, 65, 60, 62]
sax_times = [576, 576, 576, 576, 672]
for note, time in zip(sax_notes, sax_times):
    track.append(Message('note_on', note=note, velocity=VEL, time=time))
    track.append(Message('note_off', note=note, velocity=VEL, time=NOTE_DURATION // 3))

# Save the MIDI file
mid.save('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
