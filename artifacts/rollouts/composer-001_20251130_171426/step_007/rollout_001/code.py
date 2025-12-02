
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
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375), # F
    (38, 1.875, 0.375), # Eb
    (40, 2.25, 0.375), # Gb
    (41, 2.625, 0.375), # Ab
    (42, 3.0, 0.375), # Bb
    (43, 3.375, 0.375), # B
    (41, 3.75, 0.375), # Ab
    (39, 4.125, 0.375), # F
    (40, 4.5, 0.375), # Gb
    (42, 4.875, 0.375), # Bb
    (43, 5.25, 0.375), # B
    (41, 5.625, 0.375) # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    (43, 2.25, 0.375), # B7 (Fm7)
    (39, 2.25, 0.375),
    (42, 2.25, 0.375),
    (41, 2.25, 0.375),
    (43, 3.75, 0.375), # B7 (Fm7)
    (39, 3.75, 0.375),
    (42, 3.75, 0.375),
    (41, 3.75, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - Motif (start at bar 2)
sax_notes = [
    (42, 1.5, 0.375), # Gb (Fm)
    (40, 1.875, 0.375), # Eb
    (42, 2.25, 0.375), # Gb
    (44, 2.625, 0.375), # Ab
    (42, 3.0, 0.375), # Gb
    (40, 3.375, 0.375), # Eb
    (39, 3.75, 0.375), # F
    (42, 4.125, 0.375) # Gb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),  # Kick
    (38, 1.875, 0.375), # Snare
    (42, 1.5, 0.1875), # Hihat
    (42, 1.875, 0.1875),
    (36, 2.25, 0.375),  # Kick
    (38, 2.625, 0.375), # Snare
    (42, 2.25, 0.1875), # Hihat
    (42, 2.625, 0.1875),
    (36, 3.0, 0.375),  # Kick
    (38, 3.375, 0.375), # Snare
    (42, 3.0, 0.1875), # Hihat
    (42, 3.375, 0.1875),
    (36, 3.75, 0.375),  # Kick
    (38, 4.125, 0.375), # Snare
    (42, 3.75, 0.1875), # Hihat
    (42, 4.125, 0.1875),
    (36, 4.5, 0.375),  # Kick
    (38, 4.875, 0.375), # Snare
    (42, 4.5, 0.1875), # Hihat
    (42, 4.875, 0.1875),
    (36, 5.25, 0.375),  # Kick
    (38, 5.625, 0.375), # Snare
    (42, 5.25, 0.1875), # Hihat
    (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
