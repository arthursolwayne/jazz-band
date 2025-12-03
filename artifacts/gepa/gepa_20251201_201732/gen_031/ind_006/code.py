
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 0 (1)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on beat 1 (2)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5),       # D2
    (40, 1.875),     # F2
    (43, 2.25),      # G2
    (41, 2.625),     # F#2
    (38, 3.0),       # D2
    (40, 3.375),     # F2
    (43, 3.75),      # G2
    (41, 4.125),     # F#2
    (38, 4.5),       # D2
    (40, 4.875),     # F2
    (43, 5.25),      # G2
    (41, 5.625)      # F#2
]
for pitch, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # F#4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875))  # C#4

# Bar 3: G7 (G B D F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))  # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625))  # F4

# Bar 4: C7 (C E G B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375))  # B4)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 0 (1)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on beat 1 (2)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - G4 - D4 (with a slight chromatic step)
sax_notes = [
    (62, 1.5, 1.75),      # D4
    (67, 1.75, 2.0),      # F#4
    (67, 2.0, 2.25),      # F#4 (rest)
    (67, 2.25, 2.5),      # F#4
    (71, 2.5, 2.75),      # G4
    (67, 2.75, 3.0),      # F#4
    (62, 3.0, 3.25),      # D4
    (62, 3.25, 3.5),      # D4
    (62, 3.5, 3.75),      # D4
    (62, 3.75, 4.0),      # D4
    (62, 4.0, 4.25),      # D4
    (62, 4.25, 4.5),      # D4
    (62, 4.5, 4.75),      # D4
    (62, 4.75, 5.0),      # D4
    (62, 5.0, 5.25),      # D4
    (62, 5.25, 5.5),      # D4
    (62, 5.5, 5.75),      # D4
    (62, 5.75, 6.0)       # D4
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
