
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.125, 0.25),  # Hihat on &1
    (38, 0.5, 0.375),   # Snare on 2
    (42, 0.625, 0.25),  # Hihat on &2
    (36, 0.875, 0.375), # Kick on 3
    (42, 0.975, 0.25),  # Hihat on &3
    (38, 1.25, 0.375),  # Snare on 4
    (42, 1.375, 0.25)   # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line in Fm, chromatic approaches
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375), # Gb
    (62, 2.25, 0.375),  # D
    (61, 2.625, 0.375), # C
    (64, 2.875, 0.375), # F
    (65, 3.25, 0.375),  # Gb
    (62, 3.625, 0.375), # D
    (61, 4.0, 0.375),   # C
    (64, 4.25, 0.375),  # F
    (65, 4.625, 0.375), # Gb
    (62, 5.0, 0.375),   # D
    (61, 5.375, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.875, 0.375), # F7 (F, A, C, Eb)
    (69, 1.875, 0.375),
    (60, 1.875, 0.375),
    (62, 1.875, 0.375),
    # Bar 3
    (64, 3.25, 0.375),  # F7
    (69, 3.25, 0.375),
    (60, 3.25, 0.375),
    (62, 3.25, 0.375),
    # Bar 4
    (64, 4.625, 0.375), # F7
    (69, 4.625, 0.375),
    (60, 4.625, 0.375),
    (62, 4.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on &1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.125, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.5, end=start + 0.875))
    # Hihat on &2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.625, end=start + 0.875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.875, end=start + 1.25))
    # Hihat on &3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.975, end=start + 1.25))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.25, end=start + 1.625))
    # Hihat on &4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.375, end=start + 1.625))

# Sax - Dante: Motif, whisper to cry
sax_notes = [
    (64, 1.5, 0.375),   # F
    (66, 1.875, 0.375), # G
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 2.875, 0.375), # D
    (64, 3.25, 0.375),  # F
    (66, 3.625, 0.375), # G
    (62, 4.0, 0.375),   # D
    (60, 4.375, 0.375), # C
    (62, 4.625, 0.375), # D
    (66, 5.0, 0.375),   # G
    (64, 5.375, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('waynes_introduction.mid')
