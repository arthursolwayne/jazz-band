
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: walking line in Fm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Fm7 -> Bb7 -> Eb7 -> Ab7
bass_notes = [
    (38, 1.5),  # F
    (43, 1.875), # Bb
    (43, 2.25),  # Bb
    (40, 2.625), # Eb
    (38, 2.625), # F
    (43, 2.625), # Bb
    (43, 3.0),   # Bb
    (38, 3.375), # F
    (43, 3.375), # Bb
    (40, 3.75),  # Eb
    (38, 3.75),  # F
    (43, 3.75),  # Bb
    (43, 4.125), # Bb
    (38, 4.5),   # F
    (43, 4.5),   # Bb
    (40, 4.875), # Eb
]
for pitch, start in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (Ab, C, F, D)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875))  # D

# Bar 3: Bb7 (D, F, Bb, A)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625))  # A

# Bar 4: Eb7 (G, Bb, Eb, D)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))  # D

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm -> Bb -> Eb -> Ab (F, Bb, Eb, Ab)
# Bar 2: F (66), Bb (69), Eb (64), Ab (62)
# Bar 3: F (66), Bb (69), Eb (64), Ab (62)
# Bar 4: F (66), Bb (69), Eb (64), Ab (62) -> with a slight delay on the last note

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125))  # Eb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375))  # Ab

# Bar 3
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25))  # Eb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5))  # Ab

# Bar 4
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=3.875))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.125))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.375))  # Eb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625))  # Ab

# Final note with a slight delay
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0))  # Ab

# Drums for Bars 2-4
for i in range(0, 6):
    for bar in range(2, 4):
        start = bar * 1.5 + i * 0.375
        if i % 2 == 0:
            # Kick on 1 and 3
            if i in [0, 2, 4]:
                drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
        else:
            # Snare on 2 and 4
            if i in [1, 3, 5]:
                drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
        # Hi-hat on every eighth
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
