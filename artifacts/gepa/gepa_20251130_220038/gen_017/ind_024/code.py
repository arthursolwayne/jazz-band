
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Note durations based on 160 BPM and 4/4 time:
# Each beat = 0.375 seconds (60 / 160 = 0.375)
# Each 16th note = 0.1875s

# Bar 1: Drums alone (0.0 - 1.5s)
# Fill the bar with kick on 1 and 3, snare on 2 and 4, hihat on every 8th
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.1875)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.1875)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.375 + 0.1875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.125 + 0.1875)

# Hihat on every 8th
hihat_notes = [
    bar1_start + i * 0.1875 for i in range(8)
]
for h in hihat_notes:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.1875)
    drums.notes.append(hihat)

drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

# Bass line: Walking line in Dm, chromatic approaches
# Dm7: D F A C
# Let's walk D F G A C Bb B D
bass_notes = [
    (bar2_start, 2, 100),  # D
    (bar2_start + 0.375, 6, 100),  # F
    (bar2_start + 0.75, 7, 100),  # G
    (bar2_start + 1.125, 9, 100),  # A
    (bar2_start + 1.5, 11, 100),  # C
    (bar2_start + 1.875, 10, 100),  # Bb
    (bar2_start + 2.25, 11, 100),  # B
    (bar2_start + 2.625, 2, 100),  # D

    (bar3_start, 2, 100),  # D
    (bar3_start + 0.375, 6, 100),  # F
    (bar3_start + 0.75, 7, 100),  # G
    (bar3_start + 1.125, 9, 100),  # A
    (bar3_start + 1.5, 11, 100),  # C
    (bar3_start + 1.875, 10, 100),  # Bb
    (bar3_start + 2.25, 11, 100),  # B
    (bar3_start + 2.625, 2, 100),  # D

    (bar4_start, 2, 100),  # D
    (bar4_start + 0.375, 6, 100),  # F
    (bar4_start + 0.75, 7, 100),  # G
    (bar4_start + 1.125, 9, 100),  # A
    (bar4_start + 1.5, 11, 100),  # C
    (bar4_start + 1.875, 10, 100),  # Bb
    (bar4_start + 2.25, 11, 100),  # B
    (bar4_start + 2.625, 2, 100),  # D
]

for start, pitch, vel in bass_notes:
    bass_note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.1875)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7: D F A C
# Use root position and drop 2 or 3 voicings
piano_notes = []

# Bar 2: Chord on 2 (beat 2) and 4 (beat 4)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=11, start=bar2_start + 0.375, end=bar2_start + 0.5625))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=9, start=bar2_start + 0.375, end=bar2_start + 0.5625))  # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=7, start=bar2_start + 0.375, end=bar2_start + 0.5625))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=2, start=bar2_start + 0.375, end=bar2_start + 0.5625))  # D

piano_notes.append(pretty_midi.Note(velocity=100, pitch=11, start=bar2_start + 1.125, end=bar2_start + 1.3125))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=9, start=bar2_start + 1.125, end=bar2_start + 1.3125))  # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=7, start=bar2_start + 1.125, end=bar2_start + 1.3125))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=2, start=bar2_start + 1.125, end=bar2_start + 1.3125))  # D

# Bar 3: Same for beat 2 and 4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=11, start=bar3_start + 0.375, end=bar3_start + 0.5625))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=9, start=bar3_start + 0.375, end=bar3_start + 0.5625))  # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=7, start=bar3_start + 0.375, end=bar3_start + 0.5625))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=2, start=bar3_start + 0.375, end=bar3_start + 0.5625))  # D

piano_notes.append(pretty_midi.Note(velocity=100, pitch=11, start=bar3_start + 1.125, end=bar3_start + 1.3125))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=9, start=bar3_start + 1.125, end=bar3_start + 1.3125))  # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=7, start=bar3_start + 1.125, end=bar3_start + 1.3125))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=2, start=bar3_start + 1.125, end=bar3_start + 1.3125))  # D

# Bar 4: Same for beat 2 and 4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=11, start=bar4_start + 0.375, end=bar4_start + 0.5625))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=9, start=bar4_start + 0.375, end=bar4_start + 0.5625))  # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=7, start=bar4_start + 0.375, end=bar4_start + 0.5625))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=2, start=bar4_start + 0.375, end=bar4_start + 0.5625))  # D

piano_notes.append(pretty_midi.Note(velocity=100, pitch=11, start=bar4_start + 1.125, end=bar4_start + 1.3125))  # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=9, start=bar4_start + 1.125, end=bar4_start + 1.3125))  # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=7, start=bar4_start + 1.125, end=bar4_start + 1.3125))  # F
piano_notes.append(pretty_midi.Note(velocity=100, pitch=2, start=bar4_start + 1.125, end=bar4_start + 1.3125))  # D

piano.notes.extend(piano_notes)

# Sax: Motif — D F G A C Bb B D — one short phrase, sing it, leave it hanging
sax_notes = [
    (bar2_start, 2, 100),     # D
    (bar2_start + 0.375, 6, 100),  # F
    (bar2_start + 0.75, 7, 100),  # G
    (bar2_start + 1.125, 9, 100),  # A
    (bar2_start + 1.5, 11, 100),  # C
    (bar2_start + 1.875, 10, 100),  # Bb
    (bar2_start + 2.25, 11, 100),  # B
    (bar2_start + 2.625, 2, 100),  # D
]

for start, pitch, vel in sax_notes:
    sax_note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.1875)
    sax.notes.append(sax_note)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
