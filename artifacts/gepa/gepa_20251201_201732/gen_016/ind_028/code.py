
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum notes: kick=36, snare=38, hihat=42
# Bar length is 1.5 seconds at 160 BPM

# Bar 1: Little Ray alone - 0.0 to 1.5 seconds
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar1_start = 0.0
bar1_end = 1.5

# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 1.125))

# Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.5))

# Hi-hat on every eighth
for i in range(0, 4):
    start = bar1_start + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# Bar 2: 1.5s - 3.0s
bar2_start = 1.5
bar2_end = 3.0

# Marcus: Walking bass line in D (D2 to G2, chromatic approaches)
# D2 (MIDI 38) -> Eb2 (MIDI 39) -> E2 (MIDI 40) -> F2 (MIDI 41) -> G2 (MIDI 43)
# This is a D7 root and fifth with chromatic approaches

# Bar 2 - D7
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=bar2_start, end=bar2_start + 0.375))  # G2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=39, start=bar2_start + 0.375, end=bar2_start + 0.75))  # Eb2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=bar2_start + 0.75, end=bar2_start + 1.125))  # E2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=bar2_start + 1.125, end=bar2_start + 1.5))  # G2

# Diane: Open voicings (D7 in bar 2)
# D7: D, F#, A, C#
# Open voicing: D (MIDI 62), A (MIDI 69), C# (MIDI 71), F# (MIDI 76)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar2_start, end=bar2_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar2_start, end=bar2_start + 1.5))

# Little Ray: same pattern as bar 1
# Kick, snare, hihat
for i in range(0, 4):
    start = bar2_start + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 0.75, end=bar2_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.375, end=bar2_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 1.125, end=bar2_start + 1.5))

# Dante: Tenor Sax - your motif
# D (MIDI 62) -> F# (MIDI 67) -> A (MIDI 69) -> G (MIDI 67)

# Start at bar2_start
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=bar2_start, end=bar2_start + 0.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 1.125, end=bar2_start + 1.5))

# Bar 3: 3.0s - 4.5s
bar3_start = 3.0
bar3_end = 4.5

# Marcus: Walking line - G7 (G2, B2, D3, F#3)
# G2 (MIDI 43) -> A2 (MIDI 45) -> B2 (MIDI 47) -> D3 (MIDI 50)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=bar3_start, end=bar3_start + 0.375))  # D3
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=bar3_start + 0.375, end=bar3_start + 0.75))  # A2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=bar3_start + 0.75, end=bar3_start + 1.125))  # B2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=bar3_start + 1.125, end=bar3_start + 1.5))  # D3

# Diane: Cmaj7 (C, E, G, B) open voicing
# C (MIDI 60), G (MIDI 67), B (MIDI 71), E (MIDI 64)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar3_start, end=bar3_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar3_start, end=bar3_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar3_start, end=bar3_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar3_start, end=bar3_start + 1.5))

# Little Ray: Same pattern
for i in range(0, 4):
    start = bar3_start + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 0.75, end=bar3_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.375, end=bar3_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.125, end=bar3_start + 1.5))

# Dante: Tenor Sax - repeat the motif, but with a slight variation
# D (MIDI 62) -> F# (MIDI 67) -> A (MIDI 69) -> Bb (MIDI 70) (slight chromatic shift)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=bar3_start, end=bar3_start + 0.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar3_start + 0.375, end=bar3_start + 0.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=bar3_start + 0.75, end=bar3_start + 1.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=bar3_start + 1.125, end=bar3_start + 1.5))

# Bar 4: 4.5s - 6.0s
bar4_start = 4.5
bar4_end = 6.0

# Marcus: Walking line - C7 (C2, E2, G2, B2)
# C2 (MIDI 36) -> D2 (MIDI 38) -> E2 (MIDI 40) -> G2 (MIDI 43)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=bar4_start, end=bar4_start + 0.375))  # G2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=bar4_start + 0.375, end=bar4_start + 0.75))  # D2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=40, start=bar4_start + 0.75, end=bar4_start + 1.125))  # E2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=bar4_start + 1.125, end=bar4_start + 1.5))  # G2

# Diane: G7 (G, B, D, F#) - open voicing
# G (MIDI 67), D (MIDI 62), F# (MIDI 69), B (MIDI 71)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar4_start, end=bar4_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar4_start, end=bar4_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar4_start, end=bar4_start + 1.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar4_start, end=bar4_start + 1.5))

# Little Ray: Same pattern
for i in range(0, 4):
    start = bar4_start + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 0.75, end=bar4_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.375, end=bar4_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.125, end=bar4_start + 1.5))

# Dante: Tenor Sax - finish the motif with a resolution into the G7
# D (MIDI 62) -> F# (MIDI 67) -> A (MIDI 69) -> G (MIDI 67)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=bar4_start, end=bar4_start + 0.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar4_start + 0.375, end=bar4_start + 0.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=bar4_start + 0.75, end=bar4_start + 1.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=bar4_start + 1.125, end=bar4_start + 1.5))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write('dante_intro.mid')
