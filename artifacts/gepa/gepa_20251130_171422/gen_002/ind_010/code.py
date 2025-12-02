
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm
bass_notes = [
    (39, 1.5, 0.375), # Fm root (F) on 1
    (40, 1.875, 0.375), # Gb on 2
    (38, 2.25, 0.375), # Eb on 3
    (41, 2.625, 0.375), # Ab on 4
    (41, 2.625, 0.375), # Ab on 1
    (42, 3.0, 0.375), # Bb on 2
    (40, 3.375, 0.375), # Gb on 3
    (38, 3.75, 0.375), # Eb on 4
    (38, 3.75, 0.375), # Eb on 1
    (40, 4.125, 0.375), # Gb on 2
    (41, 4.5, 0.375), # Ab on 3
    (42, 4.875, 0.375), # Bb on 4
    (39, 4.875, 0.375), # F on 1
    (40, 5.25, 0.375), # Gb on 2
    (38, 5.625, 0.375), # Eb on 3
    (41, 6.0, 0.375)   # Ab on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - 7th chords comp on 2 and 4, in Fm
piano_notes = [
    (40, 1.875, 0.1875), # Gb (Fm7) on 2
    (41, 1.875, 0.1875), # Ab
    (43, 1.875, 0.1875), # Bb
    (45, 1.875, 0.1875), # Db
    (40, 2.625, 0.1875), # Gb (Fm7) on 4
    (41, 2.625, 0.1875), # Ab
    (43, 2.625, 0.1875), # Bb
    (45, 2.625, 0.1875), # Db
    (40, 4.125, 0.1875), # Gb (Fm7) on 2
    (41, 4.125, 0.1875), # Ab
    (43, 4.125, 0.1875), # Bb
    (45, 4.125, 0.1875), # Db
    (40, 4.875, 0.1875), # Gb (Fm7) on 4
    (41, 4.875, 0.1875), # Ab
    (43, 4.875, 0.1875), # Bb
    (45, 4.875, 0.1875)  # Db
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums - Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125))

# Sax - Motif
sax_notes = [
    (43, 1.5, 0.1875), # Bb on 1
    (40, 1.875, 0.1875), # Gb on 2
    (41, 2.25, 0.1875), # Ab on 3
    (40, 2.625, 0.1875), # Gb on 4
    (43, 2.625, 0.1875), # Bb on 1
    (40, 2.625, 0.1875), # Gb on 2
    (43, 3.0, 0.1875), # Bb on 3
    (41, 3.375, 0.1875), # Ab on 4
    (43, 4.5, 0.1875), # Bb on 1
    (40, 4.875, 0.1875), # Gb on 2
    (41, 5.25, 0.1875), # Ab on 3
    (43, 5.625, 0.1875) # Bb on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
