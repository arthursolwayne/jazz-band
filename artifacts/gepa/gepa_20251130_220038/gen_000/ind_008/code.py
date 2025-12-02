
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
for bar in range(1):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.0, end=time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.375, end=time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.75, end=time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 43),    # Fm root
    (1.875, 44),  # chromatic up
    (2.25, 42),   # b7
    (2.625, 43),  # root
    (2.875, 41),  # chromatic down
    (3.25, 40),   # b5
    (3.625, 41),  # chromatic up
    (4.0, 43),    # root
    (4.375, 44),  # chromatic up
    (4.75, 42),   # b7
    (5.125, 43),  # root
    (5.5, 41),    # chromatic down
    (5.875, 40),  # b5
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 57), (1.875, 50), (1.875, 53), (1.875, 55),  # F7
    (2.625, 57), (2.625, 50), (2.625, 53), (2.625, 55),  # F7
    (3.625, 57), (3.625, 50), (3.625, 53), (3.625, 55),  # F7
    (4.75, 57), (4.75, 50), (4.75, 53), (4.75, 55),       # F7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging, come back and finish it.
# Motif: F (43) - G (45) - Eb (41) - D (40)
sax_notes = [
    (1.5, 43), (1.5, 45), (1.5, 41), (1.5, 40),  # Start the motif
    (2.5, 43), (2.5, 45), (2.5, 41), (2.5, 40),  # Repeat it
    (3.5, 43), (3.5, 45), (3.5, 41), (3.5, 40),  # Repeat it again
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drum fills for bars 2-4
for bar in range(2, 4):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hi-hat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.0, end=time + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.375, end=time + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=time + 0.75, end=time + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
