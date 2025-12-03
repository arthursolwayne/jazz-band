
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.5, end=bar1_start + 1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start, end=bar1_start + 1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 0.75, end=bar1_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: D2 (D2 = MIDI 38) starting on beat 1 of bar 2 (1.5s)
# Walking line: D2, F2, G2, A2, D2, F2, G2, A2
bass_notes = [38, 41, 43, 45, 38, 41, 43, 45]
bass_durations = [0.375] * 8
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + bass_durations[i]))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875))  # D (MIDI 50)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875))  # C

# Bar 3: Gm7 (G, Bb, D, F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625))  # F

# Bar 4: Cm7 (C, Eb, G, Bb)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375))  # Bb

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (MIDI 62), F4 (MIDI 65), G4 (MIDI 67), D4 (MIDI 62)

# First note at bar 2, beat 1 (1.5s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))  # D4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625))  # F4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375))  # G4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125))  # D4 again, delayed

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.5, end=start_time + 1.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 1.5))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5))

add_drums(1.5)
add_drums(3.0)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
