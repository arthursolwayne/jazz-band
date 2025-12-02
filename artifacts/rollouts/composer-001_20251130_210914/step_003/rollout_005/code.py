
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
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 1.5),    # D (root)
    (63, 1.875, 1.875),# Eb (chromatic approach)
    (60, 2.25, 2.25),  # Bb (3rd)
    (59, 2.625, 2.625),# A (chromatic approach)
    (62, 3.0, 3.0),    # D
    (63, 3.375, 3.375),# Eb
    (60, 3.75, 3.75),  # Bb
    (59, 4.125, 4.125),# A
    (62, 4.5, 4.5),    # D
    (63, 4.875, 4.875),# Eb
    (60, 5.25, 5.25),  # Bb
    (59, 5.625, 5.625) # A
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 1.5),    # F7 (F, A, C, Eb)
    (66, 1.5, 1.5),
    (67, 1.5, 1.5),
    (62, 1.5, 1.5),
    # Bar 3
    (64, 2.625, 2.625),# F7
    (66, 2.625, 2.625),
    (67, 2.625, 2.625),
    (62, 2.625, 2.625),
    # Bar 4
    (64, 3.75, 3.75),  # F7
    (66, 3.75, 3.75),
    (67, 3.75, 3.75),
    (62, 3.75, 3.75)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: motif - Dm7 (D, F, A, C) with a twist on the 3rd bar
sax_notes = [
    (62, 1.5, 1.5),    # D
    (64, 1.875, 2.25), # F (held)
    (67, 2.25, 2.625), # A
    (65, 2.625, 3.0),  # Bb (chromatic approach)
    (62, 3.0, 3.0),    # D (rest)
    (62, 3.375, 3.75), # D
    (64, 3.75, 4.125), # F
    (67, 4.125, 4.5),  # A
    (65, 4.5, 4.875),  # Bb
    (62, 4.875, 5.25), # D
    (62, 5.25, 5.625), # D
    (64, 5.625, 6.0)   # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
