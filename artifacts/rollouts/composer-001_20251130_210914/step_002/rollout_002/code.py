
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
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.125),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches, Fm key
bass_notes = [
    (64, 1.5, 0.375),   # F
    (63, 1.875, 0.375), # Eb (chromatic)
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375),   # D
    (63, 3.375, 0.375), # Eb
    (65, 3.75, 0.375),  # F#
    (64, 4.125, 0.375), # F
    (62, 4.5, 0.375),   # D
    (60, 4.875, 0.375), # C
    (62, 5.25, 0.375),  # D
    (63, 5.625, 0.375)  # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comping around the sax
piano_notes = [
    # Bar 2
    (64, 1.875, 0.375), # F7 - F
    (71, 1.875, 0.375), # F7 - Bb
    (69, 1.875, 0.375), # F7 - E
    (67, 1.875, 0.375), # F7 - Ab
    (64, 2.625, 0.375), # F7 - F
    (71, 2.625, 0.375), # F7 - Bb
    (69, 2.625, 0.375), # F7 - E
    (67, 2.625, 0.375), # F7 - Ab
    # Bar 3
    (64, 3.375, 0.375), # F7 - F
    (71, 3.375, 0.375), # F7 - Bb
    (69, 3.375, 0.375), # F7 - E
    (67, 3.375, 0.375), # F7 - Ab
    (64, 4.125, 0.375), # F7 - F
    (71, 4.125, 0.375), # F7 - Bb
    (69, 4.125, 0.375), # F7 - E
    (67, 4.125, 0.375), # F7 - Ab
    # Bar 4
    (64, 4.875, 0.375), # F7 - F
    (71, 4.875, 0.375), # F7 - Bb
    (69, 4.875, 0.375), # F7 - E
    (67, 4.875, 0.375), # F7 - Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, A, G, F (Fm7)
# Start at bar 2, play first note, then let it ring while others play
sax_notes = [
    (64, 1.5, 0.75),  # F
    (69, 2.25, 0.75), # A
    (67, 3.0, 0.75),  # G
    (64, 3.75, 0.75)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_intro.mid")
